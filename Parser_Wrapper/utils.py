# utils.py
import os

def detect_language(repo_path: str) -> str:
    extensions = {
        ".py": "python",
        ".java": "java",
        ".cs": "csharp"
    }

    for root, _, files in os.walk(repo_path):
        for file in files:
            ext = os.path.splitext(file)[-1]
            if ext in extensions:
                return extensions[ext]

    return "generic"
