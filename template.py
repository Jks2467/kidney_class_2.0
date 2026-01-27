import os
from pathlib import Path # For handling file paths robustly
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init__.py",
    f"src/{project_name}/components/_init__.py",
    f"src/{project_name}/utils/_init__.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init_.py",
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constants/_init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


# Loop through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create directory if it does not exist
    if filedir !="":
        os.makedirs (filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Create empty file if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f" {filename} is already exists")