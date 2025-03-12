import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import os

async def main():
    # Initialize the OpenAI model
    model = ChatOpenAI(model="gpt-4")

    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="python",
        args=["math_server.py"],  # Path to your math server file
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            print("Agent response:", agent_response)

if __name__ == "__main__":
    asyncio.run(main()) 