@echo off
setlocal enabledelayedexpansion

:: ==============================
:: CONFIGURATION
:: ==============================
set ADMIN_FULL_USER=subzero-compute\banven
set PROJECT_DIR=%~dp0
set LOG_FILE=%PROJECT_DIR%admin_secure_log.txt
set PYTHON_SCRIPT=%PROJECT_DIR%run_admin.py

:: ==============================
:: STEP 1: VERIFY ADMIN USER
:: ==============================
echo [INFO] Verifying user identity...
for /f "tokens=*" %%u in ('whoami') do set CURRENT_USER=%%u

if /i not "%CURRENT_USER%"=="%ADMIN_FULL_USER%" (
    echo [ERROR] Access Denied: This script can only be run by %ADMIN_FULL_USER%
    if exist "%LOG_FILE%" echo %DATE% %TIME% - Access Denied for user %CURRENT_USER% >> "%LOG_FILE%"
    pause
    exit /b 1
)

:: ==============================
:: STEP 2: LAUNCH ADMIN PANEL
:: ==============================
echo [INFO] Identity verified. Launching Admin Panel...
echo %DATE% %TIME% - Admin panel launched by %CURRENT_USER% >> "%LOG_FILE%"

cd /d "%PROJECT_DIR%"
python "%PYTHON_SCRIPT%"

if %errorlevel% neq 0 (
    echo [ERROR] Failed to launch admin panel! Error code: %errorlevel%
    echo %DATE% %TIME% - ERROR: Admin panel launch failed (code %errorlevel%) >> "%LOG_FILE%"
    pause
    exit /b 1
)

endlocal
