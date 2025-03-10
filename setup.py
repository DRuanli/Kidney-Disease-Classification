"""
This setup.py file is the core configuration script for packaging and distributing a Python project named cnnClassification.
It leverages the setuptools library to define project "metadata", specify source code locations, and enable installation via pip.

Key Features:
- Metadata: Defines package name, version, author, and description.
- README.md Integration: Uses README.md for the long description.
- Source Location: Specifies src directory as the source.
- Automatic Package Discovery: Uses find_packages to include all modules.
- Editable Install: Supports "pip install -e ." for development.
- Repository and Bug Tracker URLs: Provides links to GitHub.

Variables:
- long_description: Content from README.md.
- __version__: Package version.
- REPO_NAME: GitHub repository name.
- AUTHOR_USER_NAME: GitHub username.
- SRC_REPO: Package name.
- AUTHOR_EMAIL: Author's email.
- package_dir: Source code location.
- packages: List of packages.

Workflow:
1. Reads README.md for package description.
2. Defines package metadata variables.
3. Calls setuptools.setup() to configure the package.
4. Enables building and installing via "python setup.py" and "pip install".

Usage:
1. Customize Metadata:
- Replace the placeholder values for AUTHOR_USER_NAME, AUTHOR_EMAIL, and REPO_NAME with your actual information.
- Update the __version__ variable as needed.
2. Create README.md:
- Write a comprehensive README.md file that describes your package.
3. Build and Install:
- To build source and wheel distributions: python setup.py sdist bdist_wheel
- To install the package in development mode: pip install -e .
- To upload to pypi twine upload dist/*
4. Distribute:
- Upload the generated distribution files (located in the dist directory) to PyPI or other package repositories.
"""
import setuptools

# Use for maintaining
# see in "r" read mode then print all concept
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Deep-Learning-Classification-MLflow-DVC"
AUTHOR_USER_NAME = "8greenhallo" # Modify with your github username
SRC_REPO = "cnnClassification"
AUTHOR_EMAIL = "vungoctamy@gmail.com" # Modify with your gmail

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)