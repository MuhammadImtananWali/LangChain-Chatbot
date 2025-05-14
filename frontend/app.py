import streamlit as st
import requests

st.title("Gemini Chatbot")


# Define a callback function to handle the input submission
def send_message():
    user_input = st.session_state.user_input
    if user_input:
        try:
            response = requests.post(
                "http://localhost:8000/chat", json={"message": user_input}
            )
            if response.status_code == 200:
                st.session_state.chat_response = response.json()["response"]["content"]
            else:
                st.session_state.chat_response = f"Error: {response.status_code}"
        except Exception as e:
            st.session_state.chat_response = f"Request failed: {str(e)}"


# Text input field with on_change trigger
st.text_input(
    "You:",
    key="user_input",
    on_change=send_message,
)

# Display the response
if "chat_response" in st.session_state:
    st.write("Bot:", st.session_state.chat_response)
