<#
.SYNOPSIS
  Run, lint, or compile this mod using the Ren'Py 6.99.12.4 runtime bundled with DDLC.

.EXAMPLE
  .\tools\run.ps1            # launch the mod
  .\tools\run.ps1 lint       # check scripts for errors
  .\tools\run.ps1 compile    # compile .rpy -> .rpyc

  Set $env:DDLC_DIR if DDLC isn't installed at the Steam default path.
#>
param([string]$Command = "")

$ErrorActionPreference = "Stop"

$ddlc = $env:DDLC_DIR
if (-not $ddlc) {
    $ddlc = "C:\Program Files (x86)\Steam\steamapps\common\Doki Doki Literature Club"
}
$exe = Join-Path $ddlc "lib\windows-i686\DDLC.exe"
$py  = Join-Path $ddlc "DDLC.py"
if (-not (Test-Path $exe)) {
    throw "DDLC runtime not found at '$ddlc'. Set `$env:DDLC_DIR to your DDLC install folder."
}

$project = Split-Path -Parent $PSScriptRoot

# DDLC only allows one running instance; lint/launch silently quit otherwise.
if (Get-Process DDLC -ErrorAction SilentlyContinue) {
    throw "DDLC (or this mod) is already running. Close the game window and try again."
}

foreach ($rpa in "audio.rpa", "images.rpa", "fonts.rpa") {
    if (-not (Test-Path (Join-Path $project "game\$rpa"))) {
        Write-Host "Copying $rpa from DDLC..."
        Copy-Item (Join-Path $ddlc "game\$rpa") (Join-Path $project "game\$rpa")
    }
}

# Turns on Ren'Py developer mode (Shift+R reload, Shift+O console, dev menu).
$env:DDLC_MOD_DEV = "1"

$argList = @("-EO", "`"$py`"", "`"$project`"")
if ($Command) { $argList += $Command }

if ($Command) {
    # lint/compile: wait and show output
    & $exe -EO $py $project $Command
    if ($Command -eq "lint" -and (Test-Path (Join-Path $project "lint.txt"))) {
        Get-Content (Join-Path $project "lint.txt")
    }
} else {
    Start-Process -FilePath $exe -ArgumentList $argList -WorkingDirectory $project
}
