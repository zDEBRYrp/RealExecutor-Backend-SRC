# `hub_fetch`: проверка оригинального native fetch

Проверен оригинальный GUI-файл `backend/real-2.7.0/Real.exe`.

## Что найдено в PE

- В таблице Tauri-команд присутствует имя `hub_fetch`.
- В оригинальном Rust-коде присутствуют `reqwest 0.12.28` и `hyper 1.9.0`.
- Нативная реализация проверяет URL по префиксу до начала запроса.
- Для разрешённого URL выполняется GET и возвращается тело HTTP-ответа как текст.
- Строки из оригинального бинарника: `URL not allowed`, `Request failed with ` и `Mozilla/5.0 (Windows NT 10.0; Win64; x64) Real`.

Разрешённые оригиналом префиксы:

```text
https://haxhell.com/
https://api.haxhell.com/
https://api.projectreal.live/
https://scriptblox.com/
https://rscripts.net/
https://robloxscripts.com/
https://rawscripts.net/
https://apis.roblox.com/
https://thumbnails.roblox.com/
```

Зафиксированные адреса для аудита:

- `hub_fetch`: ASCII file offset `8823227` (`0x86A1BB`)
- allowlist/request state machine: кодовая область около VA `0x1402F6F20`
- URL allowlist начинается в `.rdata` около VA `0x140879010`
- `URL not allowed`: около VA `0x1408790EC`
- Real User-Agent: около VA `0x1408790FB`

## Что проверено по сети

Без добавления локальных карточек проверены настоящие HTTP-источники:

- `https://scriptblox.com/api/script/fetch?page=1&max=20` — `200`, JSON с реальными скриптами.
- `https://robloxscripts.com/api/v1/scripts?page=1&limit=20` — `200`, JSON с реальными скриптами.
- `https://api.projectreal.live/public/featured-scripts` — `200`, JSON с featured-данными.
- `https://api.projectreal.live/public/rscripts/scripts?...` — сейчас `404`; это устаревший маршрут, найденный в оригинальном production-бандле.
- `https://haxhell.com/api/v1/...` — native/PowerShell запрос отвечает, но браузерный CORS для прямого вызова не разрешён.

## Техническая обвязка для browser-only запуска

Оригинальный production frontend вызывает `hub_fetch` через Tauri IPC. В обычном HTTP-браузере Tauri native-команды отсутствуют, поэтому добавлена отдельная обвязка `tools/real-frontend-server.py`.

Она не содержит каталогов, карточек или скриптов. Она только обслуживает оригинальные статические файлы, принимает `/__real/hub-fetch?url=...`, повторяет найденный allowlist и User-Agent оригинала, делает реальный GET к внешнему источнику и передаёт тело и HTTP-статус обратно frontend.

Таким образом, `No scripts found` больше не маскируется демо-ответом. Если источник недоступен или отдаёт `404`, frontend получает ошибку запроса.

Нативное выполнение, инъекция и операции с памятью этой обвязкой не включаются.
