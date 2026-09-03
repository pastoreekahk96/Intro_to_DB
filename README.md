# Intro to DB

A practical introduction to MySQL database design and Python database connectivity.

## What this repository covers

- Creating and selecting a MySQL database
- Designing tables and relationships
- Inspecting database metadata
- Inserting sample customer data
- Connecting to MySQL from Python

## Repository structure

| File | Purpose |
|---|---|
| `MySQLServer.py` | Creates the `alx_book_store` database through MySQL Connector/Python |
| `alx_book_store.sql` | Defines the main database schema |
| `task_2.sql` | Creates/works with the database schema as required by the coursework |
| `task_3.sql` | Lists database tables |
| `task_4.sql` | Inspects the `Books` table columns |
| `task_5.sql` | Inserts the first customer record |
| `task_6.sql` | Inserts additional customer records |

## Python setup

Create and activate a virtual environment, then install the dependency:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

## MySQL configuration

`MySQLServer.py` reads the connection settings from environment variables instead of storing a database password in the repository:

- `MYSQL_HOST` — defaults to `localhost`
- `MYSQL_USER` — defaults to `root`
- `MYSQL_PASSWORD` — required for authenticated MySQL connections

Example:

```bash
export MYSQL_HOST=localhost
export MYSQL_USER=root
export MYSQL_PASSWORD='your-local-password'
python MySQLServer.py
```

Never commit real database passwords or other credentials.

## Learning note

This repository preserves the original coursework progression while fixing clear correctness and security problems where necessary. The goal is to understand both SQL fundamentals and how application code safely connects to a database.
