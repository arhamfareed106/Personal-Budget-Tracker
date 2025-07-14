import csv
from db import get_records_by_month
from tkinter import filedialog

def export_to_csv(month):
    records = get_records_by_month(month)
    if not records:
        print("No records to export.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                             filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Type", "Amount", "Category"])
        writer.writerows(records)
