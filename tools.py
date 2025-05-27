# Global memory store
schema_memory = {}

def get_schema_details(table_description: str) -> str:
    """
    User provides table schema (table name and its columns).
    """
    schema_memory['schema'] = table_description
    return f"Schema stored: {table_description}"


def run_sql_query(query: str) -> str:
    from db import get_connection
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()

        rows = [dict(zip(columns, row)) for row in results]
        return f"Query result:\n{rows}"
    except Exception as e:
        return f"Error: {str(e)}"
