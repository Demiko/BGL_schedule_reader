from GameEvent import GameEvent
from datetime import date
from bs4 import BeautifulSoup
import requests as req

calendarBaseURL = "https://club.bgl.com.ua/calendar/"

class GameDay:
    """description of class"""
    def __init__(self, date: date):
        self.date = date
        self.events = []
        schedulePage = req.get(calendarBaseURL + date.isoformat())
        events = BeautifulSoup(schedulePage.text, 'lxml').find(class_='calendar-events')
        for event in events.find_all(class_='event-item'):
            ge = GameEvent(event)
            self.events.append(ge)
            pass
        pass
    pass
