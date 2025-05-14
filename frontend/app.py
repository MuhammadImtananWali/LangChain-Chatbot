import streamlit as st
import requests

st.title("Gemini Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Define a callback function to handle the input submission
def send_message():
    user_input = st.session_state.user_input
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    if user_input:
        try:
            response = requests.post(
                "http://localhost:8000/chat", json={"message": user_input}
            )
            if response.status_code == 200:
                bot_response = response.json()["response"]
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": bot_response}
                )
            else:
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": f"Error: {response.status_code}"}
                )
        except Exception as e:
            st.session_state.chat_history.append(
                {"role": "assistant", "content": f"Request failed: {str(e)}"}
            )
    # Clear the input field after submission
    st.session_state.user_input = ""


# Text input field with on_change trigger
st.text_input(
    "You:",
    key="user_input",
    on_change=send_message,
)

# Display the chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
