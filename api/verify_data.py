import sqlite3
import pandas as pd

conn = sqlite3.connect('../database/database.db')

def query_table(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    print(f"Data in {table_name}:")
    print(df)
    print("\n")

query_table('events')
query_table('companies')
query_table('people')

conn.close()
