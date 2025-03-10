# Kidney-Disease-Deep-Learning-Classification



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/DRuanli/Kidney-Disease-Classification/tree/meg
```
### STEP 01 - Create a conda environment after opening the repository

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

### STEP 02 - Install the requirements
Install packages from "-r" a requirements file.

```bash
pip install -r requirements.txt
```

or

```bash
conda install --file requirements.txt
```
