from dotenv import load_dotenv
load_dotenv()

import os
import getpass

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "{system_message}",
    ),
    ("human", "{human_message}"),
])

chain = prompt | llm

question = input("Enter the question: ")

response = chain.invoke(
    {
        "system_message": "You are a helpful assistant",
        "human_message": question,
    }
)

print(f"AI: {response.content}")