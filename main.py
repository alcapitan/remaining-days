# Author : Alexandre BOYER
# My school's name : Terminale NSI - Lycée Saint-Louis à Orange
# My school year : 2022/2023


## CONFIGURATION

# If you have the appropriate Arduino board (the model is specified in the README), you can print the text on the Arduino.
arduino_mode = False

# Choose your language here
lang = "en" # "en" for English, "fr" for French

# Find the run() function to set an event at the end of the program.


## PROGRAM

import datetime
from dateutil.relativedelta import relativedelta
import time

# Set up the Arduino device
if arduino_mode:
    # Remind to install necessary Arduino stuff and connect the card
    import JeulinLib
    JeulinLib.Connect("COM3") # Check which COM port is used by your Arduino card
    JeulinLib.LCD_RGB_Clear() # Clear the screen
    JeulinLib.LCD_RGB_SetColor(92, 214, 92) # Set a blue-green background
    JeulinLib.LCD_RGB_SetCusor(0, 0) # First line and first column

# Translations
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

# Default date if run() is called without arguments
default_date = datetime.date(1982, 7, 1) # Date of my teacher's birth
retirement_age = 64 # Retirement age in France
duration_work = relativedelta(years=retirement_age)
default_date = default_date + duration_work
default_date = [default_date.year, default_date.month, default_date.day]

def print_arduino(prompt):
    """
        Print a text on the Arduino screen.
        If the text is longer than the screen (16 boxes), then the text will scroll.
        I copied this program made by a former student of my high school.
    """
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

# Main function
def run(event_name=texts[lang]["retirement"], event_date=default_date):
    """
        The counter is updated every 24 hours.
        To stop the force program, press Ctrl + C on the keyboard at the same time (this keyboard shortcut works everywhere).
        Warn if the event is over.
    """
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

        time.sleep(86400)  # 24 hours in seconds


# Find the configuration on the top of the file
# Write your event name and date here (the format is [year, month, day])
run()
