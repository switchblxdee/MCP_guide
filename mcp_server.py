from mcp.server.fastmcp import FastMCP
from langchain_community.tools import TavilySearchResults
from settings import Settings

mcp = FastMCP("Demo MCP Server")

@mcp.tool()
def tavily_search(query: str) -> str:
    """Поиск в Интернете с использованием API Tavily."""
    tavily_tool = TavilySearchResults(tavily_api_key=Settings.TAVILY_API, max_results=3)
    return tavily_tool.run(query)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Сложить два числа и вернуть результат."""
    return a + b

@mcp.tool()
def reverse(text: str) -> str:
    """Реверсировать строку и вернуть результат."""
    return text[::-1]

@mcp.tool()
def greet(name: str) -> str:
    """Сгенерировать приветствие для пользователя по имени."""
    return f"Привет, {name}!"

if __name__ == "__main__":
    mcp.run(transport="stdio")
