import csv

from pathlib import Path

from config import RESULTS_FILE


HEADER = [

    "experiment",

    "model",

    "imgsz",

    "batch",

    "epochs",

    "precision",

    "recall",

    "map50",

    "map50_95"

]


def append_result(

        experiment,

        cfg,

        metrics

):

    file_exists = Path(

        RESULTS_FILE

    ).exists()

    with open(

            RESULTS_FILE,

            "a",

            newline="",

            encoding="utf8"

    ) as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow(HEADER)

        writer.writerow(

            [

                experiment,

                cfg["model"],

                cfg["imgsz"],

                cfg["batch"],

                cfg["epochs"],

                metrics["precision"],

                metrics["recall"],

                metrics["map50"],

                metrics["map50_95"]

            ]

        )