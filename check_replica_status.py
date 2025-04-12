import psycopg2
import argparse
import getpass

def check_replica_status(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT pg_is_in_recovery();")
        in_recovery = cur.fetchone()[0]

        if not(in_recovery):
            print("This is not a standby server.")
            return

        cur.execute("SELECT pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn();")
        receive_lsn, replay_lsn = cur.fetchone()

        if receive_lsn is None or replay_lsn is None:
            print("Replication status not available.")
            return

        cur.execute("SELECT pg_wal_lsn_diff(%s, %s);", (receive_lsn, replay_lsn))
        lag_bytes = cur.fetchone()[0]

        if lag_bytes == 0:
            print("Replica is up to date.")
        else:
            print(f"Replica is delayed by {lag_bytes} bytes.")

def main():
    parser = argparse.ArgumentParser(description="Check PostgreSQL replica status")
    parser.add_argument("--host", required=True, help="Database host")
    parser.add_argument("--port", default=5432, type=int, help="Database port")
    parser.add_argument("--dbname", required=True, help="Database name")
    args = parser.parse_args()

    #password = getpass.getpass("Password: ")

    try:
        conn = psycopg2.connect(
            host=args.host,
            port=args.port,
            user=args.user,
            dbname=args.dbname
        )
        check_replica_status(conn)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()
