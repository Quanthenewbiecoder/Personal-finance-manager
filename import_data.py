import sqlite3
from datetime import datetime

# Define a function to convert datetime to ISO 8601 string format
def adapt_datetime(dt):
    return dt.isoformat()

# Register the adapter with SQLite
sqlite3.register_adapter(datetime, adapt_datetime)

# Connect to the SQLite database
conn = sqlite3.connect('finance_manager.db')
cursor = conn.cursor()

# Insert default categories
categories = ['Income', 'Expense', 'Savings']
for category in categories:
    cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', (category,))

# Insert fake users
users = [
    ('john_doe', 'john@example.com', 'hashed_password_1'),
    ('jane_smith', 'jane@example.com', 'hashed_password_2')
]
cursor.executemany('INSERT OR IGNORE INTO users (username, email, password_hash) VALUES (?, ?, ?)', users)

# Insert fake transactions
transactions = [
    ('Grocery shopping', 50.75, datetime.now(), 2, 1),  # (description, amount, date, category_id, user_id)
    ('Salary', 2000.00, datetime.now(), 1, 1),
    ('Coffee', 3.50, datetime.now(), 2, 2),
    ('Utilities', 120.00, datetime.now(), 2, 2)
]
cursor.executemany('INSERT INTO transactions (description, amount, date, category_id, user_id) VALUES (?, ?, ?, ?, ?)', transactions)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Sample data inserted into the database.")
