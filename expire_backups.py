import os
import time
import argparse

#
# Deletes backup files older than the retention period from the specified directory.
#
# - backup_dir: Path to the directory containing the backup files.
# - retention_days: Number of days to keep backups. Older ones will be deleted.
#
def expire_backups(backup_dir, retention_days):
    
    now = time.time()
    cutoff = now - (retention_days * 86400)  # 86400 seconds = 1 day

    if not(os.path.exists(backup_dir)):
        print(f"Backup directory not found: {backup_dir}")
        return

    deleted_files = 0
    for filename in os.listdir(backup_dir):
        file_path = os.path.join(backup_dir, filename)
        if os.path.isfile(file_path) and filename.endswith(('.sql', '.dump')):
            file_mtime = os.path.getmtime(file_path)
            if file_mtime < cutoff:
                os.remove(file_path)
                print(f"Backup deleted: {file_path}")
                deleted_files += 1

    print(f"Deletion completed. Total deleted files: {deleted_files}")


# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete old PostgreSQL backups.")
    parser.add_argument("--dir", required=True, help="Directory where backups are stored.")
    parser.add_argument("--days", type=int, default=7, help="Retention period in days.")
    args = parser.parse_args()
    
    expire_backups(args.dir, args.days)
    
