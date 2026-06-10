
from pathlib import Path

import json

from faker_provider import generate_sample

from docx_renderer import DocxRenderer

from pdf_parser import PDFParser

from image_renderer import ImageRenderer

from yolo_export import YOLOExporter

from config_ import *
from augment import Augmenter

def run():
    augmenter = Augmenter()
    TEMP_DIR.mkdir(

        exist_ok=True,

        parents=True

    )

    OUTPUT_IMAGES.mkdir(

        exist_ok=True,

        parents=True

    )

    OUTPUT_LABELS.mkdir(

        exist_ok=True,

        parents=True

    )

    OUTPUT_YOLO.mkdir(

        exist_ok=True,

        parents=True

    )

    renderer = DocxRenderer(

        TEMPLATE_DOCX

    )

    pdf = PDFParser()

    image_renderer = ImageRenderer()

    yolo = YOLOExporter(

        IMAGE_WIDTH,

        IMAGE_HEIGHT

    )

    for index in range(DATASET_SIZE):

        print(

            f"{index+1}/{DATASET_SIZE}"

        )

        sample = generate_sample()

        docx_file = (

            TEMP_DIR /

            f"{index:06d}.docx"

        )

        marker_to_field,marker_to_value = renderer.create_document(

            docx_file,

            sample

        )

        pdf_path = pdf.convert_docx_to_pdf(

            docx_file,

            TEMP_DIR

        )

        page,marker_boxes = pdf.extract_marker_boxes(

            pdf_path

        )

        image_path = (

            OUTPUT_IMAGES /

            f"{index:06d}.png"

        )

        annotation = image_renderer.render(

            page,

            marker_boxes,

            marker_to_field,

            marker_to_value,

            image_path

        )
        augmenter.augment(
            image_path
        )
        json_path = (

            OUTPUT_LABELS /

            f"{index:06d}.json"

        )

        with open(

            json_path,

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                annotation,

                f,

                ensure_ascii=False,

                indent=4

            )

        yolo.export(

            annotation,

            OUTPUT_YOLO /

            f"{index:06d}.txt"

        )

        try:

            docx_file.unlink()

        except:

            pass

        try:

            pdf_path.unlink()

        except:

            pass

if __name__ == "__main__":
    run()