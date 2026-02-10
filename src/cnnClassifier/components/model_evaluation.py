import mlflow
import mlflow.keras
from urllib.parse import urlparse
import dagshub
from pathlib import Path
import tensorflow as tf
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories, save_json
from cnnClassifier.entity.config_entity import EvaluationConfig

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def train_valid_generator(self):

        datagen_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.10
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear',
            class_mode="categorical" 
        )

        valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagen_kwargs
        )

        self.valid_generator = valid_datagen.flow_from_directory(
            directory=self.config.training_data,
            subset= 'validation',
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evalutation(self):
        self.model = self.load_model(self.config.model_path)
        self.train_valid_generator()
        self.score = self.model.evaluate(self.valid_generator)

    def save_score(self):
        scores = {'loss': self.score[0], 'accuracy': self.score[1]}
        save_json(path=Path("scores.json"), data=scores)


    def log_in_mlflow(self):
        dagshub.init(repo_owner='Jks2467', repo_name='kidney_class_2.0', mlflow=True)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {'loss': self.score[0], 'accuracy': self.score[1]}
            )

            if tracking_url_type_store != 'file':
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16")
            else:
                mlflow.keras.log_model(self.model, "model")