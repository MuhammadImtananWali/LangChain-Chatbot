from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
question = "Hello, Whats the date today?"
print(f"Human: {question}")
response = llm.invoke(question)
print(f"AI: {response.content}")