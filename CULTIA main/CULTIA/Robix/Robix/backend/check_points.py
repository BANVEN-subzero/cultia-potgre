
import os
import psycopg2

os.environ['DATABASE_URL'] = 'dbname=cultia user=postgres password=Banven12199 host=localhost port=5345'
DB_CONN_STR = os.environ['DATABASE_URL']

conn = psycopg2.connect(DB_CONN_STR)
cursor = conn.cursor()

print("=== Current Point Transactions ===")
cursor.execute('''
    SELECT pt.id, u.first_name, u.last_name, 
           pt.transaction_type, pt.reference_id, pt.points_change, 
           pt.description, pt.created_at
    FROM point_transactions pt
    JOIN users u ON pt.user_id = u.id
    ORDER BY pt.created_at DESC
''')
rows = cursor.fetchall()

for row in rows:
    print(f"[ID: {row[0]}] {row[1]} {row[2]} | Type: {row[3]} | Ref: {row[4]} | Change: {row[5]} | Desc: {row[6]} | Time: {row[7]}")

print("\n=== Summary by User ===")
cursor.execute('''
    SELECT u.id, u.first_name, u.last_name, 
           SUM(pt.points_change) as total_points,
           COUNT(pt.id) as total_transactions
    FROM users u
    LEFT JOIN point_transactions pt ON u.id = pt.user_id
    GROUP BY u.id
    ORDER BY total_points DESC
''')
users = cursor.fetchall()
for u in users:
    print(f"User {u[1]} {u[2]} (ID: {u[0]}) | Total Points: {u[3] or 0} | Transactions: {u[4]}")

cursor.close()
conn.close()
