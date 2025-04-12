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
def backup_database(host, port, user, dbname, backup_dir):

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
    

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create logical backups for a PostgreSQL database using pg_dump.")
    parser.add_argument("--host", default="localhost", help="Hostname or IP address.")
    parser.add_argument("--port", default=5432, type=int, help="Port number.")
    parser.add_argument("--user", default="postgres", help="PostgreSQL user to perform the backup.")
    parser.add_argument("--dbname", required=True, help="Database name to back up.")
    parser.add_argument("--backup_dir", default="./backups", help="Target directory to save the backup. Default: backups/")
    args = parser.parse_args()
    
    backup_database(args.host, args.port, args.user, args.dbname, args.backup_dir)
    
