
import psycopg2
import os

DB_CONN_STR = os.environ.get('DATABASE_URL', 'dbname=cultia user=postgres password=Banven12199 host=localhost port=5345')

def make_admin(email):
    conn = psycopg2.connect(DB_CONN_STR)
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET role = 'admin' WHERE email = %s", (email,))
        conn.commit()
        print(f"User with email {email} is now an admin!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        make_admin(sys.argv[1])
    else:
        print("Usage: python make_admin.py <email>")
