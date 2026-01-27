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
