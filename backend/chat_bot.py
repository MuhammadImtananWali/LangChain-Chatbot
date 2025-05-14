from typing import List
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import APIRouter, status
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

router = APIRouter()


class Prompt(BaseModel):
    message: str


def get_llm():
    model_name = "gemini-2.0-flash"
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.3,
    )
    memory = ConversationBufferMemory()

    # Create a conversation chain with memory
    conversation = ConversationChain(llm=llm, memory=memory)
    return conversation


@router.post("/chat", status_code=status.HTTP_200_OK)
async def chat(prompt: Prompt):
    llm = get_llm()
    response = llm.predict(input=prompt.message)
    return {"response": response}
