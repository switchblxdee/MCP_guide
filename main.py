import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from settings import Settings
from model import GroqModel
from langgraph.prebuilt import create_react_agent

settings = Settings()

async def main():
    print("🚀 Инициализация MCP клиента...")

    client = MultiServerMCPClient({
        "demo": {
            "command": "python",
            "args": ["mcp_server.py"],
            "transport": "stdio",
        }
    })

    print("📦 Получение инструментов из MCP сервера...")
    tools = await client.get_tools()
    print(f"✅ Получено {len(tools)} инструментов")

    print("🤖 Инициализация модели...")
    model = GroqModel()
    llm = model._init_model()
    
    # Создаем агента
    print("🔧 Создание агента...")
    agent = create_react_agent(
        tools=tools,
        model=llm
    )

    print("\n🧪 Тестирование агента...")
    result = agent.invoke({
        "messages": [{"role": "user", "content": "Привет, какие tools у тебя доступны?"}]
    })
    print(f"🤖 Ответ: {result['messages'][-1].content}")

if __name__ == "__main__":
    asyncio.run(main())