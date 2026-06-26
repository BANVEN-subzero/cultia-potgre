
@echo off
echo Requesting administrator privileges...
powershell -Command "Start-Process powershell -Verb RunAs -ArgumentList '-NoExit', '-Command', 'Restart-Service -Name postgresql-x64-18 -Force; Start-Sleep -Seconds 3; Get-Service -Name postgresql-x64-18; Write-Host ''Service restarted! Now you can run the backend!'' -ForegroundColor Green'"
