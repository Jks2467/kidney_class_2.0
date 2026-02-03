import os
from pathlib import Path
import shutil
from dataclasses import dataclass
from pathlib import Path
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_classes: int
    params_weights: str
    params_include_top: bool
    

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epoch: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
    params_learning_rate: float