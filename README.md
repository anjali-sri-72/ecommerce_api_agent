# 🛒 E-commerce AI Agent

This project builds an **AI-powered agent** that answers natural language questions based on e-commerce sales data.  
It uses a **local SQLite database**, integrates with the **Gemini LLM** to generate SQL queries, and provides results through a **FastAPI backend**.

---

## 📂 Datasets Used

1. **Product-Level Ad Sales and Metrics**  
2. **Product-Level Total Sales and Metrics**  
3. **Product-Level Eligibility Table**

All CSVs are converted into a single SQLite database (`ecommerce.db`) for query purposes.

---

## 🚀 Features

- Accepts natural language questions (e.g., “What is my total sales?”)
- Converts to SQL using Gemini (Google Generative AI)
- Queries SQLite database and returns structured data
- Provides an API endpoint for external integration
- Bonus: Easily extendable for visual responses (charts)

---

## 📦 Technologies Used

- Python 🐍
- FastAPI ⚡
- SQLite 🗃️
- Pandas 📊
- Google Generative AI (Gemini) ✨

---

## 📁 Project Structure

ecommerce_ai_agent/
├── datasets/
│ ├── ad_sales.csv
│ ├── total_sales.csv
│ └── eligibility.csv
├── db_setup.py # Converts CSVs into SQLite tables
├── ecommerce.db # SQLite database (generated)
├── llm_utils.py # LLM logic using Gemini API
├── query_utils.py # SQL query runner
├── main.py # FastAPI app
├── README.md # You're reading this!
└── requirements.txt # Optional: to install dependencies



---

## 🧪 Example API Queries

POST to: `http://localhost:8000/ask`

```json
{
  "query": "What is my total sales?"
}



Response

{
  "query": "What is my total sales?",
  "sql": "SELECT SUM(total_sales) FROM total_sales;",
  "result": [
    {
      "SUM(total_sales)": 1589934.75
    }
  ]
}



