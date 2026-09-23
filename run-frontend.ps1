$frontendRoot = Join-Path $PSScriptRoot 'frontend\frontend-root'
if (-not (Test-Path -LiteralPath $frontendRoot -PathType Container)) {
    throw "Recovered frontend root not found: $frontendRoot"
}
Write-Host "Serving recovered original frontend from $frontendRoot"
Write-Host "Open http://127.0.0.1:4173/ in a browser."
python -m http.server 4173 --directory $frontendRoot
