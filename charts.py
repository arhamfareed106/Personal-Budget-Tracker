import matplotlib.pyplot as plt
from db import get_records_by_month

def show_charts(month):
    records = get_records_by_month(month)
    if not records:
        print("No records found")
        return

    income = sum(r[2] for r in records if r[1] == "Income")
    expenses = sum(r[2] for r in records if r[1] == "Expense")

    categories = {}
    for r in records:
        if r[1] == "Expense":
            categories[r[3]] = categories.get(r[3], 0) + r[2]

    # Bar Chart
    plt.figure(figsize=(8,4))
    plt.bar(["Income", "Expense"], [income, expenses], color=["green", "red"])
    plt.title(f"Summary for {month}")
    plt.ylabel("Amount")
    plt.show()

    # Pie Chart
    if categories:
        plt.figure(figsize=(6,6))
        plt.pie(list(categories.values()), labels=list(categories.keys()), autopct="%1.1f%%")
        plt.title("Expenses by Category")
        plt.show()
