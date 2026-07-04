"""
Netflix Content Intelligence Platform

Module:
Import Raw Dataset to MySQL

Author:
Daksh Patel

Description:
Reads the raw Netflix CSV dataset and imports it into
the MySQL database for further preprocessing.

"""

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# ==========================
# 1. Read CSV
# ==========================
csv_path = "../02_Dataset/Raw/netflix_titles.csv"

df = pd.read_csv(csv_path)

print("=" * 50)
print("CSV Loaded Successfully")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")
print("=" * 50)

# ==========================
# 2. MySQL Connection
# ==========================
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="YOUR_PASSWORD",      # <-- Your MySQL password
    host="localhost",
    port=3306,
    database="netflix_analytics"
)

engine = create_engine(connection_url)

# ==========================
# 3. Upload to MySQL
# ==========================
df.to_sql(
    name="raw_netflix_titles",
    con=engine,
    if_exists="replace",
    index=False
)

# ==========================
# 4. Verify
# ==========================
print("✅ Data imported successfully into MySQL!")
print("Table Name : raw_netflix_titles")
print(f"Total Rows : {len(df)}")