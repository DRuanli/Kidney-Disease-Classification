import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",  
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir = file_path.parent  
    file_name = file_path.name

    # Create directory if it does not exist (skip if file is in the current directory)
    if file_dir != Path('.'):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory {file_dir} for the file: {file_name}")

    # Check if file doesn't exist or is empty;
    if (not file_path.exists()) or (file_path.stat().st_size == 0):
        with open(file_path, "w") as f: 
            pass
        logging.info(f"Creating empty file: {file_path}")
    else: 
        logging.info(f"{file_name} already exists")
