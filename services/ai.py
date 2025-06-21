import os
import requests
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from datetime import datetime
load_dotenv()

AI_API_KEY = os.getenv("AI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    verbose=True,
    streaming=True,
    google_api_key=AI_API_KEY,
)

tools = [
    Tool(name="DownloadSong", func=download_song, description="Download songs from YouTube. Use format: 'song by artist'."),
    Tool(name="GetLyrics", func=get_lyrics, description="Get song lyrics from YouTube description. Use format: 'song by artist'.")
]

agents = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True),
)

def get_response(prompt: str):
    response = agents.run(prompt)
    return response