from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

print("CONFIG_FILE_PATH:", CONFIG_FILE_PATH)
print("PARAMS_FILE_PATH:", PARAMS_FILE_PATH)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
    ):
        project_root = Path(__file__).resolve().parents[2]  # src/cnnClassifier/configuration.py → project root
        config_path = project_root / config_filepath
        params_path = project_root / params_filepath

        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([Path(config.root_dir)])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            unzip_dir=Path(config.unzip_dir),
        )

        return data_ingestion_config