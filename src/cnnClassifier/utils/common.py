"""
This module provides a collection of utility functions designed to streamline common tasks within a project.
It includes functions for file operations (YAML, JSON, binary), directory management, data serialization, image encoding/decoding, and logging.
The functions are type-hinted and use runtime type checking through the "@ensure_annotations" decorator.

Functions:
1. read_yaml(path) -> ConfigBox:
    Reads YAML, returns ConfigBox object, allowing attribute-style access to the data. Handles empty YAML files and logs successful loading.
2. create_directories(paths, verbose=True):
    Creates a list of directories. Logs(note history) the creation of each directory if verbose is True.
3. save_json(path, data):
    Saves JSON file with proper indentation.
4. load_json(path) -> ConfigBox:
    Loads JSON, returns ConfigBox object.
5. save_bin(data, path):
    Saves any Python object as a binary file using joblib.
6. load_bin(path) -> Any:
    Loads a binary file using joblib and returns the loaded object.
7. get_size(path) -> str:
    Gets the size of a file in kilobytes (KB).
8. decodeImage(imgString, fileName):
    Decodes a base64 encoded image string and saves it to a file.
9. encodeImageIntoBase64(path) -> bytes:
    Encodes an image file into a base64 encoded byte string.

For the 2-6. function, logs(note history) the successful loading of the file.

Key Features:
- File I/O (YAML, JSON, binary).
- Directory creation.
- Data serialization.
- Image base64 handling.
- Logging.
- Type validation.

Usage:
- Import and use the functions as needed within project. The "@ensure_annotations" decorator will enforce type hints, and the logging will provide valuable information during execution.
"""
import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations # This helps catch type-related bugs early.
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file content and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) -> None:
    """
    Create list of directories for modifying file(create, remove, move, ... file).
    Using for validation it.

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to  False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB

    Args:
        path (Path): path of the file
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgString, fileName) -> None:
    """
    Decodes a base64 encoded image string and saves it to a file.
    Use in predicted Pipeline and User app.

    Args:
        imgString (str): The base64 encoded image string.
        fileName (Path): The path to the file where the decoded image will be saved.
    """
    imgData = base64.b64decode(imgString)
    with open(fileName, "wb") as f:
        f.write(imgData)
        f.close()

def encodeImageIntoBase64(croppedImagePath) -> None:
    """
    Encodes an image file into a base64 encoded byte string.
    Use in predicted Pipeline and User app.

    Args:
        croppedImagePath (Path): The path to the image file to be encoded.

    Returns:
        bytes: The base64 encoded image data as a byte string.
    """
    # Opens the file in binary read mode ("rb").
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())