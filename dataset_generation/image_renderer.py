
from pathlib import Path

import fitz

from PIL import Image

from PIL import ImageDraw

from PIL import ImageFont

from config_ import DPI

from config_ import FONT_SIZE

from config_ import FONT_DIR


class ImageRenderer:

    def __init__(self):

        self.scale = DPI / 72

        self.font = ImageFont.truetype(

            str(

                FONT_DIR /

                "times.ttf"

            ),

            FONT_SIZE

        )


    def render(

        self,

        page,

        marker_boxes,

        marker_to_field,

        marker_to_value,

        output_image

    ):

        pix = page.get_pixmap(

            dpi=DPI

        )

        tmp = str(output_image)+".tmp.png"

        pix.save(tmp)

        image = Image.open(tmp)

        draw = ImageDraw.Draw(image)

        annotation = {}

        for marker,data in marker_boxes.items():

            if marker not in marker_to_value:

                continue

            value = marker_to_value[marker]

            field = marker_to_field[marker]

            x0,y0,x1,y1 = data["bbox"]

            x0*=self.scale

            y0*=self.scale

            x1*=self.scale

            y1*=self.scale

            padding = 8

            draw.rectangle(

                (

                    x0-padding,

                    y0-padding,

                    x1+padding,

                    y1+padding

                ),

                fill="white"

            )

            draw.text(

                (

                    x0,

                    y0

                ),

                value,

                fill="black",

                font=self.font

            )

            left,top,right,bottom = draw.textbbox(

                (

                    x0,

                    y0

                ),

                value,

                font=self.font

            )

            annotation[field]={

                "text":value,

                "bbox":[

                    int(left),

                    int(top),

                    int(right),

                    int(bottom)

                ]

            }

        image.save(output_image)

        Path(tmp).unlink()

        return annotation
