# Frontend authenticity and launch verification

Status: **verified recovered production frontend; native backend remains external**.

## Evidence and entry point

The extracted application is a SvelteKit production build. The technical wrapper is only `recovered/frontend/frontend-root/index.html`; all files below `/_app/immutable/` and the public assets are recovered Real production resources.

- SvelteKit bootstrap: `/_app/immutable/entry/start.BXGHPMMc.js`.
- SvelteKit app manifest: `/_app/immutable/entry/app.C9GxT-3O.js`.
- Manifest exports `nodes`, `root`, `dictionary`, `server_loads`, `matchers` and `hooks`.
- The manifest route dictionary is `{"/":[2]}`: there is one normal route, `/`, whose leaf is node 2.
- Node 0 is the root layout/application shell; node 1 is the error page; node 2 is the route bootstrap/auxiliary-window component.

This confirms that `nodes/0.CYB2H8S_.js` is the root application shell by manifest linkage and by its actual code, not by filename guesswork. Its internal view state contains Home/Overview, Editor, Accounts and Settings. Editor and Settings are not separate SvelteKit URLs in this build; they are views selected inside the root shell.

## Actual recovered UI structure

The root shell contains the original Real UI and references the original labels and components for Welcome/Home, script editor/Explorer/Monaco/terminal/output, Accounts and Settings. Node 2 handles the query-driven auxiliary windows (`undocked-script`, `undocked-panel`, `theme-editor`) through dynamic imports. Node 1 is only the SvelteKit error component.

Dynamic import and route evidence is machine-readable in `analysis/frontend-invoke-calls.json` and `analysis/frontend-tauri-plugin-calls.txt`; the complete static resource inventory is in `analysis/embedded-frontend-assets.json` and `analysis/frontend-static-assets.json`.

## Assets

The recovered tree contains 46 embedded SvelteKit JS/CSS resources and the recovered public assets, including Monaco loader/editor resources, Lottie data, backgrounds, icons, providers, launcher images and data JSON. The original development `.svelte`/`.ts` sources and usable source-map `sourcesContent` were not present; the production bundles themselves were recovered and passed syntax validation.

## Run verification

The original production frontend was served unchanged from `frontend-root` with a minimal technical wrapper. In a local WebView2 browser, it rendered:

1. the original Real splash screen;
2. the original Real window chrome and Welcome/auth screen with the original “Continue with Discord”, “Use another sign-in method” and “Create account” controls.

This is a successful visual launch of the recovered frontend, not a replacement design. The screenshot was captured from the running page during this verification.

For the requested frontend test, the technical wrapper now provides an explicitly labelled Guest mode. It feeds the recovered root shell a neutral Guest session and safe UI-test responses, without implementing native executor actions. With that mode, the original Home/Overview, Editor and Settings views were opened through their original navigation controls and visually verified. This is a frontend test session, not a real account or native backend session.

## Technical wrapper boundary

The wrapper consists only of `index.html`, `_app/version.json` and the explicit Tauri static stub in the wrapper. It loads the recovered SvelteKit entry and recovered CSS. The stub records attempted IPC calls in `__REAL_INVOKES__` and returns neutral values so that the visual shell can mount; Guest mode adds only UI-test responses for session/access/profile/version/GitHub status. It does not implement Real behavior, injection, account handling, native file operations or executor functionality. It must not be confused with the original backend.

## Backend and IPC conclusion

The frontend imports the Tauri 2 bridge from `LvMcih3f.js` and directly uses `window.__TAURI_INTERNALS__` (`invoke`, `transformCallback`, `metadata.currentWindow.label`) and `window.__TAURI_EVENT_PLUGIN_INTERNALS__`. The recovered source does not depend on a legacy `window.__TAURI__` object. Exact frontend occurrences of recovered application commands are listed in `frontend-invoke-calls.json`; framework calls are listed in `frontend-tauri-plugin-calls.txt`.

The GUI `Real.exe` is a Tauri/WRY/WebView2 PE. Its frontend is embedded in the executable as compressed asset records and served through Tauri's internal asset protocol; there is no external `frontend-root` directory that the original binary automatically reads. The extracted GUI executable is byte-identical to the installed GUI executable (see `analysis/launch-note.md` and `analysis/pe-info.json`). The separate `bin/Real.exe` is a native helper, not the WebView host.

Therefore a static HTTP copy can display the original production UI, but it cannot make that UI use the original native backend. Making the unmodified original EXE load an externally modified frontend would require a supported external-resource/configuration path (not found), or binary/resource/protocol patching/repacking of the GUI executable. No such patch was performed. Replacing only files beside the EXE is insufficient.

## Result against the requested success criterion

- **A (original EXE + modifiable external frontend): not demonstrated and not supported by the recovered packaging evidence.**
- **B (confirmed technical report): achieved.** The original frontend is recovered and independently launchable for modification at `recovered/frontend/frontend-root`; the original native backend is embedded behind the Tauri asset protocol and cannot be attached to that HTTP copy by file replacement alone. A real editable frontend/backend combination would require either the vendor's original source/build configuration or a controlled modification of the GUI host's asset-loading path, while preserving the existing native command surface.
