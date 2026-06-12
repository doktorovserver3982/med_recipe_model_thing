import sys

from ultralytics import YOLO

from config import *
from experiments import EXPERIMENTS
def train(experiment_name):
    #download_dataset()
    #prepare_dataset()
    #fix_warning()
    cfg = EXPERIMENTS[experiment_name]

    model = YOLO(cfg["model"])

    model.train(

        data=DATASET,

        imgsz=cfg["imgsz"],

        batch=cfg["batch"],

        epochs=cfg["epochs"],

        mosaic=cfg["mosaic"],

        mixup=cfg["mixup"],

        copy_paste=cfg["copy_paste"],

        degrees=cfg["degrees"],

        perspective=cfg["perspective"],

        shear=cfg["shear"],

        rect=RECT,

        workers=WORKERS,

        patience=PATIENCE,

        pretrained=PRETRAINED,

        save=SAVE,

        save_period=SAVE_PERIOD,

        project=PROJECT,

        name=experiment_name,

        device=DEVICE,

        verbose=VERBOSE

    )
    from evaluate import evaluate
    from results import append_result



    metrics=evaluate(

        f"models/{experiment_name}/weights/best.pt",

        imgsz=cfg["imgsz"]

    )

    append_result(

        experiment_name,

        cfg,

        metrics

    )

if __name__ == "__main__":

    if len(sys.argv) == 1:

        train(DEFAULT_EXPERIMENT)

    elif sys.argv[1] == "-all":

        for exp in EXPERIMENTS:

            train(exp)

    else:

        train(sys.argv[1])

