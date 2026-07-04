/*====================================================================

Project      : Netflix Content Intelligence Platform

Module       : Business Analysis Queries

Author       : Daksh Patel

Description
-------------
This script answers key business questions using SQL.

The generated results support:

• Executive Reporting
• Business Intelligence
• Power BI Dashboard
• Strategic Analysis

====================================================================*/

-- ==========================================
-- Business Question 1
-- What is the distribution of Movies vs TV Shows?
-- ==========================================

SELECT
    type,
    COUNT(*) AS total_titles,
    ROUND(COUNT(*) * 100.0 /
          (SELECT COUNT(*) FROM raw_netflix_titles),2) AS percentage
FROM raw_netflix_titles
GROUP BY type;


-- ==========================================
-- Business Question 2
-- Which content ratings dominate Netflix?
-- ==========================================

SELECT
    rating,
    COUNT(*) AS total_titles
FROM raw_netflix_titles
GROUP BY rating
ORDER BY total_titles DESC;

SELECT *
FROM raw_netflix_titles
WHERE rating IS NULL
   OR rating = '';
   
   -- ==========================================
-- Business Question 3
-- Which release years have the most Netflix titles?
-- ==========================================

   SELECT
    release_year,
    COUNT(*) AS total_titles
FROM raw_netflix_titles
GROUP BY release_year
ORDER BY total_titles DESC;

/* ============================================================
Business Question 4
Which directors have the highest number of titles on Netflix?
------------------------------------------------------------ */

SELECT
    director,
    COUNT(*) AS total_titles
FROM raw_netflix_titles
WHERE director IS NOT NULL
  AND director <> ''
GROUP BY director
ORDER BY total_titles DESC
LIMIT 10;

/* ============================================================
Business Question 5
How many titles were added to Netflix each year?
============================================================ */

SELECT
    YEAR(STR_TO_DATE(date_added,'%M %d, %Y')) AS year_added,
    COUNT(*) AS total_titles
FROM raw_netflix_titles
WHERE date_added IS NOT NULL
  AND date_added <> ''
GROUP BY year_added
ORDER BY year_added;

/* ============================================================
Business Question 6
Which ratings are most common for Movies and TV Shows?
============================================================ */

SELECT
    type,
    rating,
    COUNT(*) AS total_titles
FROM raw_netflix_titles
GROUP BY type, rating
ORDER BY type, total_titles DESC;


/* ============================================================
Business Question 7
Which actors appear in the highest number of Netflix titles?
============================================================ */

SELECT
    a.actor_name,
    COUNT(*) AS total_titles
FROM actors a
JOIN title_actor ta
ON a.actor_id = ta.actor_id
GROUP BY a.actor_name
ORDER BY total_titles DESC
LIMIT 10;

/* ============================================================
Business Question 8
Which genres are most common for Movies?
============================================================ */

SELECT
    g.genre_name,
    COUNT(*) AS total_movies
FROM genres g
JOIN title_genre tg
ON g.genre_id = tg.genre_id
JOIN clean_netflix_titles nt
ON tg.show_id = nt.show_id
WHERE nt.type = 'Movie'
GROUP BY g.genre_name
ORDER BY total_movies DESC
LIMIT 10;

/* ============================================================
Business Question 9
Which genres are most common for TV Shows?
============================================================ */

SELECT
    g.genre_name,
    COUNT(*) AS total_tvshows
FROM genres g
JOIN title_genre tg
ON g.genre_id = tg.genre_id
JOIN clean_netflix_titles nt
ON tg.show_id = nt.show_id
WHERE nt.type = 'TV Show'
GROUP BY g.genre_name
ORDER BY total_tvshows DESC
LIMIT 10;

/* ============================================================
Business Question 10
Which countries produce the most Movies?
============================================================ */

SELECT
    c.country_name,
    COUNT(*) AS total_movies
FROM countries c
JOIN title_country tc
ON c.country_id = tc.country_id
JOIN clean_netflix_titles nt
ON tc.show_id = nt.show_id
WHERE nt.type = 'Movie'
GROUP BY c.country_name
ORDER BY total_movies DESC
LIMIT 10;

/* ============================================================
Business Question 11
Which countries produce the most TV Shows?
============================================================ */

SELECT
    c.country_name,
    COUNT(*) AS total_tvshows
FROM countries c
JOIN title_country tc
ON c.country_id = tc.country_id
JOIN clean_netflix_titles nt
ON tc.show_id = nt.show_id
WHERE nt.type = 'TV Show'
GROUP BY c.country_name
ORDER BY total_tvshows DESC
LIMIT 10;

/* ============================================================
Business Question 12
Which release year produced the most Netflix content?
============================================================ */

SELECT
    release_year,
    COUNT(*) AS total_titles
FROM clean_netflix_titles
GROUP BY release_year
ORDER BY total_titles DESC
LIMIT 10;

/* ============================================================
Business Question 13
What is the average movie duration by genre?
============================================================ */

SELECT
    g.genre_name,
    ROUND(AVG(nt.duration_minutes),2) AS avg_duration
FROM genres g
JOIN title_genre tg
ON g.genre_id = tg.genre_id
JOIN clean_netflix_titles nt
ON tg.show_id = nt.show_id
WHERE nt.type='Movie'
GROUP BY g.genre_name
ORDER BY avg_duration DESC;

/* ============================================================
Business Question 14
Which directors have directed the most Movies?
============================================================ */

SELECT
    d.director_name,
    COUNT(*) AS total_movies
FROM directors d
JOIN title_director td
ON d.director_id = td.director_id
JOIN clean_netflix_titles nt
ON td.show_id = nt.show_id
WHERE nt.type='Movie'
GROUP BY d.director_name
ORDER BY total_movies DESC
LIMIT 10;