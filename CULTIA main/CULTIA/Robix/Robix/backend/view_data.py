
import psycopg2
import os
import threading

db_lock = threading.Lock()  # Thread lock to prevent database locking issues

DB_CONN_STR = os.environ.get('DATABASE_URL', 'dbname=cultia user=postgres password=Banven12199 host=localhost port=5345')

def view_users():
    """View all users in the database"""
    try:
        with db_lock:
            conn = psycopg2.connect(DB_CONN_STR)
            cursor = conn.cursor()
            
            # Get column names
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'users' ORDER BY ordinal_position")
            columns = [info[0] for info in cursor.fetchall()]
            
            # Get all users
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            
            print("\n" + "="*80)
            print("DATABASE CONTENTS - USERS TABLE")
            print("="*80)
            
            # Print column headers
            header = " | ".join(f"{col:>12}" for col in columns)
            print(header)
            print("-" * len(header))
            
            # Print user data
            for user in users:
                row = " | ".join(f"{str(val):>12}" for val in user)
                print(row)
                
            print("="*80)
            print(f"Total users: {len(users)}")
            conn.close()
        
    except Exception as e:
        print(f"Error accessing database: {e}")

if __name__ == "__main__":
    view_users()
