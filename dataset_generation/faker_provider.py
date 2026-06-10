
import random

from faker import Faker

fake = Faker("ru_RU")


MEDICINES = [

    "Амоксициллин",

    "Азитромицин",

    "Парацетамол",

    "Ибупрофен",

    "Метформин",

    "Лизиноприл",

    "Но-шпа",

    "Нимесулид",

    "Цефтриаксон",

    "Омепразол"

]


FORMS = [

    "таблетки",

    "капсулы",

    "раствор",

    "суспензия",

    "мазь"

]


DOSAGES = [

    "100 мг",

    "250 мг",

    "500 мг",

    "750 мг",

    "1 г"

]


DAYS = [



    "60",

    "90",

    "180",

    "365"

]


def generate_patient():
    last_name=fake.last_name()
    while len(last_name) > 10:
        last_name = fake.last_name()
    return (

        fake.last_name()

        + " "

        + fake.first_name()[0]

        + ". "

        + fake.middle_name()[0]

        + ". "
    )


def generate_doctor():

    return (

        fake.last_name()

        + " "

        + fake.first_name()[0]

        + "."

        + fake.middle_name()[0]

        + "."

    )


def generate_birth_date():

    return fake.date_of_birth(

        minimum_age=18,

        maximum_age=90

    ).strftime("%d.%m.%Y")


def generate_sample():

    return {

        "patient_name":

            generate_patient(),

        "birth_date":

            generate_birth_date(),

        "doctor_name":

            generate_doctor(),

        "medicine":

            random.choice(MEDICINES),

        "form":

            random.choice(FORMS),

        "dosage":

            random.choice(DOSAGES),

        "days":

            random.choice(DAYS)

    }
