import sqlite3
import pandas as pd

def run_sql_query(query):
    conn = sqlite3.connect("ecommerce.db")
    try:
        return pd.read_sql_query(query, conn)
    except Exception as e:
        return pd.DataFrame({ "error": [str(e)] })
