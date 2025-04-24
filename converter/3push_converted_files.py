import os
import subprocess
import tarfile


def extract_repo_tar(input_file: str, extract_path: str = "."):
    print(f"📂 Extracting {input_file}...")
    with tarfile.open(input_file, "r:gz") as tar:
        tar.extractall(path=extract_path)
    print("✅ Extraction complete.")


def push_to_git(clone_dir: str, commit_message: str):
    print("📤 Committing and pushing to Git...")
    subprocess.run(["git", "config", "--global", "user.email", "elyra@pipeline.com"], check=True)
    subprocess.run(["git", "config", "--global", "user.name", "elyra-bot"], check=True)
    subprocess.run(["git", "add", "."], cwd=clone_dir, check=True)

    try:
        subprocess.run(["git", "commit", "-m", commit_message], cwd=clone_dir)
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stderr.decode("utf-8") if e.stderr else "":
            print("✅ Nothing to commit. Repo is already up-to-date.")
        else:
            raise

    # Set git remote again (just in case)
    subprocess.run(["git", "remote", "set-url", "origin", os.environ["GIT_REPO"]], cwd=clone_dir)
    try:
        subprocess.run(["git", "push"], cwd=clone_dir)
        print("🚀 Git push complete.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git push failed: {e}")
        raise
    print("🚀 Git push complete.")


if __name__ == "__main__":
    INPUT_TAR = "repo.tar.gz"
    CLONE_DIR = "repo"

    extract_repo_tar(INPUT_TAR)
    push_to_git(CLONE_DIR, commit_message="✨ Convert .ipynb to .py via Elyra pipeline")
