from pathlib import Path

def read_tree(path):
    '''Read all files from src folder and return list of their paths'''
    src_path = Path(path)
    if not src_path.is_dir():
        if not src_path.exists():
            raise FileNotFoundError(f"The path {path} does not exist.")
        else:
            entry_dir_name = src_path.name
    return [str(file) for file in src_path.rglob('*') if file.is_file()]

def main():
    ''''Parse input 2 arguments src, dst folders'''
    import argparse
if __name__ == "__main__":
    main()