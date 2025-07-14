import sqlite3
import random
from datetime import datetime, timedelta

# Categories
income_categories = ["Salary", "Freelance", "Bonus", "Gift"]
expense_categories = ["Groceries", "Rent", "Utilities", "Dining", "Transport", "Entertainment"]

def random_date(month_year="2025-07"):
    base = datetime.strptime(month_year + "-01", "%Y-%m-%d")
    day = random.randint(1, 28)
    return (base + timedelta(days=day-1)).strftime("%Y-%m-%d")

def generate_data(n=50, month_year="2025-07"):
    conn = sqlite3.connect("budget.db")
    c = conn.cursor()
    
    for _ in range(n):
        date = random_date(month_year)
        rtype = random.choice(["Income", "Expense"])
        if rtype == "Income":
            amount = round(random.uniform(5000, 50000), 2)
            category = random.choice(income_categories)
        else:
            amount = round(random.uniform(500, 8000), 2)
            category = random.choice(expense_categories)
        
        c.execute("INSERT INTO budget (date, type, amount, category) VALUES (?, ?, ?, ?)",
                  (date, rtype, amount, category))
    
    conn.commit()
    conn.close()
    print(f"{n} random records inserted for {month_year}.")

# Generate 50 entries for July 2025
generate_data(50, "2025-07")
