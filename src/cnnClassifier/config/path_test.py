from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig
from pathlib import Path
import os

print("CONFIG_FILE_PATH:", CONFIG_FILE_PATH)
print("PARAMS_FILE_PATH:", PARAMS_FILE_PATH)


config_filepath= Path(CONFIG_FILE_PATH)
params_filepath= Path(PARAMS_FILE_PATH)
project_root = Path(__file__).resolve().parents[3]
config_path = project_root / config_filepath
params_path = project_root / params_filepath

config = read_yaml(config_path)
# params = read_yaml(params_path)

root_path_test= os.path.join(project_root,config.artifacts_root)
print(project_root)
print(root_path_test)