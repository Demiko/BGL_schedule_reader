from bs4.element import Tag
import re

class GameEvent:
    """an object representing data about BGL game event"""
    def __init__(self, event: Tag):
        # glyphicons are noize
        for glyph in event.find_all(class_='glyphicon'): glyph.decompose()

        try:
            self.id = re.search('\d+', event.find(class_='btn')['href']).group()
            self.link = 'https://club.bgl.com.ua/calendar/event/%s' % self.id
        except: self.id = 'id not found'

        try: self.title = event.find(class_="event-item-title").a.text.strip()
        except: self.title = 'title not found'

        try:
            # Should change this later to read the class tag.
            # Reason: because MTG has one type but several different type titles.
            self.type = event.find(class_='event-type').text.strip()
        except: self.type = 'type not found'

        try: self.time = event.find(class_='event-item-time').text.strip()
        except: self.time = 'time not found'

        try:
            tmp = re.search(r'\d+', event.find(class_='event-item-users').text)
            self.seats = tmp.group() if tmp else '0'
            del tmp
        except: self.seats = 'seats not found'
        pass
pass
