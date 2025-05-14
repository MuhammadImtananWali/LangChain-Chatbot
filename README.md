# Chatbot using LangChain

This repository hosts a chatbot built with LangChain.

## Prerequisites

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

## Starting the Application

Run the following command to start both the frontend and backend:
```bash
sh run.sh
```

## Environment Variables

1. `GOOGLE_API_KEY`: Replace with your Google API key.
2. `LANGSMITH_TRACING`: Set to `true` or `false` to enable or disable tracing.
3. `LANGSMITH_API_KEY`: Replace with your Langsmith API key.
4. `LANGSMITH_PROJECT`: Replace with your Langsmith project name.