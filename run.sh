#!/bin/bash
# DeskTick launcher script for Linux/macOS

echo "Starting DeskTick..."

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 not found. Please install Python 3.7 or higher."
    exit 1
fi

# Run the application
python3 main.py

# Check exit status
if [ $? -ne 0 ]; then
    echo "Error: Failed to start DeskTick."
    exit 1
fi
