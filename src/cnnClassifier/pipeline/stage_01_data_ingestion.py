from cnnClassifier.config.configuration import ConfigurationManager
import os
from pathlib import Path
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
import sys
import os



STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion)
        data_ingestion.copy_files()
    

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"Error in Stage {STAGE_NAME}: {e}")
        raise e