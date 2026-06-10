from paddleocr import PaddleOCR

from config import OCR_LANGUAGE
from config import OCR_USE_ANGLE


class OCR:

    def __init__(self):

        self.ocr = PaddleOCR(

            lang=OCR_LANGUAGE,

            use_angle_cls=OCR_USE_ANGLE,

            show_log=False

        )

    def recognize(self, image):

        result = self.ocr.ocr(

            image,

            cls=True

        )

        if result is None:
            return ""

        if len(result) == 0:
            return ""

        if result[0] is None:
            return ""

        text = []

        for line in result[0]:

            text.append(

                line[1][0]

            )

        return " ".join(text).strip()