from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connector import GitConnector
import uvicorn

app = FastAPI()

class CloneRequest(BaseModel):
    repo_url: str
    provider: str  # github / gitlab / bitbucket
    token: str | None = None

@app.post("/clone-repo")
def clone_repo(request: CloneRequest):
    try:
        connector = GitConnector(
            provider=request.provider,
            repo_url=request.repo_url,
            token=request.token
        )
        result = connector.clone()
        return {"message": f"Repository {result['status']}", "path": result["path"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8010,reload=True)
