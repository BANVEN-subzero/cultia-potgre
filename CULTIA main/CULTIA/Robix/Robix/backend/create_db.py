
import psycopg2
from psycopg2 import OperationalError
import os

# Connect to the default 'postgres' database to create our cultia database
DB_CONN_STR_TEMPLATE = "dbname=postgres user=postgres password={} host=localhost port=5345"

def create_database(password):
    try:
        conn = psycopg2.connect(DB_CONN_STR_TEMPLATE.format(password))
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("CREATE DATABASE cultia")
        print("✓ Database 'cultia' created successfully!")
        cur.close()
        conn.close()
    except OperationalError as e:
        print(f"Error: Could not connect to PostgreSQL server. Check your password. Details: {e}")
    except psycopg2.errors.DuplicateDatabase:
        print("ℹ️ Database 'cultia' already exists!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import getpass
    password = getpass.getpass("Enter PostgreSQL password for 'postgres' user: ")
    create_database(password)
