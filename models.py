# models.py
from pydantic import BaseModel
from pydantic_ai import Tool

# Tool input schemas
class GetSchemaDetailsInput(BaseModel):
    table_description: str

class RunSQLQueryInput(BaseModel):
    query: str

# Tool functions
from tools import get_schema_details, run_sql_query

tools = [
    Tool.from_function(
        name="get_schema_details",
        description="User provides table schema (name and columns)",
        func=get_schema_details,
        input_model=GetSchemaDetailsInput
    ),
    Tool.from_function(
        name="run_sql_query",
        description="Executes a SQL query provided by the user",
        func=run_sql_query,
        input_model=RunSQLQueryInput
    )
]
