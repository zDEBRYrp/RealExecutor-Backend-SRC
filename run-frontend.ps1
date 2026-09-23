$frontendRoot = Join-Path $PSScriptRoot 'frontend\frontend-root'
$transport = Join-Path $PSScriptRoot 'tools\real-frontend-server.py'
if (-not (Test-Path -LiteralPath $frontendRoot -PathType Container)) {
    throw "Recovered frontend root not found: $frontendRoot"
}
if (-not (Test-Path -LiteralPath $transport -PathType Leaf)) {
    throw "Recovered hub_fetch transport not found: $transport"
}
Write-Host "Serving recovered original frontend from $frontendRoot"
Write-Host "Open http://127.0.0.1:4173/ in a browser."
python $transport --port 4173 --root $frontendRoot
