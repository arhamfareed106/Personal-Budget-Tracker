import sqlite3

def init_db():
    conn = sqlite3.connect("budget.db", factory=sqlite3.Connection)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY,
            date TEXT,
            type TEXT,
            amount REAL,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_record(date, rtype, amount, category):
    conn = sqlite3.connect("budget.db")
    c = conn.cursor()
    c.execute("INSERT INTO budget (date, type, amount, category) VALUES (?, ?, ?, ?)", 
              (date, rtype, amount, category))
    conn.commit()
    conn.close()

def get_records_by_month(month):
    conn = sqlite3.connect("budget.db")
    c = conn.cursor()
    c.execute("SELECT date, type, amount, category FROM budget WHERE substr(date, 1, 7) = ?", (month,))
    rows = c.fetchall()
    conn.close()
    return rows

# --- Usage ---

# Step 1: Initialize the database
init_db()

# Step 2: Insert sample data
add_record("2025-07-10", "Income", 35000.00, "Salary")
add_record("2025-07-11", "Expense", 1200.00, "Transport")
add_record("2025-07-12", "Expense", 2000.00, "Groceries")
add_record("2025-07-13", "Income", 5000.00, "Freelance")
add_record("2025-07-14", "Expense", 8500.00, "Rent")

# Step 3: Print records for July 2025 to verify
records = get_records_by_month("2025-07")
for r in records:
    print(r)
