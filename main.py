from fastapi import FastAPI
from pydantic import BaseModel
from llm_utils import get_sql_from_llm
from query_utils import run_sql_query

app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/ask")
def ask_agent(data: Question):
    sql = get_sql_from_llm(data.query)
    result = run_sql_query(sql)
    return {
        "query": data.query,
        "sql": sql,
        "result": result.to_dict(orient="records")
    }
