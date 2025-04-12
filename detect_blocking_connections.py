import psycopg2
import argparse
import getpass

def detect_blocking_connections(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT
                blocking.pid AS blocking_pid,
                blocking.query AS blocking_query,
                blocked.pid AS blocked_pid,
                blocked.query AS blocked_query,
                age(now()::timestamp(0), blocking.query_start::timestamp(0)) AS blocking_duration,
                age(now()::timestamp(0), blocked.query_start::timestamp(0)) AS blocked_duration
            FROM
                pg_locks blocked_locks
                JOIN pg_stat_activity blocked ON blocked_locks.pid = blocked.pid
                JOIN pg_locks blocking_locks ON blocking_locks.locktype = blocked_locks.locktype
                    AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
                    AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
                    AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
                    AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
                    AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
                    AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
                    AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
                    AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
                    AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
                    AND blocking_locks.pid != blocked_locks.pid
                JOIN pg_stat_activity blocking ON blocking_locks.pid = blocking.pid
            WHERE NOT blocked_locks.granted
            ORDER BY blocking_pid;
        """)
        
        results = cur.fetchall()
        
        if not(results):
            print("No blocking queries found.")
        else:
            for row in results:
                print(f"Blocking PID:\t\t{row[0]}")
                print(f"Blocking Query:\t\t{row[1]}")
                print(f"Blocking duration:\t{row[5]}")
                print(f"Blocked PID:\t\t{row[2]}")
                print(f"Blocked Query:\t\t{row[3]}")
                print(f"Blocked duration:\t{row[4]}")
                print("-" * 60)


# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect PostgreSQL blocking sessions")
    parser.add_argument("--host", default="localhost", help="Hostname or IP address.")
    parser.add_argument("--port", default=5432, type=int, help="Port number.")
    parser.add_argument("--user", default="postgres", help="PostgreSQL user.")
    args = parser.parse_args()
    
    try:
        conn = psycopg2.connect(
            host = args.host,
            port = args.port,
            user = args.user
        )
        detect_blocking_connections(conn);
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    
    