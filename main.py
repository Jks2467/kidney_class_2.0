from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
import sys
import os
from pathlib import Path


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f"Error in Stage {STAGE_NAME}: {e}")
    raise e