EXPERIMENTS = {

    "baseline": {

        "model": "yolo11n.pt",

        "imgsz": 1280,

        "batch": 8,

        "epochs": 100,

        "mosaic": 1.0,

        "mixup": 0.0,

        "copy_paste": 0.0,

        "degrees": 0.0,

        "perspective": 0.0,

        "shear": 0.0

    },

    "highres": {

        "model": "yolo11n.pt",

        "imgsz": 2048,

        "batch": 4,

        "epochs": 100,

        "mosaic": 1.0,

        "mixup": 0.0,

        "copy_paste": 0.0,

        "degrees": 0.0,

        "perspective": 0.0,

        "shear": 0.0

    },

    "highres_nomosaic": {

        "model": "yolo11n.pt",

        "imgsz": 2048,

        "batch": 4,

        "epochs": 100,

        "mosaic": 0.0,

        "mixup": 0.0,

        "copy_paste": 0.0,

        "degrees": 0.0,

        "perspective": 0.0,

        "shear": 0.0

    }

}