from ultralytics import YOLO

from config import DATASET


def evaluate(

        model_path,

        imgsz=2048

):

    model = YOLO(model_path)

    metrics = model.val(

        data=DATASET,

        imgsz=imgsz

    )

    return {

        "precision": float(metrics.box.mp),

        "recall": float(metrics.box.mr),

        "map50": float(metrics.box.map50),

        "map50_95": float(metrics.box.map)

    }