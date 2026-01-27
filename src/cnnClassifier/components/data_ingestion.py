from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
import os
from pathlib import Path
import shutil


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def copy_files(self):
        try:
            os.makedirs(self.config.unzip_dir, exist_ok=True)
            logger.info(f"Copying files to {self.config.unzip_dir}")
            src_path = Path(self.config.source_URL)
            dest_path = Path(self.config.unzip_dir)
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
            logger.info(f"Files copied successfully to {self.config.unzip_dir}")
            logger.info(f"Total size of copied files: {get_size(self.config.unzip_dir)}")
        except Exception as e:
            logger.error(f"Error occurred while copying files: {e}")
            raise e