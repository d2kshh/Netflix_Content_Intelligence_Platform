"""
====================================================================

Project : Netflix Content Intelligence Platform

Module  : Exploratory Data Analysis (EDA)

Author  : Daksh Patel

Description
-----------
This script demonstrates the process used to generate
visualizations from the Netflix dataset after SQL cleaning
and Python preprocessing.

The implementation shown below generates the Ratings
Distribution chart.

The same visualization workflow was reused for other
business charts throughout the project by changing only:

• SQL Query
• Chart Title
• X-axis
• Y-axis
• Output File Name

Generated Business Charts
-------------------------
• Movies vs TV Shows
• Ratings Distribution
• Release Year Trends
• Genre Distribution
• Country Analysis
• Director Analysis
• Actor Analysis
• Duration Analysis

====================================================================
"""

# ==========================================================
# Import Required Libraries
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os

# ==========================================================
# Step 1
# Connect to MySQL Database
# ==========================================================
#
# Establishes connection with the Netflix Analytics
# database to retrieve processed data.
#
# Replace YOUR_PASSWORD with your own MySQL password.
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
print("Exploratory Data Analysis Started")
print("=" * 60)

# ==========================================================
# Step 2
# Create Output Folder
# ==========================================================
#
# All generated charts are automatically saved
# inside the Images folder.
# ==========================================================

OUTPUT_FOLDER = "../09_Images"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==========================================================
# Step 3
# Retrieve Data from MySQL
# ==========================================================
#
# This SQL query calculates the number of Netflix
# titles available under each content rating.
#
# Example
#
# TV-MA
# TV-14
# PG
# R
#
# Similar SQL queries were written for all other
# business visualizations in this project.
# ==========================================================

query = """
SELECT
    rating,
    COUNT(*) AS total_titles
FROM clean_netflix_titles
WHERE rating IS NOT NULL
  AND rating <> ''
GROUP BY rating
ORDER BY total_titles DESC;
"""

df = pd.read_sql(query, engine)

print(df.head())

# ==========================================================
# Step 4
# Create Visualization
# ==========================================================
#
# A bar chart is generated to display the
# distribution of Netflix ratings.
#
# The same visualization workflow was reused
# throughout the project by changing only:
#
# • SQL Query
# • Chart Labels
# • Figure Title
# • Output File Name
# ==========================================================

plt.figure(figsize=(10,6))

plt.bar(
    df["rating"].astype(str),
    df["total_titles"]
)

plt.title("Netflix Ratings Distribution")

plt.xlabel("Rating")

plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()

# ==========================================================
# Step 5
# Save Chart
# ==========================================================
#
# Export the generated visualization as a
# high-quality PNG image.
# ==========================================================

plt.savefig(
    os.path.join(
        OUTPUT_FOLDER,
        "chart8_ratings.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# Step 6
# Validation
# ==========================================================
#
# Confirm successful chart generation.
# ==========================================================

print("=" * 60)
print("Visualization Generated Successfully")
print("=" * 60)

print("Chart Saved:")
print("✓ chart8_ratings.png")

# ==========================================================
# Reusability of the Visualization Workflow
# ==========================================================
#
# The same visualization workflow implemented
# above was reused for all business charts.
#
# Only the following components changed:
#
# • SQL Query
# • Chart Title
# • X-axis Label
# • Y-axis Label
# • Output Image Name
#
# Charts Created During the Project
# ---------------------------------
#
# Movies vs TV Shows
# Ratings Distribution
# Release Year Trends
# Genre Distribution
# Country Analysis
# Director Analysis
# Actor Analysis
# Movie Duration Analysis
#
# This ensured a consistent visualization
# pipeline throughout the project while
# minimizing duplicate code.
#
# ==========================================================