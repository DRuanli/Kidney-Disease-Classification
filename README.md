# 📌 Kidney-Disease-Deep-Learning-Classification


## Recycle Code Workflows

1. Update config.yaml: Change source_URL for future recycle.
2. Update secrets.yaml [Optional] so the user don't saw it
3. Update params.yaml
4. Update the src/entity (can work on notebook first than update to entity later)
5. Update the configuration manager in src/config
6. Update the src/components: model preparation(trainer, evaluation, ...)
7. Update the src/pipeline (training, prediction)
8. Update the main.py -> this is the **end point**
9. Update the dvc.yaml: tracking pipeline
10. Create user app at app.py

# 📁 Project Structure
```
├── template.py              # Setup directories
├── requirement.txt          # Packages list is required.
├── setup.py                 # Use the local packages automatically.
├── src/cnnClassifier/
    ├── __init__.py          # For import package
    ├── utils/               # Save the exception history that module facing.
        └── common.py        # Store common functions within project, for better reference lately.
    ├── entity/              # return type of function
    ├── templates/           # For web application builder
├── main.py                  # Run the module
├── logs/running_logs.log    # Save the running histories
├── research/                # Store experiment caught through testing notebook
└── 
```

# How to run?
### STEPS: Clone the repository

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
- **setup.py**: file to help automatically preparing local packages for folder.

- **__init__.py**: the Constructor file help you easily import these packages.

- **main.py**: file to run and test module. Note that "cnnClassifier" is set as local package in **setup.py**.

```code
from cnnClassifier import logger # instead of src.cnnClassifier
```

- **logs/running_logs.log**: After run history will save to this file.

- Add functions that you use recently in **common.py**

- Testing your module in **research** folder.

### STEP 05 - Exacting Data

We use Kidney dataset from kaggle, you can visit this link: [kaggle link](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone)

Because it the image dataset so it bring with huge capacity. So we will use *gdown* to download it from google drive.

1. Download the data from the kaggle
2. Upload the data to google drive, remember to set the status to accessible with whoever have the link
3. Build config: Modify the *config/config.yaml*: Change the source_URL for future recycle.

**Configuration vs Hardcode**

- The configuration version allows you to change database credential, switch between different API endpoints, value without modifying the code.

- Easily maintain system: can have different *config.yaml* files for development, testing, and production.

After done do *STEP 09 - Testing and Training*

### STEP 06 - Model Choosing
For image dataset, we tend to choose **VGG-16** cause of it primary purpose is image classification.

- **Characteristic**: a deep architecture, consisting of 16 layers with weights (convolutional and fully connected layers).

- **Training**: The original VGG-16 model was trained on the ImageNet dataset, a massive dataset of millions of labeled images. This pre-training allows the model to learn general-purpose image features.

- Layers:
    - Convolution layers:
        - Conv n-m: Convolutional Layers with the Filter Dimensions(kernel) e.g. Conv 1-1 is represented to a 1x1 convolution uses a filter that is 1 pixel wide and 1 pixel high.
        - Pooling: is used to reduce the spatial dimensions of the feature maps. This reduces the number of parameters and makes the network more robust to small variations in the input.
    - Activation Function: Softmax activation.
    - FC(Fully Connect) a.k.a Top layer =:
        - In python program parameter, it represent as Dense layer.
        - In FC layer, every neuron in the layer is connected to every neuron in the previous layer. This means that each neuron receives input from all neurons in the preceding layer. 
        - Perform the final classification or prediction based on the features extracted by earlier layers (e.g., convolutional layers in a CNN).
    
After done do *STEP 09 - Testing and Training*

### STEP 07 - Training Model
You can change class and epochs to see the model performance.

After done do *STEP 09 - Testing and Training*

### STEP 08 - Model Evaluation with MLflow

**What is MLflow?**
- 

After done do *STEP 09 - Testing and Training*

### STEP 09 - Testing and Training

After do testing at notebook in *research* folder, update it base on the *Recycle Code Workflows*. Then execute:

```base
python3 main.py # or python
```

### STEP 09 - 

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