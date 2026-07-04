"""
====================================================================

Project : Netflix Content Intelligence Platform

Module  : Data Normalization

Author  : Daksh Patel

Description
-----------
This script demonstrates the normalization process used to convert
multi-valued attributes into a relational database structure.

The implementation shown below normalizes the Actor (Cast) column.

The same normalization workflow was also applied during this project
for the following attributes:

• Director
• Country
• Listed_In (Genres)

Only the source column and destination table names were changed,
while the normalization logic remained the same.

Purpose
-------
1. Split comma-separated actor names.
2. Remove duplicate actor records.
3. Generate unique Actor IDs.
4. Create the Actors Dimension Table.
5. Create the Title_Actor Bridge Table.
6. Upload both tables into MySQL.

====================================================================
"""

# ==========================================================
# Import Required Libraries
# ==========================================================

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# ==========================================================
# Step 1
# Connect to MySQL Database
# ==========================================================
#
# Establishes a connection with the Netflix Analytics
# database using SQLAlchemy.
#
# Update YOUR_PASSWORD with your local MySQL password
# before executing the script.
# ==========================================================

connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="YOUR_PASSWORD",
    host="localhost",
    port=3306,
    database="netflix_analytics"
)

engine = create_engine(connection_url)

print("=" * 60)
print("Netflix Content Intelligence Platform")
print("Actor Normalization Started")
print("=" * 60)

# ==========================================================
# Step 2
# Read Required Data
# ==========================================================
#
# Only two columns are required:
#
# • show_id
# • cast
#
# show_id is used to maintain relationships.
# cast contains comma-separated actor names.
# ==========================================================

df = pd.read_sql(
    "SELECT show_id, cast FROM clean_netflix_titles",
    engine
)

print(f"Dataset Loaded Successfully")
print(f"Rows : {len(df)}")

# ==========================================================
# Step 3
# Split the Cast Column
# ==========================================================
#
# Each row may contain multiple actor names separated
# by commas.
#
# Example
#
# Before
# ------------------------------------
# Tom Hanks, Tim Allen
#
# After
# ------------------------------------
# Tom Hanks
# Tim Allen
#
# This process converts one cell into multiple records,
# making the data suitable for normalization.
# ==========================================================

rows = []

for _, row in df.iterrows():

    if pd.isna(row["cast"]):
        continue

    actors = [a.strip() for a in row["cast"].split(",")]

    for actor in actors:

        rows.append({

            "show_id": row["show_id"],

            "actor_name": actor

        })

actor_df = pd.DataFrame(rows)

print(f"Total Actor Records : {len(actor_df)}")
print(f"Unique Actors       : {actor_df['actor_name'].nunique()}")

print(actor_df.head(20))

# ==========================================================
# Step 4
# Create Actors Dimension Table
# ==========================================================
#
# Duplicate actor names are removed.
#
# A unique Actor ID is generated for every actor.
#
# Example
#
# actor_id    actor_name
# -------------------------
# 1           Tom Hanks
# 2           Shah Rukh Khan
# 3           Leonardo DiCaprio
#
# This table stores each actor only once.
# ==========================================================

actors = (
    actor_df[["actor_name"]]
    .drop_duplicates()
    .reset_index(drop=True)
)

actors.insert(0, "actor_id", range(1, len(actors) + 1))

# ==========================================================
# Step 5
# Create Title_Actor Bridge Table
# ==========================================================
#
# The bridge table creates a many-to-many relationship
# between Netflix titles and actors.
#
# Example
#
# show_id      actor_id
# ----------------------
# s1           25
# s1           43
# s2           18
#
# This allows one movie to have multiple actors and one
# actor to appear in multiple movies.
# ==========================================================

title_actor = actor_df.merge(
    actors,
    on="actor_name",
    how="left"
)[["show_id", "actor_id"]]

# ==========================================================
# Step 6
# Upload Tables to MySQL
# ==========================================================
#
# Two normalized tables are created.
#
# 1. actors
# 2. title_actor
#
# Existing tables are replaced if they already exist.
# ==========================================================

actors.to_sql(
    "actors",
    con=engine,
    if_exists="replace",
    index=False
)

title_actor.to_sql(
    "title_actor",
    con=engine,
    if_exists="replace",
    index=False
)

# ==========================================================
# Step 7
# Validation
# ==========================================================
#
# Display the total number of records created after
# normalization.
# ==========================================================

print("=" * 60)
print("Normalization Completed Successfully")
print("=" * 60)

print(f"Actors Table Records      : {len(actors)}")
print(f"Title_Actor Relationships : {len(title_actor)}")

print("\nNormalized Tables Created")
print("-------------------------")
print("✓ actors")
print("✓ title_actor")

# ==========================================================
# Reusability of the Normalization Process
# ==========================================================
#
# The same normalization workflow implemented above was
# reused for the following multi-valued attributes:
#
# Source Column        Dimension Table      Bridge Table
# ----------------------------------------------------------
# director        ->   directors       ->   title_director
# country         ->   countries       ->   title_country
# listed_in       ->   genres          ->   title_genre
# cast            ->   actors          ->   title_actor
#
# Only the source column name and destination table names
# were changed.
#
# The normalization logic remained exactly the same,
# ensuring a consistent ETL process across all entities.
#
# ==========================================================