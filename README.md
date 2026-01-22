# 💰 Personal Finance Dashboard (Streamlit + Google Sheets)

A personal finance tracking application built with Python and **Streamlit**. It allows you to import bank statements, categorize expenses, and visualize spending habits using **Google Sheets** as a cloud database.

The app supports CSV imports from Polish banks (ING, mBank) and offers an interactive dashboard for analyzing data.

---

## 🚀 Key Features

### 1. 📥 Data Import & Processing
* **Bank Statement Parsing:** Custom parsers for **ING** and **mBank** CSV files.
* **Auto-Cleaning:** Automatically handles currency formatting (removing "PLN", fixing decimal separators) and date formats.
* **Duplicate Prevention:** Checks existing data before appending new transactions.

### 2. 📊 Analytics & Visualization (Altair)
* **Expenses Over Time:** Interactive bar chart showing monthly spending. Clicking a bar filters the transaction details below.
* **Category Analysis:** Breakdown of expenses by category. Clickable charts to drill down into specific spending areas.
* **Filters:** Filter by date range, bank source, and categories.

### 3. 📝 Data Management (CRUD)
* **Live Editor:** Edit transaction details (Category, Description, Amount) directly in the browser.
* **Cloud Sync:** "Save changes" button securely updates the Google Sheet without overwriting hidden data (preserves data outside the current filter view).
* **Admin Panel:** Tools to view raw data, delete specific rows by ID, and re-index the entire database (sort by date and reset IDs).

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
* **Database:** Google Sheets (via `gspread` & Google Drive API)
* **Visualization:** [Altair](https://altair-viz.github.io/)

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

```bash
pip install streamlit pandas gspread google-auth altair python-dateutil
