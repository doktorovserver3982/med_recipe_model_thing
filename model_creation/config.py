from pathlib import Path
import os

# Get current working directory (your Kaggle notebook directory)
WORK_DIR = Path.cwd()

# ==========================
# Dataset
# ==========================
DATASET_DIR = Path(f"/kaggle/input/datasets/ohoohooo/med-recipe-dataset-form-107-1/images")
DATASET = str(DATASET_DIR / "data.yaml")  # Full path
TRAIN_RATIO = 0.7
VAL_RATIO = 0.2
TEST_RATIO = 0.1

# ==========================
# Training
# ==========================
DEFAULT_MODEL = "yolo11n.pt"
DEFAULT_EXPERIMENT = "baseline"
DEVICE = 0  # We'll override this programmatically
WORKERS = 4
PATIENCE = 20
PROJECT = str(WORK_DIR / "models")  # Changed to working directory
SAVE = True
SAVE_PERIOD = -1
PRETRAINED = True
RECT = True
VERBOSE = True

# ==========================
# Output
# ==========================
RESULTS_FILE = WORK_DIR / "results.csv"
MODEL_PATH = str(WORK_DIR / "models/highres_nomosaic/weights/best.pt")
CONFIDENCE = 0.25

# OCR
OCR_LANGUAGE = "ru"
OCR_USE_ANGLE = True

# Dataset
DATASET_REPO = "wuht0s1swuh/medical_recipe_dataset"