import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_avg_years_of_schooling(connection, country: str, start_date: int, end_date: int) -> list:
    """Retrieves the average years of schooling in a given country between the start and end dates

    Args:
        connection (psycopg2.connection) - the connection to the database
        country (str) - the country of interest
        start_date (int) - the earliest date to retrieve
        end_date (int) - the latest date to retrieve

    Returns:
        list - a list of average years of schooling for the country between the start and end date
    """
    try:
        cursor = connection.cursor()
        query = "SELECT entity, avg_years_of_schooling FROM literacy_rates_vs_avg_years_of_schooling WHERE date_year>=%s AND date_year<=%s AND entity=%s ORDER BY date_year DESC;"
        cursor.execute(query, (start_date, end_date, country,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def get_countries_literacy_rate(connection, temp: str) -> list:
    """Retrieves literacy data points (and all the literacy information associated with that country) 

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (str) - the country of interest

    Returns:
        list - a list of all literacy information from the country
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM literacy_rates_vs_avg_years_of_schooling WHERE entity=%s ORDER BY date_year DESC;"
        cursor.execute(query, (temp,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_max_temp_over_threshold(connection, 50)
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()