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
            raw_data = await resp.json()

    # 🔧 Enrich the result based on application/repo
    enriched_data = enrich_response(raw_data, repo_path)
    return enriched_data


# enrich.py
def enrich_response(data: dict, repo_path: str) -> dict:
    app_name = repo_path.split("/")[-1].lower()  

    # Example enrichment rules
    app_metadata = {
        "App1": {"team": "Credit", "tech_stack": ["Python", "Kafka"], "app_category": "Finance", "dept": "NCL"},
        "orders-api": {"team": "Commerce", "tech_stack": ["Java", "Spring"], "app_category": "Technical", "dept": "NCL"},
        "risk-core": {"team": "RiskTech", "tech_stack": ["C#", "SQL"], "app_category": "Risk", "dept": "NCL"}
    }

    metadata = app_metadata.get(app_name, {
        "team": "Unknown",
        "tech_stack": [],
        "app_category": "General",
        "dept":""
    })

    # Add the new fields to top-level JSON
    data["repo_path"] = repo_path
    data["application_name"] = app_name
    data["team"] = metadata["team"]
    data["tech_stack"] = metadata["tech_stack"]
    data["app_category"] = metadata["app_category"]
    data["department"] = metadata["dept"]

    return data

