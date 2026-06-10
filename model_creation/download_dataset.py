import os
from pathlib import Path

from huggingface_hub import snapshot_download

from config import DATASET_REPO
from config import DATASET_DIR


def download_dataset():

    dataset_path = Path(DATASET_DIR)
    data_yaml=Path("dataset/data.yaml")

    if data_yaml.exists():
        return
    if dataset_path.exists():
        print("Dataset already exists.")
        return dataset_path

    token = os.getenv("HF_TOKEN")

    if token is None:
        raise RuntimeError(
            "Environment variable HF_TOKEN is not set."
        )

    snapshot_download(

        repo_id=DATASET_REPO,

        repo_type="dataset",

        local_dir=DATASET_DIR,

        token=token

    )

    return dataset_path


if __name__ == "__main__":

    download_dataset()