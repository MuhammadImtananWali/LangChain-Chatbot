#!/bin/bash

# Exit on error
set -e

# Check and create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
fi

# Start Python backend in background
cd backend
echo "Starting Python backend..."
sh run.sh &
PY_BACKEND_PID=$!
cd ..

# Wait for backend to become available
echo "Waiting for Python backend to become ready..."
until curl -s http://localhost:8000/health > /dev/null; do
    sleep 1
done
echo "Python backend is ready."

# Start frontend in background
cd frontend
echo "Starting frontend..."
sh run.sh