import os
from pathlib import Path

package_name = "legal_ai_project"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/data_processing.py",
    f"src/{package_name}/summarization.py",
    f"src/{package_name}/embeddings.py",
    f"src/{package_name}/chatbot.py",
    f"src/{package_name}/api.py",
    f"src/{package_name}/ui.py",
    "models/.gitkeep",
    "data/.gitkeep",
    "requirements.txt",
    "run.py",
    "README.md",
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File already exists: {filepath}")
