import os
from git import Repo

class GitConnector:
    def __init__(self, provider, repo_url, token=None):
        self.provider = provider.lower()
        self.repo_url = self._prepare_url(repo_url, token)
        self.repo_name = self._extract_repo_name(repo_url)
        self.dest_dir = f"./cloned_repos/{self.repo_name}"

    def _prepare_url(self, repo_url, token):
        if token:
            repo_url = repo_url.replace("https://", f"https://{token}@")
        return repo_url

    def _extract_repo_name(self, repo_url):
        return repo_url.rstrip("/").split("/")[-1].replace(".git", "")

    def clone(self):
        if os.path.exists(self.dest_dir):
            return {"status": "already exists", "path": self.dest_dir}
        os.makedirs("cloned_repos", exist_ok=True)
        Repo.clone_from(self.repo_url, self.dest_dir)
        return {"status": "cloned", "path": self.dest_dir}
