# seed.py — Database Setup & Seeding

## Purpose
`seed.py` initializes the backend environment for the ALX ProDev Generator project. It sets up the MySQL database, creates the required table, and inserts sample user data from a CSV file.

## ⚙️ What It Does
- Connects to the MySQL server
- Creates `ALX_prodev` database if it doesn't exist
- Creates `user_data` table with fields:
  - `user_id` (UUID, Primary Key)
  - `name` (VARCHAR, Not Null)
  - `email` (VARCHAR, Not Null)
  - `age` (DECIMAL, Not Null)
- Loads data from `user_data.csv` and inserts into the table using `INSERT IGNORE`

## 🐍 Functions

| Function              | Description                                       |
|-----------------------|---------------------------------------------------|
| `connect_db()`        | Connects to the MySQL server (without database)   |
| `create_database()`   | Creates `ALX_prodev` if it doesn’t exist          |
| `connect_to_prodev()` | Connects to the `ALX_prodev` database             |
| `create_table()`      | Creates `user_data` table with required schema    |
| `insert_data()`       | Seeds the table from a CSV file                   |

## 📁 Requirements
- Python 3.x
- MySQL running locally
- `user_data.csv` file in the same directory

## Usage
```bash
python3 seed.py
