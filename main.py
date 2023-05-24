# Author : Alexandre BOYER
# School : Terminale NSI - Lycée Saint-Louis à Orange
# School year : 2022/2023


import datetime
from dateutil.relativedelta import relativedelta
import time

lang = "fr"

texts = {
    "en": {
        "retirement": "the retirement",
        "sentence": "days left before",
    },
    "fr": {
        "retirement": "la retraite",
        "sentence": "jours restants avant",
    },
}

# Default date if date reading failed
default_date = datetime.date(1982, 7, 1)
retirement_age = 64
duration_work = relativedelta(years=retirement_age)
default_date = default_date + duration_work
default_date = [default_date.year, default_date.month, default_date.day]

arduino_mode = False
if arduino_mode:
    import JeulinLib
    JeulinLib.Connect("COM3")
    JeulinLib.LCD_RGB_Clear()
    JeulinLib.LCD_RGB_SetColor(255, 153, 153)
    JeulinLib.LCD_RGB_SetCusor(0, 0)


def print_arduino(prompt):
    while True:
        text = prompt
        if len(text) <= 16:
            JeulinLib.LCD_RGB_Write(text)
        else:
            liste = [" " for i in range(16)]
            for i in range(len(text)):
                liste.append(text[i])
            while len(liste) != 0:
                JeulinLib.LCD_RGB_Write(text)
                time.sleep(0.25)
                JeulinLib.LCD_RGB_Clear()
                del liste[0]
                text = ""
                for i in liste:
                    text += i


def run(event_name=texts[lang]["retirement"], event_date=default_date):
    while True:
        today = datetime.date.today()
        interval_days = datetime.date(
            event_date[0], event_date[1], event_date[2]) - today
        interval_days = interval_days.days
        if interval_days < 0:
            print("The event is over.")
            if arduino_mode:
                print_arduino("The event is over.")
        else:
            print(f"{interval_days} {texts[lang]['sentence']} {event_name}")
            if arduino_mode:
                print_arduino(
                    f"{interval_days} {texts[lang]['sentence']} {event_name}")

        # time.sleep(1)
        time.sleep(86400)  # 24 hours in seconds


run("le bac de philo", [2023, 6, 14])
