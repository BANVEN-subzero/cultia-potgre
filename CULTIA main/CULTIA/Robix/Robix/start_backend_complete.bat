
@echo off
echo ========================================
echo   Starting CULTIA Backend Setup
echo ========================================
echo.

cd /d "%~dp0backend"

REM Set your PostgreSQL password here (replace YOUR_PASSWORD with your actual postgres password)
set DATABASE_URL=dbname=cultia user=postgres password=Banven12199 host=localhost port=5345

echo Initializing database...
python init_db.py
if errorlevel 1 (
    echo.
    echo ❌ ERROR: Could not initialize database. Please check your password and try again!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Database initialized successfully!
echo   Starting backend server...
echo ========================================
echo.

python api.py
