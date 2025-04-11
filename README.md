# PostgreSQL Backup Script

A simple Python script to automate backups of a PostgreSQL database using `pg_dump`.

## Requirements

- Python 3
- PostgreSQL client tools installed (`pg_dump` must be available in PATH)
- `PGPASSWORD` environment variable set with the user's password

## Usage

```bash
export PGPASSWORD='your_password'
python3 backup.py --user postgres --dbname mydb
