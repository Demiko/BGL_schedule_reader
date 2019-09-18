from bs4 import BeautifulSoup
import requests as req
import time
import re
from game_event import GameEvent

calendarBaseURL = "https://club.bgl.com.ua/calendar/"

def main():
    day = list(time.localtime())
    schedulePage = req.get(calendarBaseURL + time.strftime('%Y-%m-%d', tuple(day)))
    events = BeautifulSoup(schedulePage.text, 'lxml').find(class_='calendar-events')
    for event in events.find_all(class_='event-item'):
        ge = GameEvent(event)
        print('ID: %s' % ge.id)
        print('Event: %s' % ge.title)
        print('Type: %s' % ge.type)
        print('Time: %s' % ge.time)
        print('Free seats: %s' % ge.seats)
        print()
        pass
    pass

if __name__ == "__main__":
    main()
