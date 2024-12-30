import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('finance_manager.db')
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.execute('DROP TABLE IF EXISTS transactions;')
cursor.execute('DROP TABLE IF EXISTS categories;')
cursor.execute('DROP TABLE IF EXISTS users;')

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Create the categories table
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

# Insert default categories
cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', ('Income',))
cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', ('Expense',))
cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', ('Savings',))

# Create the transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    category_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

# Create the daily_totals table
cursor.execute('''
CREATE TABLE IF NOT EXISTS daily_totals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    total_income REAL DEFAULT 0,
    total_expense REAL DEFAULT 0,
    total_savings REAL DEFAULT 0,
    net_total REAL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id),
    UNIQUE(user_id, date)  -- Ensure no duplicate entries for the same user and date
)
''')

# Function to update daily totals
def update_daily_totals(user_id, date):
    cursor.execute('''
    WITH daily_data AS (
        SELECT
            user_id,
            date(date) AS date_str,
            SUM(CASE WHEN c.name = 'Income' THEN amount ELSE 0 END) AS total_income,
            SUM(CASE WHEN c.name = 'Expense' THEN amount ELSE 0 END) AS total_expense,
            SUM(CASE WHEN c.name = 'Savings' THEN amount ELSE 0 END) AS total_savings
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE user_id = ? AND date(date) = ?
        GROUP BY user_id, date_str
    )
    INSERT INTO daily_totals (user_id, date, total_income, total_expense, total_savings, net_total)
    SELECT
        user_id,
        date_str,
        total_income,
        total_expense,
        total_savings,
        (total_income - total_expense) + total_savings AS net_total
    FROM daily_data
    ON CONFLICT(user_id, date) DO UPDATE SET
        total_income = excluded.total_income,
        total_expense = excluded.total_expense,
        total_savings = excluded.total_savings,
        net_total = excluded.net_total;
    ''', (user_id, date))

    conn.commit()

# Function to calculate total money
def calculate_total_money(user_id):
    cursor.execute('''
    SELECT
        SUM(total_income - total_expense) AS total_money,
        SUM(total_savings) AS total_savings
    FROM daily_totals
    WHERE user_id = ?;
    ''', (user_id,))

    result = cursor.fetchone()
    return result

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database setup completed successfully.")
