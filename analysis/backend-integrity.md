# Backend integrity verification

The installed Real version was compared against the extracted copy. The six native components that form the installed backend/runtime set are present in the extracted tree and are byte-identical by SHA-256:

- `Real.exe` — GUI/Tauri host
- `bin/Real.exe` — native helper
- `bin/Real.dll`
- `bin/real-mcp.exe`
- `bin/luau-lsp.exe`
- `bin/Spoofer.exe`

Machine-readable sizes and hashes are in `backend-integrity.json`.

This verifies the backend binaries were downloaded/copied completely for the installed version. It does **not** mean the original Rust source, command handler source, symbols or a redistributable development backend was recovered. Those are not present in the installation; command names and behavior evidence come from production frontend/binary analysis.

User data was deliberately excluded: the DPAPI account vault, WebView2 profile databases/cookies, caches, shortcuts and setup logs must not be committed to GitHub.
