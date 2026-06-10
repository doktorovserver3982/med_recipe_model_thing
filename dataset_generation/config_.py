
from pathlib import Path

# -----------------------------
# Пути
# -----------------------------

BASE_DIR = Path(__file__).parent

TEMPLATE_DOCX = BASE_DIR / "templates" / "form107.docx"

TEMP_DIR = BASE_DIR / "temp"

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_IMAGES = OUTPUT_DIR / "images"

OUTPUT_LABELS = OUTPUT_DIR / "labels"

OUTPUT_YOLO = OUTPUT_DIR / "yolo"

FONT_DIR = BASE_DIR / "fonts"

# -----------------------------
# LibreOffice
# -----------------------------

SOFFICE_PATH = r"C:\Program Files\LibreOffice\program\soffice.exe"
#SOFFICE_PATH = r"/usr/bin/soffice"

# -----------------------------
# Генерация
# -----------------------------

DATASET_SIZE = 1

DPI = 300

FONT_SIZE = 38

IMAGE_WIDTH = 2480

IMAGE_HEIGHT = 3508

# -----------------------------
# Маркеры шаблона
# -----------------------------

FIELDS = {

    "{patient_name}": "patient_name",

    "{birth_date}": "birth_date",

    "{doctor_name}": "doctor_name",

    "{medications.name}": "medicine",

    "{medications.form}": "form",

    "{medications.dosage}": "dosage",

    "{prescription_days}": "days"

}

