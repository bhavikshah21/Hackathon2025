# parser_dispatcher.py
import os
import aiohttp
from utils import detect_language

PARSER_ENDPOINTS = {
    "python": "http://localhost:8001/pythonParser",
    "java": "http://localhost:8002/javaParser",
    "csharp": "http://localhost:8003/csharpParser",
    "generic": "http://localhost:8004/genericParser"
}

async def handle_repo(repo_path: str):
    language = detect_language(repo_path)

    parser_url = PARSER_ENDPOINTS.get(language, PARSER_ENDPOINTS["generic"])

    async with aiohttp.ClientSession() as session:
        async with session.post(parser_url, json={"repo_path": repo_path}) as resp:
            return await resp.json()
