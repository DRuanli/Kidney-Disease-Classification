# Use the library to ensure it can handle window issue
from pathlib import Path

# Uses the pathlib module in Python to define file paths for configuration and parameters files in a more object-oriented and platform-independent way. 
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")