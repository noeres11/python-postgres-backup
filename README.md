# PostgreSQL Automation Scripts in Python

Collection of Python scripts designed to automate routine PostgreSQL administration tasks.
Ideal for DBAs looking to streamline maintenance, backups, and monitoring.

## 📁 Scripts Included

---

### 1. `backup_postgres.py` – Automated Backups with `pg_dump`

Performs a PostgreSQL database backup using `pg_dump`, with timestamped output and support for connection arguments.

**Usage:**
```bash
export PGPASSWORD='your_password'
python3 backup_postgres.py --user postgres --dbname mydb
```
What
**Optional arguments:**
- `--host` (default: `localhost`)
- `--port` (default: `5432`)
- `--out`  (default: `./backups`)

---

### 2. `delete_old_backups.py` – Delete Old Backups Based on Retention Policy

Removes `.sql` or `.dump` files older than N days from a specified directory.
Default directory is `/backups`.

**Usage:**
```bash
python3 rotate_backups.py --dir ./backups --days 7
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
- `psycopg2-binary`
- PostgreSQL client tools (`pg_dump`)
- `PGPASSWORD` environment variable set.

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Development

Create a virtual environment to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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

## 📄 License

MIT
