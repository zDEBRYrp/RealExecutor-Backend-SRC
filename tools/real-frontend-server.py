"""Static server plus the recovered Real.exe hub_fetch transport.

This is transport only: it does not contain script/catalog data and it does
not execute or inject anything. The allowlist and request headers mirror the
native command recovered from Real.exe.
"""

from __future__ import annotations

import argparse
import http.server
import pathlib
import urllib.parse

import requests


ALLOWED_PREFIXES = (
    "https://haxhell.com/",
    "https://api.haxhell.com/",
    "https://api.projectreal.live/",
    "https://scriptblox.com/",
    "https://rscripts.net/",
    "https://robloxscripts.com/",
    "https://rawscripts.net/",
    "https://apis.roblox.com/",
    "https://thumbnails.roblox.com/",
)
REAL_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Real"


class RealFrontendHandler(http.server.SimpleHTTPRequestHandler):
    server_version = "RealFrontendTechnicalTransport/1.0"

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        parsed = urllib.parse.urlsplit(self.path)
        if parsed.path == "/__real/hub-fetch":
            self._hub_fetch(parsed.query)
            return
        super().do_GET()

    def _hub_fetch(self, query: str) -> None:
        values = urllib.parse.parse_qs(query, keep_blank_values=True)
        target = values.get("url", [""])[0]
        if not any(target.startswith(prefix) for prefix in ALLOWED_PREFIXES):
            self._send_text(403, "URL not allowed")
            return

        try:
            response = requests.get(
                target,
                headers={"User-Agent": REAL_USER_AGENT, "Accept": "*/*"},
                timeout=(10, 30),
            )
            body = response.content
            self.send_response(response.status_code)
            self.send_header("Content-Type", response.headers.get("Content-Type", "text/plain"))
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except requests.RequestException as error:  # transport failure, surfaced to frontend
            self._send_text(502, f"Request failed with {error}")

    def _send_text(self, status: int, text: str) -> None:
        body = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=pathlib.Path)
    parser.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Frontend root not found: {root}")

    handler = lambda *handler_args, **handler_kwargs: RealFrontendHandler(  # noqa: E731
        *handler_args, directory=str(root), **handler_kwargs
    )
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Serving recovered frontend from {root}")
        print(f"Native-compatible hub_fetch transport: http://127.0.0.1:{args.port}/__real/hub-fetch")
        print(f"Open http://127.0.0.1:{args.port}/?guest=1")
        server.serve_forever()


if __name__ == "__main__":
    main()
