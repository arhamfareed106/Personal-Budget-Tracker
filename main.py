import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from db import init_db, add_record, get_records_by_month
from charts import show_charts
from utils import export_to_csv
from datetime import datetime

# Initialize DB
init_db()

# --- GUI ---
root = tk.Tk()
root.title("Personal Budget Tracker")
root.geometry("700x600")

# Input Frame
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

tk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
tk.Label(frame, text="Type:").grid(row=1, column=0)
tk.Label(frame, text="Amount:").grid(row=2, column=0)
tk.Label(frame, text="Category:").grid(row=3, column=0)

entry_date = tk.Entry(frame)
entry_date.insert(0, datetime.today().strftime('%Y-%m-%d'))
entry_type = ttk.Combobox(frame, values=["Income", "Expense"])
entry_amount = tk.Entry(frame)
entry_category = tk.Entry(frame)

entry_date.grid(row=0, column=1)
entry_type.grid(row=1, column=1)
entry_amount.grid(row=2, column=1)
entry_category.grid(row=3, column=1)

def submit():
    try:
        date = entry_date.get()
        rtype = entry_type.get()
        amount = float(entry_amount.get())
        category = entry_category.get()
        add_record(date, rtype, amount, category)
        messagebox.showinfo("Success", "Record added!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

btn_add = ttk.Button(frame, text="Add Record", command=submit)
btn_add.grid(row=4, column=1, pady=10)

# Filter by Month
def load_data():
    tree.delete(*tree.get_children())
    month = month_entry.get()
    records = get_records_by_month(month)
    for r in records:
        tree.insert("", "end", values=r)

ttk.Label(root, text="Enter Month (YYYY-MM):").pack()
month_entry = ttk.Entry(root)
month_entry.pack()
ttk.Button(root, text="Load Records", command=load_data).pack(pady=5)

# Treeview for Display
tree = ttk.Treeview(root, columns=("Date", "Type", "Amount", "Category"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
tree.pack(expand=True, fill="both", pady=10)

# Bottom Buttons
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Show Charts", command=lambda: show_charts(month_entry.get())).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Export CSV", command=lambda: export_to_csv(month_entry.get())).pack(side="left", padx=5)

root.mainloop()
