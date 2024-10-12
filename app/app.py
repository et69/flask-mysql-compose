from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Get MySQL connection details from environment variables
db_host = os.getenv("MYSQL_HOST")
db_user = os.getenv("MYSQL_USER")
db_password = os.getenv("MYSQL_PASSWORD")
db_database = os.getenv("MYSQL_DATABASE")

# Connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if the visits table exists, create it if not
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS visits (
        count INT NOT NULL
    )
    """)
    conn.commit()

    # Check if there is an entry, initialize if not
    cursor.execute("SELECT count FROM visits")
    row = cursor.fetchone()

    if row is None:
        cursor.execute("INSERT INTO visits (count) VALUES (1)")
        conn.commit()
        visit_count = 1
    else:
        visit_count = row[0] + 1
        cursor.execute("UPDATE visits SET count = %s", (visit_count,))
        conn.commit()

    cursor.close()
    conn.close()

    return f"Hello, World! This page has been visited {visit_count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

