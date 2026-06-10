import cv2

from detect import Detector

from ocr import OCR
from postprocess import postprocess

class Predictor:

    def __init__(self):

        self.detector = Detector()

        self.ocr = OCR()

    def predict(

            self,

            image_path

    ):

        detections = self.detector.detect(

            image_path

        )

        image = cv2.imread(

            image_path

        )

        result = {}

        for det in detections:

            x1, y1, x2, y2 = det["bbox"]

            crop = image[

                y1:y2,

                x1:x2

            ]

            text = self.ocr.recognize(

                crop

            )

            result[

                det["class"]

            ]=postprocess(

                det["class"],

                text

            )

        return result

import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Использование: python predict.py <image_path>")
        exit(1)

    predictor = Predictor()

    result = predictor.predict(sys.argv[1])

    for key, value in result.items():
        print(f"{key}: {value}")