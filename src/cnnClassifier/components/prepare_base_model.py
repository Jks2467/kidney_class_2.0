import os
from urllib import request
from zipfile import ZipFile
from pathlib import Path
import tensorflow as tf
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,
            classes=self.config.params_classes
        )

        self.save_model(model=self.model, path=self.config.base_model_path)

    
    @staticmethod
    def save_model(model: tf.keras.Model, path: Path):
        model.save(path)
        logger.info(f"Model saved at: {path}")  

    
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        else:
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.Model(inputs=model.input, outputs=prediction)
        
        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )

        logger.info("Full model is prepared and compiled.")

        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(model=self.full_model, path=self.config.updated_base_model_path)
    
    