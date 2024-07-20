import pandas as pd
import sqlite3

def load_csv_to_sqlite(csv_file, table_name, conn):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

conn = sqlite3.connect('./../database/database.db')

load_csv_to_sqlite('data/events.csv', 'events', conn)
load_csv_to_sqlite('data/companies.csv', 'companies', conn)
load_csv_to_sqlite('data/people.csv', 'people', conn)

conn.close()
