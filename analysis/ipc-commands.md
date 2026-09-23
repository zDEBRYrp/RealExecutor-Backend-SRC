# Recovered native command map

The following names are `[RECOVERED]` from the original Rust command registration/string table and related frontend/runtime data. Exact argument schemas and return types are `[UNKNOWN]` unless stated. These are not reimplemented handlers.

## Application and GUI

| Command(s) | Evidence / likely purpose | Status |
|---|---|---|
| `load_settings`, `save_settings`, `fload_settings` | settings persistence | `[RECOVERED]` name; signature `[UNKNOWN]` |
| `get_real_version`, `check_for_updates`, `start_real_repair`, `run_real_update` | version/update lifecycle | `[RECOVERED]`; signature `[UNKNOWN]` |
| `get_system_info`, `get_installed_versions`, `get_latest_roblox_version`, `get_previous_roblox_version`, `get_running_roblox_version`, `validate_roblox_version`, `install_roblox_client` | client/version information | `[RECOVERED]`; signature `[UNKNOWN]` |
| `open_path_in_explorer`, `select`, `open_folder_in_explorer`, `open_script_in_explorer`, `open_script_in_vscode`, `open_in_vscode` | file/editor integration | `[RECOVERED]`; signature `[UNKNOWN]` |
| `read_file_path`, `write_file_path`, `get_file_path`, `read_dropped_file`, `read_image_data_url` | local file bridge | `[RECOVERED]`; signature `[UNKNOWN]` |
| `openf`, `open_path`, `save_output_file`, `savefrun_real_update` | dialogs/actions inferred from names | `[RECOVERED]` names only |
| `exit_app`, `restart_app`, `close_app`, `restart_app` | process/window lifecycle | `[RECOVERED]`; signature `[UNKNOWN]` |
| `set_theme`, `save_theme_config`, `list_theme_configs`, `get_theme_dir`, `get_themes_dir`, `add_theme_to_folder`, `update_theme_config`, `delete_theme_config` | theme system | `[RECOVERED]`; signature `[UNKNOWN]` |
| `undock_panels`, `snapshot_undock`, `remove_undocked_panel`, `dock_panel`, `update_undocked_panel`, `get_undocked_panel`, `close_all_undocked_panels`, plus script-tab variants | panel/window docking | `[RECOVERED]`; signature `[UNKNOWN]` |

## Editor, scripts and LSP

| Command(s) | Evidence / likely purpose | Status |
|---|---|---|
| `read_editor_session_index`, `save_editor_session_index`, `clear_editor_session_files`, `read_editor_session_file`, `delete_editor_session_files`, `write_vscode_sync`, `read_vscode_from_sync` | editor/session persistence and VS Code sync | `[RECOVERED]`; disk protocol also observed in embedded extension |
| `get_folder_tree`, `get_folder_scripts`, `create_script`, `delete_script`, `rename_script`, `move_scripts`, `create_folder`, `delete_folder`, `rename_folder`, `add_explorer_custom_root`, `remove_explorer_custom_root`, `rename_explorer_custom_root` | Explorer/script management | `[RECOVERED]`; signature `[UNKNOWN]` |
| `runtime_lsp_snapshot`, `luau_lsp_start`, `luau_lsp_restart`, `luau_lsp_clear_runtime_tree`, `luau_lsp_apply_runtime_tree`, `luau_lsp_notify`, `luau_lsp_request`, `luau_lsp_open_document`, `luau_lsp_change_document`, `luau_lsp_close_document`, `luau_lsp_document_uri` | Luau language server | `[RECOVERED]`; signature `[UNKNOWN]` |
| `read_console_output`, `start_console_watch`, `stop_console_watch`, `start_console_watch` | terminal/output integration | `[RECOVERED]`; signature `[UNKNOWN]` |

## Roblox/account/runtime families

The binary contains extensive registered names under `accounts`, `roblox_api`, `injection`, `process_memory`, `altgen`, `workspace`, `spoofer`, `mcp`, and `github_gists`. Representative recovered names include `get_accounts`, `add_account`, `remove_account`, `import_accounts`, `export_accounts`, `launch_roblox_as_account`, `prepare_attach`, `inject_instances`, `inject_executor`, `execute_in_instance`, `inject_exec`, `get_roblox_instances`, `stop_console_watch`, `spawn_spoofer`, `authorize_spoof_run`, `abort_spoof_run`, `process_priority`, `set_process_memory_limit`, `get_folder_tree`, `cloud_scripts_list`, `github_gist_list`, `github_gist_read_file`, and `github_gist_update_file`.

These names prove backend surface area, not working access to the proprietary runtime. Arguments, return values, permission checks, authentication and side effects remain `[UNKNOWN]` without dynamic tracing or source/debug symbols.

## Tauri plugin commands

The standard runtime exposes recovered plugin namespaces such as `plugin:window|...`, `plugin:webview|...`, `plugin:opener|...`, `plugin:path|...`, `plugin:resources|...`, `plugin:tray|...`, `plugin:menu|...`, and `plugin:event|...`. Window/webview names include close, show, hide, minimize, maximize, resize, position, focus, drag, devtools, zoom, and browsing-data operations. These are framework commands, not application-specific Real commands.
