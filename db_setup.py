
import pandas as pd
import sqlite3

conn = sqlite3.connect("ecommerce.db")

ad_sales = pd.read_csv("datasets/ad_sales.csv")
total_sales = pd.read_csv("datasets/total_sales.csv")
eligibility = pd.read_csv("datasets/eligibility.csv")

ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)
eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)

conn.close()
