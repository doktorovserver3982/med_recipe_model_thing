
from pathlib import Path

CLASS_MAP = {

    "patient_name":0,

    "birth_date":1,

    "doctor_name":2,

    "medicine":3,

    "form":4,

    "dosage":5,

    "days":6

}


class YOLOExporter:

    def __init__(

        self,

        image_width,

        image_height

    ):

        self.image_width = image_width

        self.image_height = image_height


    def export(

        self,

        annotation,

        output_path

    ):

        lines = []

        for field,data in annotation.items():

            if field not in CLASS_MAP:

                continue

            left,top,right,bottom = data["bbox"]

            x = (left + right)/2

            y = (top + bottom)/2

            w = right-left

            h = bottom-top

            x /= self.image_width

            y /= self.image_height

            w /= self.image_width

            h /= self.image_height

            cls = CLASS_MAP[field]

            line = (

                f"{cls} "

                f"{x:.6f} "

                f"{y:.6f} "

                f"{w:.6f} "

                f"{h:.6f}"

            )

            lines.append(line)

        Path(output_path).write_text(

            "\n".join(lines),

            encoding="utf8"

        )

