/*====================================================================

Project      : Netflix Content Intelligence Platform

Module       : Data Cleaning

Author       : Daksh Patel

Description
-------------
This script performs initial data cleaning and preprocessing
on the raw Netflix dataset before normalization and dashboard
development.

Cleaning Tasks

• Missing Value Analysis

• Data Validation

• Text Standardization

• Date Conversion

• Duration Transformation

====================================================================*/

/* ============================================================
Step 1

Create a cleaned copy of the raw table.

============================================================ */

CREATE TABLE clean_netflix_titles AS
SELECT *
FROM raw_netflix_titles;

SELECT COUNT(*)
FROM clean_netflix_titles;

/* ============================================================
Step 2

Check missing values in every important column.

============================================================ */

SELECT
    SUM(show_id IS NULL OR show_id = '') AS show_id_missing,
    SUM(type IS NULL OR type = '') AS type_missing,
    SUM(title IS NULL OR title = '') AS title_missing,
    SUM(director IS NULL OR director = '') AS director_missing,
    SUM(cast IS NULL OR cast = '') AS cast_missing,
    SUM(country IS NULL OR country = '') AS country_missing,
    SUM(date_added IS NULL OR date_added = '') AS date_added_missing,
    SUM(rating IS NULL OR rating = '') AS rating_missing,
    SUM(duration IS NULL OR duration = '') AS duration_missing,
    SUM(listed_in IS NULL OR listed_in = '') AS listed_in_missing
FROM clean_netflix_titles;

/* ============================================================
Step 3

Investigate missing date_added values.

============================================================ */

SELECT *
FROM clean_netflix_titles
WHERE date_added IS NULL
   OR date_added = '';
   
   /* ============================================================
Step 4

Investigate missing ratings.

============================================================ */

SELECT *
FROM clean_netflix_titles
WHERE rating IS NULL
   OR rating = '';
   
   /* ============================================================
Step 5

Remove leading and trailing spaces.

============================================================ */
SET SQL_SAFE_UPDATES = 0;
UPDATE clean_netflix_titles
SET
    type = TRIM(type),
    title = TRIM(title),
    director = TRIM(director),
    cast = TRIM(cast),
    country = TRIM(country),
    rating = TRIM(rating),
    duration = TRIM(duration),
    listed_in = TRIM(listed_in);
    
    SELECT ROW_COUNT();
    
    SELECT COUNT(*)
FROM clean_netflix_titles;

/* ============================================================
Step 6

Convert date_added to DATE datatype.

============================================================ */

ALTER TABLE clean_netflix_titles
ADD COLUMN date_added_new DATE;

/* ============================================================
Step 7

Populate the new DATE column.

============================================================ */

UPDATE clean_netflix_titles
SET date_added_new = STR_TO_DATE(date_added, '%M %d, %Y')
WHERE date_added IS NOT NULL
  AND date_added <> '';
  
  SELECT
    date_added,
    date_added_new
FROM clean_netflix_titles
LIMIT 10;

/* ============================================================
Step 8

Separate movie duration and TV show seasons.

============================================================ */

ALTER TABLE clean_netflix_titles
ADD COLUMN duration_minutes INT,
ADD COLUMN seasons INT;

UPDATE clean_netflix_titles
SET
    duration_minutes = CASE
        WHEN type = 'Movie'
        THEN CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED)
        ELSE NULL
    END,
    seasons = CASE
        WHEN type = 'TV Show'
        THEN CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED)
        ELSE NULL
    END;
    
/*==============================================================
  Validation
  Verify duration transformation.
==============================================================*/

    SELECT
    type,
    duration,
    duration_minutes,
    seasons
FROM clean_netflix_titles
LIMIT 10;

/*==============================================================
Final Validation

Verify the cleaned dataset before exporting
for Python preprocessing and Power BI analysis.

==============================================================*/

SELECT COUNT(*) AS total_records
FROM clean_netflix_titles;

DESCRIBE clean_netflix_titles;