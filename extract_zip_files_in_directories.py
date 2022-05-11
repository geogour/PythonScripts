from pathlib import Path
import zipfile

root_dir = Path('.')
destination = Path('destination')

for path in root_dir.glob("*.zip"):
  with zipfile.ZipFile(path, 'r') as zf:
    final_path = destination / Path(path.stem)
    zf.extractall(path=final_path)