from typing import List
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import APIRouter, status

router = APIRouter()

# Store conversations by session ID
conversations = {}

class Prompt(BaseModel):
    message: str

def get_llm():
    model_name = "gemini-2.0-flash"
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.3,
    )
    return llm


@router.post("/chat", status_code=status.HTTP_200_OK)
async def chat(prompt: Prompt):
    llm = get_llm()
    response = llm.invoke(prompt.message)
    return {"response": response}