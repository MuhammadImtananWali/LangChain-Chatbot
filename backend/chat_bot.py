from pydantic import BaseModel
from fastapi import APIRouter, status
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, MessagesState, StateGraph

router = APIRouter()

workflow = StateGraph(state_schema=MessagesState)

messages = []


class Prompt(BaseModel):
    message: str


def initialize_app():
    model_name = "gemini-2.0-flash"
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.3,
    )

    # ----------Set up memory start ----------

    def call_model(state: MessagesState):
        response = llm.invoke(state["messages"])
        return {"messages": response}

    workflow.add_edge(START, "model")
    workflow.add_node("model", call_model)

    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)

    # ----------Set up memory end ----------

    return app


app = initialize_app()


@router.post("/chat", status_code=status.HTTP_200_OK)
async def chat(prompt: Prompt):
    global messages

    input_messages = [HumanMessage(prompt.message)]
    response = app.invoke(
        {"messages": input_messages}, {"configurable": {"thread_id": "abc123"}}
    )
    messages = response["messages"]
    return {"response": response["messages"][-1]}


@router.get("/chats")
async def get_all_messages():
    """
    Get all messages from the memory.
    """
    simplified_messages = [
        {"role": message.type, "content": message.content} for message in messages
    ]
    return {"chats": simplified_messages}
