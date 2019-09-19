from datetime import date, datetime
from GameDay import GameDay
from ScheduleBot import ScheduleBot
import logging
import locale

def main():
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    logging.basicConfig(filename="log_%s.log" % datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

    with open('token', 'r') as tokenFile:
        token = tokenFile.read()
    bot = ScheduleBot(token)
    bot.Start()
    pass

if __name__ == "__main__":
    main()
