import datetime
from dateutil.relativedelta import relativedelta
import time

# Default date if date reading failed
default_date = datetime.date(1982, 7, 1)
retirement_age = 67
duration_work = relativedelta(years=retirement_age)
default_date = default_date + duration_work

arduino_mode = False
if arduino_mode:
    import JeulinLib
    JeulinLib.Connect("COM3")
    JeulinLib.LCD_RGB_Clear()
    JeulinLib.LCD_RGB_SetCusor(0, 0)
    JeulinLib.LCD_RGB_SetColor(255, 153, 153)


def read_date_file():
    with open("date.txt", 'r') as f:
        content = f.read().strip()
    date = [int(num) for num in content.split(',')]
    date = datetime.date(date[0], date[1], date[2])
    return date


def run():
    while True:
        today = datetime.date.today()
        try:
            interval_days = read_date_file() - today
        except:
            interval_days = default_date - today
        interval_days = interval_days.days
        print(interval_days)
        if arduino_mode:
            JeulinLib.LCD_RGB_Write(interval_days)
        # time.sleep(1)
        time.sleep(86400)  # 24 hours in seconds


# print(read_date_file())
run()
