import os
import subprocess
import tarfile


def clone_git_repo(repo_url: str, clone_dir: str, branch: str = "main"):
    print(f"📥 Cloning repo {repo_url} into {clone_dir}")
    subprocess.run(["git", "clone", "--branch", branch, repo_url, clone_dir], check=True)


def archive_repo_folder(clone_dir: str, output_file: str):
    print(f"📦 Creating archive {output_file} from {clone_dir}/")
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(clone_dir, arcname=os.path.basename(clone_dir))
    print(f"✅ Archive created: {output_file}")


if __name__ == "__main__":
    # Get environment variables passed from Elyra pipeline
    GIT_REPO = os.environ["GIT_REPO"]
    GIT_BRANCH = os.environ.get("GIT_BRANCH", "main")

    # Define local clone dir and output archive name
    CLONE_DIR = "repo"
    OUTPUT_TAR = "repo.tar.gz"

    # Step 1: Clone repo
    clone_git_repo(GIT_REPO, CLONE_DIR, GIT_BRANCH)

    # Step 2: Create tar.gz archive as Elyra output
    archive_repo_folder(CLONE_DIR, OUTPUT_TAR)
