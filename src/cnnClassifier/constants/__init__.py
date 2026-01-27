from pathlib import Path

CONFIG_ROOT = Path(__file__).resolve().parents[3] 
PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_FILE_PATH = CONFIG_ROOT / "config/config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"