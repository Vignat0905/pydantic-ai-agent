from dotenv import load_dotenv
import os
from pydantic_ai import Agent
from tools import get_schema_details, run_sql_query

load_dotenv()

agent = Agent(
    model='google-gla:gemini-1.5-flash',
    system_prompt='You are a helpful assistant.' \
    'which will ask the user for a table schema and then execute SQL queries on a MySQL database.',
    tools=[get_schema_details, run_sql_query]
)

def ask_agent(user_prompt: str) -> str:
    try:
        result = agent.run_sync(user_prompt)
        return result.output
    except Exception as e:
        return f"Error during agent execution: {str(e)}"

