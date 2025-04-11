#!/usr/bin/env python3

import subprocess
import os
from pathlib import Path
from datetime import datetime
import argparse

#
# Takes a logical backup of the database given by the user using pg_dump
# to the "backups" directory. A custom target directory may be specified.
# If it doesn't exist, it will be created,
#
# - host: hostname or IP address of the PostgreSQL server.
# - port: The port number on which PostgreSQL is listening.
# - user: The PostgreSQL user to perform the backup. The user must have
#   the necessary permissions.
# - dbname: The name of the database to back up.
# - backup_dir: The directory where the backup file will be saved.
#
def backup(host, port, user, dbname, backup_dir):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{dbname}_{timestamp}.sql"
    filepath = Path(backup_dir) / filename

    os.makedirs(backup_dir, exist_ok=True)

    try:
        print(f"→ Starting backup of '{dbname}' in {filepath}")
        command = [
            "pg_dump",
            "-h", host,
            "-p", str(port),
            "-U", user,
            "-d", dbname,
            "-f", str(filepath)
        ]
        env = os.environ.copy()
        env["PGPASSWORD"] = os.getenv("PGPASSWORD", "")

        subprocess.run(command, env=env, check=True)
        print("Backup succesfull.")
    except subprocess.CalledProcessError as e:
        print("Backup failed:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatic Logical Backups for PostgreSQL using pg_dump.")
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", default=5432, type=int)
    parser.add_argument("--user", required=True)
    parser.add_argument("--dbname", required=True)
    parser.add_argument("--backup_dir", default="./backups")

    args = parser.parse_args()

    backup(args.host, args.port, args.user, args.dbname, args.backup_dir)

