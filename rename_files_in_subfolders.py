
from pathlib import Path
from datetime import datetime

root_dir = Path('files')
file_paths = root_dir.glob("**/*")



for path in file_paths:
  if path.is_file():
    stat = path.stat()
    grab_ctime = stat.st_ctime
    timestamp = datetime.fromtimestamp(grab_ctime)
    date_created_str = timestamp.strftime("%Y-%m-%d_%H:%M:%S")
            
    new_filename = date_created_str + '_' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)