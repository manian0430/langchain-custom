# LangChain MCP Adapters Example

This project demonstrates the use of Model Context Protocol (MCP) tools with LangChain and LangGraph. It includes a simple math server that provides addition and multiplication operations, which are then used by a LangChain agent.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix/MacOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```bash
# On Windows PowerShell
$env:OPENAI_API_KEY = "your-api-key-here"

# On Unix/MacOS
export OPENAI_API_KEY="your-api-key-here"
```

## Project Structure

- `math_server.py`: Implements an MCP server with add and multiply functions
- `math_client.py`: Implements a client that uses the math server's tools via LangChain
- `requirements.txt`: Lists all project dependencies

## Usage

1. Run the math client (it will automatically start the server):
```bash
python math_client.py
```

The client will execute a sample calculation: "(3 + 5) x 12"

## Features

- MCP server implementation with basic math operations
- LangChain integration with MCP tools
- Async client implementation
- GPT-4 powered agent for natural language math operations

## Dependencies

- langchain-mcp-adapters
- langgraph
- langchain-openai
- mcp>=1.3.0
- pydantic>=2.7.2
- httpx>=0.27
- httpx-sse>=0.4
- uvicorn>=0.23.1
- python-dotenv>=1.0.1 