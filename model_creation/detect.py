from ultralytics import YOLO

from config import MODEL_PATH

from config import CONFIDENCE


class Detector:

    def __init__(

            self,

            model_path=MODEL_PATH

    ):

        self.model = YOLO(model_path)

    def detect(

            self,

            image

    ):

        result = self.model(

            image,

            conf=CONFIDENCE,

            verbose=False

        )[0]

        detections = []

        for box in result.boxes:

            cls = int(

                box.cls.item()

            )

            name = result.names[cls]

            conf = float(

                box.conf.item()

            )

            x1, y1, x2, y2 = (

                box.xyxy[0]

                .cpu()

                .numpy()

                .tolist()

            )

            detections.append(

                {

                    "class": name,

                    "confidence": conf,

                    "bbox": [

                        int(x1),

                        int(y1),

                        int(x2),

                        int(y2)

                    ]

                }

            )

        detections.sort(

            key=lambda x: (

                x["bbox"][1],

                x["bbox"][0]

            )

        )


        return detections

import cv2


def draw(

        image,

        detections

):

    img = cv2.imread(image)

    for d in detections:

        x1, y1, x2, y2 = d["bbox"]

        cv2.rectangle(

            img,

            (x1, y1),

            (x2, y2),

            (0,255,0),

            2

        )

        cv2.putText(

            img,

            d["class"],

            (x1,y1-10),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.7,

            (0,255,0),

            2

        )

    return img