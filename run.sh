#!/bin/bash

# Exit on error
set -e

# Check and create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
fi

# Run Python backend in background
cd backend
echo "Starting Python backend..."
sh run.sh &
cd ..
wait

# Run frontend in background
cd frontend
echo "Starting frontend..."
sh run.sh &
cd ..

# Start .NET backend (this one runs in the foreground)
echo "Starting .NET backend..."
dotnet run
