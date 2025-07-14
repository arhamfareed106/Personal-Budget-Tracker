# 💸 Personal Budget Tracker (Tkinter + SQLite)

A desktop GUI application to track your income and expenses, view monthly summaries, generate charts, and export data — all with a user-friendly interface built using **Python and Tkinter**.

---

## 🎯 Features

- 📆 **Record daily income and expenses**
- 📂 Filter transactions by **month (YYYY-MM)**
- 📊 View monthly summary charts (bar/pie)
- 💾 Export records to **CSV file**
- 🗃️ Local data storage using **SQLite**
- 🧩 Modular structure (`db.py`, `charts.py`, `utils.py`) for maintainability

---

## 🖼️ GUI Preview

> *(Add a screenshot as `screenshot.png` for better presentation)*

---

## 🧱 Tech Stack

| Component    | Library         |
|--------------|------------------|
| GUI          | `tkinter`, `ttk` |
| Database     | `sqlite3`        |
| Charts       | `matplotlib`     |
| File Export  | `csv`, `tkinter.filedialog` |

---

## 📁 Folder Structure

```bash
personal_budget_tracker/
├── main.py           # Main GUI application
├── db.py             # SQLite database logic
├── charts.py         # Monthly pie/bar chart display
├── utils.py          # CSV export and utility functions
├── budget.db         # (auto-created) SQLite database
└── README.md         # Project documentation
