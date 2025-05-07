from dotenv import load_dotenv
load_dotenv()

import os
import getpass

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

question = [
    (
        "system",
        "You are a helpful assistant that translates English to Urdu. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]

print(f"Human: {question}")
response = llm.invoke(question)
print(f"AI: {response.content}")