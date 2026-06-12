from pathlib import Path
import shutil
def fix_warning():
    for split in ["train", "val", "test"]:

        src=Path(f"/kaggle/input/datasets/ohoohooo/med-recipe-dataset-form-107-1/images/yolo/{split}")
        dst=Path(f"/kaggle/input/datasets/ohoohooo/med-recipe-dataset-form-107-1/images/labels/{split}")

        dst.mkdir(parents=True, exist_ok=True)

        for file in src.glob("*.txt"):
            shutil.copy(file, dst / file.name)

    print("Done")

if __name__ == "__main__":
    fix_warning()