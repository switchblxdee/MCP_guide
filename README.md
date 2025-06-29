# MCP (Model Context Protocol) Guide

## Что такое MCP?

**Model Context Protocol (MCP)** — это открытый протокол для подключения AI-моделей к внешним данным и инструментам. MCP позволяет создавать серверы, которые предоставляют инструменты (tools) для AI-моделей, расширяя их возможности.

### Основные концепции:

- **MCP Server** — сервер, который предоставляет инструменты и данные
- **MCP Client** — клиент, который подключается к серверам и использует их инструменты
- **Tools** — функции, которые может вызывать AI-модель (например, поиск в интернете, работа с файлами, API вызовы)

## Как работает MCP?

1. **Сервер** регистрирует инструменты и запускается
2. **Клиент** подключается к серверу и получает список доступных инструментов
3. **AI-модель** использует инструменты через клиента для выполнения задач
4. **Результаты** возвращаются модели для дальнейшей обработки

## Архитектура проекта

```
MCP_guide/
├── mcp_server.py      # MCP сервер с инструментами
├── main.py           # Клиент и агент
├── model.py          # Модель Groq
├── settings.py       # Настройки
├── requirements.txt  # Зависимости
└── README.md        # Этот файл
```

## Установка и запуск

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
GROQ_API=your_groq_api_key_here
MODEL_NAME=llama3-8b-8192
MCP_SERVER_URL=http://127.0.0.1:8000
TAVILY_API=your_tavily_api_key_here
```

### 3. Получение API ключей

- **Groq API**: Зарегистрируйтесь на [groq.com](https://groq.com)
- **Tavily API**: Зарегистрируйтесь на [tavily.com](https://tavily.com)

### 4. Запуск проекта

```bash
python main.py
```

## Доступные инструменты

В данном проекте реализованы следующие инструменты:

### 1. `tavily_search`
- **Описание**: Поиск информации в интернете
- **Параметры**: `query` (строка)
- **Пример**: Поиск новостей, информации о технологиях

### 2. `add`
- **Описание**: Сложение двух чисел
- **Параметры**: `a` (int), `b` (int)
- **Пример**: `add(5, 3)` → `8`

### 3. `reverse`
- **Описание**: Переворачивание текста
- **Параметры**: `text` (строка)
- **Пример**: `reverse("hello")` → `"olleh"`

### 4. `greet`
- **Описание**: Создание приветствия
- **Параметры**: `name` (строка)
- **Пример**: `greet("Анна")` → `"Привет, Анна!"`

## Транспорты MCP

### stdio (рекомендуется)
- Простой и надежный
- Работает через стандартный ввод/вывод
- Подходит для локальной разработки

### streamable-http
- Работает через HTTP с Server-Sent Events
- Требует правильных заголовков
- Подходит для веб-приложений

## Примеры использования

### Базовый пример

```python
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    # Подключение к MCP серверу
    client = MultiServerMCPClient({
        "demo": {
            "command": "python",
            "args": ["mcp_server.py"],
            "transport": "stdio",
        }
    })
    
    # Получение инструментов
    tools = await client.get_tools()
    print(f"Доступно инструментов: {len(tools)}")

asyncio.run(main())
```

### Использование с LangGraph

```python
from langgraph.prebuilt import create_react_agent

# Создание агента с MCP инструментами
agent = create_react_agent(
    tools=tools,
    model=llm
)

# Вызов агента
result = agent.invoke({
    "messages": [{"role": "user", "content": "Сложи 5 и 3"}]
})
```

## Устранение неполадок

### Ошибка "Not Acceptable: Client must accept text/event-stream"
- **Причина**: Неправильная конфигурация HTTP транспорта
- **Решение**: Используйте stdio транспорт или добавьте правильные заголовки

### Ошибка "Expected dict, got string"
- **Причина**: Неправильный формат входных данных для агента
- **Решение**: Передавайте данные в формате `{"messages": [...]}`

### Ошибка подключения к серверу
- **Причина**: Сервер не запущен или неправильный URL
- **Решение**: Убедитесь, что сервер запущен и URL корректный

## Расширение функциональности

### Добавление нового инструмента

1. Добавьте функцию в `mcp_server.py`:

```python
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Умножить два числа."""
    return a * b
```

2. Перезапустите сервер

### Подключение к внешним API

```python
@mcp.tool()
def weather(city: str) -> str:
    """Получить погоду для города."""
    # Ваш код для API вызова
    return f"Погода в {city}: солнечно"
```

## Полезные ссылки

- [Официальная документация MCP](https://modelcontextprotocol.io/)
- [FastMCP документация](https://github.com/jlowin/fastmcp)
- [LangChain MCP адаптеры](https://github.com/langchain-ai/langchain-mcp-adapters)
- [Groq API документация](https://console.groq.com/docs)

## Лицензия

MIT License 