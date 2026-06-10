from pathlib import Path

# ==========================
# Dataset
# ==========================

DATASET = "dataset/data.yaml"
TRAIN_RATIO = 0.7

VAL_RATIO = 0.2

TEST_RATIO = 0.1
# ==========================
# Training
# ==========================

DEFAULT_MODEL = "yolo11n.pt"

DEFAULT_EXPERIMENT = "baseline"

DEVICE = 0

WORKERS = 2

PATIENCE = 20

PROJECT = "models"

SAVE = True

SAVE_PERIOD = -1

PRETRAINED = True

RECT = True

VERBOSE = True

# ==========================
# Output
# ==========================

RESULTS_FILE = Path("results.csv")

MODEL_PATH = (
    "models/highres_nomosaic/weights/best.pt"
)

CONFIDENCE = 0.25

# OCR

OCR_LANGUAGE = "ru"

OCR_USE_ANGLE = True

# Dataset


DATASET_DIR = "dataset"

DATASET_REPO = "wuht0s1swuh/medical_recipe_dataset"