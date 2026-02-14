from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    # Create a MultiServerMCPClient instance
    mcp_client = MultiServerMCPClient()

    # Create a ChatGroq instance
    chat_groq = ChatGroq()

    # Create a ReAct agent using the ChatGroq instance
    react_agent = create_react_agent(chat_groq)

    # Register the ReAct agent with the MCP client
    mcp_client.register_agent(react_agent)

    # Start the MCP client to listen for incoming requests
    await mcp_client.start()