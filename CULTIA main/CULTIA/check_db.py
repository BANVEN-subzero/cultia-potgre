
import psycopg2

def test_connection():
    try:
        # Connect to default postgres DB first to check if cultia exists
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='Banven12199',
            host='localhost',
            port=5345
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        # Check if cultia database exists
        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'cultia'")
        exists = cur.fetchone()
        
        if not exists:
            print("Creating cultia database...")
            cur.execute("CREATE DATABASE cultia")
            print("cultia database created!")
        else:
            print("cultia database already exists!")
        
        cur.close()
        conn.close()
        
        # Now connect to cultia database
        print("\nConnecting to cultia database...")
        conn2 = psycopg2.connect(
            dbname='cultia',
            user='postgres',
            password='Banven12199',
            host='localhost',
            port=5345
        )
        print("Successfully connected to cultia database!")
        conn2.close()
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_connection()
