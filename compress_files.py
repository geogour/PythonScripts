from pathlib import Path
from zipfile import ZipFile

root_dir = Path('files')

with ZipFile('files.zip','w') as zip:
        # writing each file one by one
        for file in root_dir.rglob("*.txt"):
          zip.write(file)
  
    
print('All files zipped successfully!') 
