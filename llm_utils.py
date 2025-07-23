import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY") 

model = genai.GenerativeModel("gemini-pro")

def ask_llm(prompt):
    response = model.generate_content(prompt)
    return response.text

def get_sql_from_llm(question):
    prompt = f"""
You are a SQL expert. Translate this user question to a SQLite SQL query using these tables:
- ad_sales
- total_sales
- eligibility

Question: \"{question}\"

Just give the SQL query. No explanation.
"""
    return ask_llm(prompt)
