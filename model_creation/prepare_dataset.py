from pathlib import Path
import random
import shutil

from config import TRAIN_RATIO
from config import VAL_RATIO
from config import TEST_RATIO


def prepare_dataset():

    dataset = Path("images")

    train_dir = dataset / "images" / "train"

    if train_dir.exists():
        print("Dataset already prepared.")
        return

    images_dir = dataset / "images"
    labels_dir = dataset / "labels"
    yolo_dir = dataset / "yolo"

    images = sorted(images_dir.glob("*.png"))

    random.seed(42)

    random.shuffle(images)

    n = len(images)

    n_train = int(n * TRAIN_RATIO)
    n_val = int(n * VAL_RATIO)

    train = images[:n_train]
    val = images[n_train:n_train+n_val]
    test = images[n_train+n_val:]

    for split, files in {

        "train": train,
        "val": val,
        "test": test

    }.items():

        (images_dir / split).mkdir(exist_ok=True)

        (labels_dir / split).mkdir(exist_ok=True)
        (yolo_dir / split).mkdir(exist_ok=True)

        for image in files:

            label = labels_dir / (image.stem + ".json")
            yolo = yolo_dir / (image.stem + ".txt")

            shutil.move(

                image,

                images_dir / split / image.name

            )

            shutil.move(

                label,

                labels_dir / split / label.name

            )
            shutil.move(

                yolo,

                yolo_dir / split / yolo.name

            )
