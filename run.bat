@echo off
REM DeskTick launcher script for Windows

echo Starting DeskTick...

REM Check if python is available
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: python not found. Please install Python 3.7 or higher.
    pause
    exit /b 1
)

REM Run the application
python main.py

REM Check exit status
if %errorlevel% neq 0 (
    echo Error: Failed to start DeskTick.
    pause
    exit /b 1
)
