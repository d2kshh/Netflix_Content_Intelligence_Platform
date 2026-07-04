/*====================================================================

Project      : Netflix Content Intelligence Platform

Module       : Database Setup

Author       : Daksh Patel

Description
-------------
This script creates the project database and the raw table used to
store the original Netflix dataset before data cleaning,
transformation, and analysis.

====================================================================*/

CREATE DATABASE netflix_analytics;

USE netflix_analytics;

/*==============================================================
Create Raw Dataset Table
==============================================================*/

CREATE TABLE raw_netflix_titles (

    show_id VARCHAR(20),

    type VARCHAR(20),

    title VARCHAR(300),

    director TEXT,

    cast TEXT,

    country TEXT,

    date_added VARCHAR(50),

    release_year INT,

    rating VARCHAR(20),

    duration VARCHAR(30),

    listed_in TEXT,

    description TEXT

);

/*==============================================================
Validation Queries
==============================================================*/

SELECT COUNT(*) AS total_rows
FROM raw_netflix_titles;

/*==============================================================
Utility Commands
(Execute only when required)
==============================================================*/

TRUNCATE TABLE raw_netflix_titles;

DROP TABLE raw_netflix_titles;