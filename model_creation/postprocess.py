import re


def normalize_spaces(text):

    return " ".join(

        text.split()

    )


def normalize_dosage(text):

    text = text.replace(

        "м г",

        "мг"

    )

    text = text.replace(

        "мл ",

        "мл"

    )

    return text


def normalize_date(text):

    text = text.replace(

        ",",

        "."

    )

    text = text.replace(

        " ",

        ""

    )

    return text


def normalize_case(text):

    return text.strip()


def postprocess(field, text):

    text = normalize_spaces(text)

    text = normalize_case(text)

    if field == "birth_date":

        text = normalize_date(text)

    if field == "dosage":

        text = normalize_dosage(text)

    return text