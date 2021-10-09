# Import postgres driver 
import psycopg2 as postgres
# Import queries list
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # Set connection string variables
    hostname = "127.0.0.1"
    database_name = "postgres"
    username = "postgres"
    password = "123456"
    
    # connect to default database
    connection = postgres.connect(
        "host={} dbname={} user={} password={}".format(
            hostname, database_name, username, password
        )
    )
    
    # Set auto-commit to Trues
    connection.set_session(autocommit=True)
    
    # Create a cursor
    cursor = connection.cursor()
    
    # create sparkify database with UTF8 encoding
    
    # > Drop the sparkifydb database if it already exists
    cursor.execute("DROP DATABASE IF EXISTS sparkifydb")
    # > Then recreate the database
    cursor.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    connection.close()    
    
    # Change database_name to Sparkify database
    database_name = "sparkifydb"
    
    # connect to sparkify database
    connection = postgres.connect(
        "host={} dbname={} user={} password={}".format(
            hostname, database_name, username, password
        )
    )
    
    # Create a new cursor
    cursor = connection.cursor()
    
    return cursor, connection


def drop_tables(cursor, connection):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cursor.execute(query)
        connection.commit()


def create_tables(cursor, connection):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cursor.execute(query)
        connection.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cursor, connection = create_database()
    
    drop_tables(cursor, connection)
    create_tables(cursor, connection)

    connection.close()


if __name__ == "__main__":
    main()