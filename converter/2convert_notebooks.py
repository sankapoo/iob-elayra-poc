import os
import tarfile
from pathlib import Path
from ipynb_py_convert import convert

def extract_repo_tar(input_file: str, extract_path: str = "."):
    print(f"📂 Extracting {input_file}...")
    with tarfile.open(input_file, "r:gz") as tar:
        tar.extractall(path=extract_path)
    print("✅ Extraction complete.")

def convert_all_notebooks(clone_dir: str):
    print("🔍 Searching for .ipynb files...")
    count = 0
    for ipynb_path in Path(clone_dir).rglob("*.ipynb"):
        ipynb_path = str(ipynb_path)
        py_path = ipynb_path.replace(".ipynb", ".py")
        print(f"🔁 Converting {ipynb_path} → {py_path}")
        convert(ipynb_path, py_path)
        count += 1
    print(f"✅ Converted {count} notebooks.")

def archive_repo_folder(clone_dir: str, output_file: str):
    print(f"📦 Updating archive {output_file}...")
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(clone_dir, arcname=os.path.basename(clone_dir))
    print(f"✅ Updated archive: {output_file}")

if __name__ == "__main__":
    INPUT_TAR = "repo.tar.gz"
    CLONE_DIR = "repo"

    extract_repo_tar(INPUT_TAR)
    convert_all_notebooks(CLONE_DIR)
    archive_repo_folder(CLONE_DIR, INPUT_TAR)  # reuse same tar name
