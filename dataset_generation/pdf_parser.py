
import subprocess
from pathlib import Path

import fitz

from config_ import SOFFICE_PATH

import re

MARKER_PATTERN = re.compile(r"^§[A-Z]\d{3}§$")
class PDFParser:

    def __init__(self):

        pass

    def convert_docx_to_pdf(
        self,
        docx_path,
        output_dir
    ):

        output_dir = Path(output_dir)

        output_dir.mkdir(
            exist_ok=True,
            parents=True
        )

        subprocess.run(

            [

                SOFFICE_PATH,

                "--headless",

                "--convert-to",

                "pdf",

                str(docx_path),

                "--outdir",

                str(output_dir)

            ],

            check=True

        )

        pdf_name = (

            Path(docx_path).stem

            + ".pdf"

        )

        return output_dir / pdf_name


    def extract_marker_boxes(
        self,
        pdf_path
    ):

        doc = fitz.open(pdf_path)

        page = doc[0]

        words = page.get_text(
            "words"
        )

        markers = {}

        for word in words:

            x0,y0,x1,y1,text,*_ = word

            if MARKER_PATTERN.match(text):

                markers[text] = {

                    "bbox":[

                        x0,

                        y0,

                        x1,

                        y1

                    ]

                }

        return page,markers

