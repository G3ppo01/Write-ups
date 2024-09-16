import sqlite3
import sys
import csv

def db_connect(): #imports DB file and connects to it
    """
    Connects to an SQLite database file from the command-line argument.

    Returns:
    conn (sqlite3.Connection): Database connection object.
    cursor (sqlite3.Cursor): Cursor object for executing queries.
    If connection fails, returns None, None.
    """
    try:
        db_file = sys.argv[-1] # import db file
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        print("Connected to the database: "+ db_file)
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error connecting to database: "+ e)
        return None, None

def exec_query(cursor, query):
    """
    Execute a SQL query on the database and return results.
    
    Parameters:
    cursor: SQLite cursor object.
    query (str): SQL query to execute.
    
    Returns:
    result: The result of the query.
    """ 
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print("Error executing query: " + str(e))
        return None
    
def write_to_csv(cursor, result, output_file):
     """
    Writes the result data to a CSV file and automatically extracts header names from the cursor.

    Parameters:
    cursor (sqlite3.Cursor): The SQLite cursor from which to extract column names.
    result (list of tuples): Data returned from the SQL query.
    output_file (str): The name of the CSV file to write the data to.
    """
     # Get the column names from the cursor description
     header = [description[0] for description in cursor.description]
     # Open the output file in write mode
     with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header to the CSV file
        writer.writerow(header)
        
        # Write the result data (rows) to the CSV file
        writer.writerows(result)
    
     print("Data successfully written to "+ output_file)

def main():
    conn, cursor = db_connect()
    query = "SELECT t_customer.gender AS gender, SUBSTR(t_customer.lastname, 1, 2) || '--------' AS lastname, SUBSTR(t_customer.birthdate, 7, 4) AS birthdate, SUBSTR(t_location.zip, 1, 2) || '00' AS zip, t_customer_status.status AS status FROM t_customer JOIN t_location ON t_customer.fk_location = t_location.pk_location JOIN t_customer_status ON t_customer.fk_customer_status = t_customer_status.pk_customer_status;" #Input query here
    result = exec_query(cursor, query)
    write_to_csv(cursor, result, 'anonymized.csv')

    conn.close()
    print("Connection to " + str(sys.argv[-1]) + " closed.")
if __name__ == "__main__":
    main()
