import os
import time
from pathlib import Path

# Folder containing videos
video_folder = Path(r"C:\Users\syed abdullah\Downloads\Workspace II\january\recordings")

# Number of days
days_old = 30

# Video file extensions
extensions = {".mp4", ".mkv", ".avi", ".mov", ".wmv"}

# Cutoff time (in seconds since epoch)
cutoff_time = time.time() - (days_old * 24 * 60 * 60)

# Traverse directory recursively
for file_path in video_folder.rglob("*"):
    if file_path.is_file() and file_path.suffix.lower() in extensions:
        if file_path.stat().st_mtime < cutoff_time:
            file_path.unlink()
