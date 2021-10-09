######################## DROP TABLES Queries ###########################

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

######################### CREATE TABLES Queries #########################
 
# >>> Create The Fact Table <<<

# Songplays Table

# PostgreSQL has a special kind of database object generator called SERIAL. 
# It is used to generate a sequence of integers which are often used as the 
# Primary key of a table.
# SERIAL: storage size = 4 bytes, Range = 1 to 2, 147, 483, 647
# The timestamp datatype allows you to store both date and time. 
# However, it does not have any time zone data.
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMP,
        user_id INTEGER,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INTEGER,
        location VARCHAR,
        user_agent VARCHAR
    );
""")

# >>> Create Dimension Tables <<<

# Users Table

# In Postgres, CHAR(1) → where n is a positive integer.
# n → defines the length of the string. 
# The length is fixed and indicates the number of characters 
# declared when a table is created.
users_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        gender CHAR(1),
        level VARCHAR    
    );
""")

# Songs Table

songs_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR,
        artist_id VARCHAR,
        year INTEGER,
        duration DECIMAL    
    );
""")

# Artists Table

# Difference between INT and DECIMAL: 
# If you need numbers with decimals, use decimal (or numeric). 
# if you need numbers without decimals, use integer or bigint. 
# A typical use of decimal as a column type would be a "product price" 
# column or an "interest rate". A typical use of an integer type would 
# be e.g. a column that stores how many products were ordered 
# (assuming you can't order "half" a product).

artists_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY,
        name VARCHAR,
        location VARCHAR,
        latitude DECIMAL,
        longitude DECIMAL    
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INTEGER,
        day INTEGER,
        week INTEGER,
        month INTEGER,
        year INTEGER,
        weekday INTEGER    
    );
""")

############################ INSERT RECORDS Queries #########################

songplay_table_insert = ""

users_table_insert = ""

songs_table_insert = ""

artists_table_insert = ""

time_table_insert = ""

############################# FIND SONGS Query ###########################

songs_select = ""

############################ QUERY LISTS ###########################

create_table_queries = [songplay_table_create, users_table_create, 
                        songs_table_create, artists_table_create, 
                        time_table_create]

drop_table_queries = [songplay_table_drop, users_table_drop, songs_table_drop,
                      artists_table_drop, time_table_drop]