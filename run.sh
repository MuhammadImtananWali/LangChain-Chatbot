#!/bin/bash

# Check and create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
fi


# Install shared requirements once (if any)
# pip install -r requirements.txt   # Uncomment if needed

# Run frontend and backend in parallel
(cd frontend && sh run.sh) &
frontend_pid=$!

(cd backend && sh run.sh) &
backend_pid=$!

# Wait for frontend and backend
wait $frontend_pid
wait $backend_pid

# Start .NET backend after Python services
dotnet run
