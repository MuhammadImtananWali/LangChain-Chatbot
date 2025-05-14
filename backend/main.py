import os
import getpass
from dotenv import load_dotenv
from fastapi import FastAPI
from chat_bot import router as chat_router

load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

app = FastAPI(title="Gemini Chatbot")

app.include_router(chat_router)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
