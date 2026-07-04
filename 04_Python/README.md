# Python Scripts

This folder contains the Python workflow used in the Netflix Content Intelligence Platform.

## Scripts

### 01_Import_To_MySQL.py
Imports the raw Netflix dataset into the MySQL database.

### 02_Data_Normalization.py
Demonstrates the normalization workflow used to transform multi-valued attributes into relational tables. The same process was reused for Actors, Directors, Countries, and Genres.

### 03_Exploratory_Data_Analysis.py
Generates business visualizations from the processed dataset. The same workflow was reused to create multiple charts used during exploratory analysis and dashboard development.

## Libraries

- pandas
- matplotlib
- sqlalchemy
- pymysql