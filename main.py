from dotenv import load_dotenv
load_dotenv()

import os
import getpass

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant",
    ),
    ("human", "{human_message}"),
])

output_parser=StrOutputParser()
chain = prompt | llm | output_parser

st.title("Chatbot using LangChain")
question = st.text_input("Enter your question:")

if question:
    response = chain.invoke(
    {
        "human_message": question,
    })
    st.write(response)

    print("Response:", response)