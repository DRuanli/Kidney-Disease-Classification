# 📌 Kidney-Disease-Deep-Learning-Classification



# 📁 Project Structure
```
├── template.py               # Setup directories
├── requirement.txt           # Packages list is required.
├── setup.py                  # Use the local packages automatically.
├── src/
    ├── cnnClassifier/
        ├── __init__.py       # For import package
        ├── templates/        # For web application builder
        ├── 
    └── common.py
├── main.py                   # Run the module
├── logs/running_logs.log     # Save the running histories
├── research/                 # Store the testing notebook
├── utils/                    # Save the exception history that module facing.
    └── common.py             # Store common functions within project, for better reference lately.
└── 
```

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/DRuanli/Kidney-Disease-Classification/tree/meg
```
### STEP 01 - Create and activate a conda environment after opening the repository

Always create a new virtual environment for each project.

**Why not "python -m venv cnncls"?**

Because this bash support python file only, while we want consistent environments across different platforms. So conda is highly recommend, it more powerful but also more complex -> no pain no gain.

**Create new anaconda environment**

Replace "kidney" and "3.8"(highly recommend) as needed; "-n" for new environment; "-y" for auto yes answer

```bash
conda create -n cnncls python=3.8 -y
```

**Activate the virtual environment**

```base
conda activate cnncls
```

### STEP 02 - Project structure creation
Starting from zero, we need to make structure for the project for easily maintaining. You can modify in "template.py" file. Then executed:

```bash
python3 template.py # or python
```

You can add new folder(or structure) after executed: if folders have code inside, it won't be replaced just ignore it and create the new one from the list.

### STEP 03 - Install the requirements
After running successfully, "requirement.txt", which is a list of package along with its version that need for the project, is added.

1. So modifying the "requirement.txt".

2. Install packages from "-r" a requirements file.

```bash
pip install -r requirements.txt
```

or

```bash
conda install --file requirements.txt
```

### STEP 04 - Project Workflow Files Setup
**setup.py**: file to help automatically preparing local packages for folder.

**__init__.py**: the Constructor file help you easily import these packages.

**main.py**: file to run and test module. Note that "cnnClassifier" is set as local package in **setup.py**.

```code
from cnnClassifier import logger # instead of src.cnnClassifier
```

**logs/running_logs.log**: After run history will save to this file.



### STEP 05 - Project Setup

### STEP 00 - End the virtual environment
After the project is completed

**Listing all conda environments**

```base
conda env list
```

**Remove the conda virtual environment**

Can use this command line to remove:

```base
conda env remove -n cnncls
```

Alternatively, you can remove by path:

```base
# Replace with your path to the environment
conda env remove -p /opt/anaconda3/envs/cnncls
```

**Deactivate all virtual environments for sure**

```base
conda deactivate
```