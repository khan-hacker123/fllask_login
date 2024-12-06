import sqlite3
import os

# Get the absolute path to ensure SQLite can access the database file
base_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
db_path = os.path.join(base_dir, 'database.db')  # Construct absolute path to database

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table to store user details
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
