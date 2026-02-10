from cnnClassifier.config.configuration import ConfigurationManager
import os
from pathlib import Path
from cnnClassifier import logger
import sys
import os
from cnnClassifier.components.model_evaluation import Evaluation


STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evalutation()
        evaluation.save_score()
        evaluation.log_in_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"Error in Stage {STAGE_NAME}: {e}")
        raise e