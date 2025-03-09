"""
This script initializes a project structure by creating a predefined list of directories and files. 
It's designed to automate the setup of a (new machine learning) project, specifically for a CNN classifier
Can be adapted for other projects by modifying the project_name and list_of_files variables.

Key Features:
- Project Structure Initialization: Creates essential directories and files for a project: including source code directories, configuration files, and utility scripts.
- Cross-Platform Compatibility: Uses pathlib.Path to ensure compatibility across different operating systems.
- Logging: Provides informative logging messages to track the progress of directory and file creation.
- Idempotency: Checks if directories and files already exist before creating them, preventing errors and ensuring that the script can be run multiple times without unintended side effects.
- Configurable Project Name: The project_name variable allows for easy customization of the project structure.

Variables:
- project_name: A string representing the name of the project. This is used to create project-specific directories within the src directory.
- list_of_files: A list of strings representing the paths to the directories and files that should be created.

Workflow:
1. Logging Setup: Configures basic logging to display informative messages during script execution.
2. Project Name Definition: Sets the project_name variable, which determines the name of the project's source code directory.
3. File List Definition: Defines the list_of_files variable, which specifies the directories and files to be created.
4. Directory and File Creation:
- Iterates through each filepath in the list_of_files.
- Splits the filepath into filedir (directory) and filename.
- Creates the filedir if it doesn't exist using os.makedirs(filedir, exist_ok=True).
- Creates an empty file at the filepath if it doesn't exist or is empty using open(filepath, "w").
- Logs messages to indicate the creation of directories and files, or if they already exist.
5. Pathlib conversion: Converts the string filepath to a pathlib object for cross platform compatability.

Usage:
1. Customize Project Name: Modify the project_name variable to match your project's name.
2. Adjust File List: Update the list_of_files variable to include the directories and files required for your project.
3. Run the Script: Execute the script.
"""
import os
from pathlib import Path
import logging

# Logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')\

# Change for different project
project_name = 'cnnClassifier'

list_of_files = [
    # give path to be more robotic
    ".github/workflow/.gitkeep",
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
    "requirements.txt", # for package info need
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html" # Use to create web application
    
    # add more file can be written here
    # ...
]

# Check for the creation list of files for sure
# make sure every operating system work fine with it
for filepath in list_of_files:
    # check for our os then convert path to the os
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")

