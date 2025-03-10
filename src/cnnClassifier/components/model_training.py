import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from pathlib import Path
from src.cnnClassifier.entity.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        """
        Modified to address compatibility issues when loading the model
        by using a custom solution to manually load model structure.
        """
        try:
            # Attempt to load the model directly as a first option
            self.model = tf.keras.models.load_model(
                self.config.updated_base_model_path
            )
            print("Loaded model successfully")
        except Exception as e:
            print(f"Could not load model directly: {str(e)}")
            print("Creating a new model with the same architecture...")
            
            # Create a VGG16 base model with default parameters
            base_model = tf.keras.applications.vgg16.VGG16(
                input_shape=self.config.params_image_size,
                weights='imagenet',  # Default from params.yaml
                include_top=False    # Default from params.yaml
            )
            
            # Freeze all layers of the base model
            for layer in base_model.layers:
                layer.trainable = False
            
            # Add classification head (2 classes for kidney classification)
            flatten_in = tf.keras.layers.Flatten()(base_model.output)
            prediction = tf.keras.layers.Dense(
                units=2,  # Default number of classes from params.yaml
                activation="softmax"
            )(flatten_in)
            
            # Create the full model
            self.model = tf.keras.models.Model(
                inputs=base_model.input, 
                outputs=prediction
            )
            
            # Compile with default parameters
            self.model.compile(
                optimizer=tf.keras.optimizers.legacy.SGD(learning_rate=0.01),  # Default from params.yaml
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"]
            )
            
            print("Created new model with frozen base layers to match the original architecture")

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)



    
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
    