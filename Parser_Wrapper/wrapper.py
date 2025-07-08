# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from parser_dispatcher import handle_repo

app = FastAPI()

class RepoRequest(BaseModel):
    repos: List[dict]

@app.post("/parse")
async def parse_repositories(request: RepoRequest):
    all_results = []

    for repo in request.repos:
        repo_path = repo.get("repo_path")
        if repo_path:
            result = await handle_repo(repo_path)
            all_results.append({
                "repo_path": repo_path,
                "resources": result
            })

    return {"results": all_results}
