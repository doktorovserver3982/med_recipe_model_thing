
import cv2

import albumentations as A


class Augmenter:

    def __init__(self):

        self.pipeline = A.Compose(

            [

                A.MotionBlur(

                    blur_limit=5,

                    p=0.25

                ),

                A.GaussNoise(

                    std_range=(0.02, 0.08),

                    p=0.3

                ),

                A.RandomBrightnessContrast(

                    brightness_limit=0.15,

                    contrast_limit=0.15,

                    p=0.4

                ),

                A.ImageCompression(

                    quality_range=(60,95),

                    p=0.4

                )

            ]

        )


    def augment(self, image_path):

        image = cv2.imread(str(image_path))

        if image is None:

            raise RuntimeError(

                f"Не удалось открыть {image_path}"

            )

        image = self.pipeline(

            image=image

        )["image"]

        cv2.imwrite(

            str(image_path),

            image

        )

