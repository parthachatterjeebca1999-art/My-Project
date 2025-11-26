@echo off
REM Somnath Portfolio - Local Server Runner

echo.
echo ========================================
echo  Somnath Portfolio - Local Server
echo ========================================
echo.

REM Try Python 3
python3 -m http.server 8000
if %errorlevel% equ 0 goto :success

REM Try Python
python -m http.server 8000
if %errorlevel% equ 0 goto :success

REM Try Node.js http-server
npx http-server -p 8000
if %errorlevel% equ 0 goto :success

REM If all fail
echo.
echo ERROR: Could not start server
echo.
echo Please install one of:
echo 1. Python 3: https://www.python.org/downloads/
echo 2. Node.js: https://nodejs.org/
echo.
pause
exit /b 1

:success
echo.
echo Server started successfully!
echo Open your browser and go to: http://localhost:8000
echo.
pause
