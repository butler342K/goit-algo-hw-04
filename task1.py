
from pathlib import Path
import shutil

def sort_files_by_extension(src, dst):
    src_path = Path(src)
    dst_path = Path(dst)
    if not dst_path.exists():
        dst_path.mkdir(parents=True)

    for path in src_path.iterdir():
        if path.is_dir():
            sort_files_by_extension(path, dst_path)
        else:
            ext = path.suffix[1:] if path.suffix else 'no_extension'
            ext_dir = dst_path / ext
            if not ext_dir.exists():
                ext_dir.mkdir()
            dest_file = ext_dir / path.name
            counter = 1
            #Якщо файл з таким ім'ям вже існує, додаємо суфікс _1, _2 і т.д.
            while dest_file.exists():
                dest_file = ext_dir / f"{path.stem}_{counter}{path.suffix}"
                counter += 1
            shutil.copy(path, dest_file)
    return

if len(sys.argv) < 2:
    print("Path_to_directory is not provided.")
    sys.exit(1)
elif len(sys.argv) < 3:
    src = sys.argv[1]
    dst = 'dist'
else:
    src, dst = sys.argv[1], sys.argv[2]

src_path = Path(src)
if not src_path.is_dir():
    print(f"The path {src} is not a valid directory.")
    sys.exit(1)
if dst == None:
    dst = 'dist'

sort_files_by_extension(src, dst)