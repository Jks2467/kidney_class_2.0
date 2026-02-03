from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig
import os

print("CONFIG_FILE_PATH:", CONFIG_FILE_PATH)
print("PARAMS_FILE_PATH:", PARAMS_FILE_PATH)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
    ):
        self.project_root = Path(__file__).resolve().parents[3]
        config_path = self.project_root / config_filepath
        params_path = self.project_root / params_filepath

        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        artifacts_root = os.path.join(self.project_root,self.config.artifacts_root )

        create_directories([Path(artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([Path(config.root_dir)])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(self.project_root /config.root_dir),
            source_URL=config.source_URL,
            unzip_dir=Path(self.project_root /config.unzip_dir),
        )

        return data_ingestion_config
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([Path(config.root_dir)])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(self.project_root /config.root_dir),
            base_model_path=Path(self.project_root /config.base_model_path),
            updated_base_model_path=Path(self.project_root /config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_classes=self.params.CLASSES,
            params_weights=self.params.WEIGHTS,
            params_include_top=self.params.INCLUDE_TOP

        )

        return prepare_base_model_config
    

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training 
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = Path(self.config.data_ingestion.unzip_dir)

        create_directories([training.root_dir])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epoch=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_image_size=params.IMAGE_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_learning_rate=params.LEARNING_RATE
        )

        return training_config