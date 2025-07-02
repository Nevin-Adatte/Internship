from typing import TypedDict, List
from langchain_core.messages import HumanMessage
#from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv # used to store secret stuff like API keys or configuration values
#from langchain_community.llms import HuggingFaceHub # Import HuggingFaceLLM
from langchain_huggingface import HuggingFaceEndpoint
import os
from langchain.chat_models import init_chat_model

load_dotenv()

class AgentState(TypedDict):
    messages: List[HumanMessage]


#llm = HuggingFaceEndpoint(repo_id="gpt2", huggingfacehub_api_token=API_Token)

os.environ["GOOGLE_API_KEY"] = "AIzaSyDkO8q56QqJzKY5pIScH-Sfyg5eGWlp3g0"
llm = init_chat_model("google_genai:gemini-2.0-flash")

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(f"\nAI: {response.content}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END) 
agent = graph.compile()

user_input = input("Enter: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter: ")