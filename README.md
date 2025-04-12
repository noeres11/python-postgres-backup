# PostgreSQL Automation Scripts in Python

Collection of Python scripts designed to automate routine PostgreSQL administration tasks.
Ideal for DBAs looking to streamline maintenance, backups, and monitoring.

## 📁 Scripts Included

---

### 1. `backup_database.py` – Automate database backups with `pg_dump`

Performs a PostgreSQL database backup using `pg_dump`, with timestamped output and support for connection arguments.

**Usage:**
```bash
export PGPASSWORD='your_password'
python3 backup_postgres.py --dbname mydb
```
What
**Optional arguments:**
- `--host` (default: `localhost`)
- `--port` (default: `5432`)
- `--user` (default: `postgres`)
- `--backup_dir` (default: `./backups`)

---

### 2. `expire_backups.py` – Delete Old Backups Based on Retention Policy

Removes `.sql` or `.dump` files older than N days from a specified directory.
Default directory is `/backups`.

**Usage:**
```bash
python3 expire_backups.py --dir ./backups --days 7
```

---

### 3. `check_replica_status.py` – Check PostgreSQL Replica Status

Connects to a PostgreSQL instance and checks if it's a standby. If so, it shows replication lag in bytes.

**Usage:**
```bash
python3 check_replica_status.py --host localhost --user postgres --dbname mydb
```

---

### 4. `detect_locks.py` – (Coming Soon)

Detects blocking queries using `pg_stat_activity` and `pg_locks`.

---

## Requirements

- Python 3
-  `psycopg2` module
- PostgreSQL v.17
- `PGPASSWORD` environment variable set.

---

## Development

Create a virtual environment to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install psycopg2-binary
```

---

## Directory Structure

```
python-postgres-automation/
├── backups/
├── backup_database.py
├── delete_old_backups.py
├── check_replica_status.py
├── detect_locks.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## License


