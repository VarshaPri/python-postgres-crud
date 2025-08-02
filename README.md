# Connecting PostgreSQL with Python using psycopg2

Hi! 👋  
This is a small project I created to understand how to connect a **PostgreSQL database** with a **Python program** using the `psycopg2` library.

---

## 🔍 What I Learned

In this project, I learned how to:

- Set up a connection between Python and PostgreSQL.
- Use a **cursor** to execute SQL queries from Python.
- **Create a table** inside PostgreSQL using Python code.
- **Insert data** into the table — both single and multiple records.
- **Update** data in the table.
- **Delete** specific records using SQL conditions.
- **Fetch and display** the data from the PostgreSQL table in Python.



## 🐍 File Description

- `python_sql.py` — This script contains all the operations: CREATE, INSERT, SELECT, UPDATE, DELETE, and also demonstrates how to use context managers for connections and cursors.

---

## ⚙️ How to Run This

1. Make sure you have PostgreSQL installed and running.
2. Install `psycopg2` if not already:

   ```bash
   pip install psycopg2
