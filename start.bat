@echo off
title Nivo MP3

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed.
    echo Download it from: https://www.python.org/downloads/
    pause
    exit /b
)

echo Installing dependencies...
pip install -r requirements.txt

echo Starting Nivo MP3...
python main.py

pause
