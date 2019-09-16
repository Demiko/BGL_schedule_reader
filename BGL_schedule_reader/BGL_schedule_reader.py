from bs4 import BeautifulSoup
import requests as req
import time
import re

calendar = "https://club.bgl.com.ua/calendar/"

def main():
    day = list(time.localtime())
    schedule_page = req.get(calendar + time.strftime('%Y-%m-%d', tuple(day)))
    events = BeautifulSoup(schedule_page.text, 'lxml').find(class_='calendar-events')

    for event in events.find_all(class_='event-item'):

        for glyph in event.find_all(class_='glyphicon'):
            glyph.extract()

        ev_id = re.search(r'\d+', event.find(class_='btn')['href']).group()
        print('ID: %s' % ev_id)

        ev_title = event.find(class_="event-item-title")
        print('Event: %s' % ev_title.a.text.strip())

        ev_type = event.find(class_='event-type')
        print('Type: %s' % ev_type.text.strip())

        ev_time = event.find(class_='event-item-time')
        print('Time: %s' % ev_time.text.strip())

        ev_users = event.find(class_='event-item-users')
        ev_seats = re.search(r'\d+', ev_users.text);
        ev_seats = ev_seats.group() if ev_seats is not None else '0'
        print('Free seats: %s' % ev_seats)

        ev_link = 'https://club.bgl.com.ua' + event.find(class_='btn')['href']
        print('Link: %s' % ev_link)

        print()

    pass

if __name__ == "__main__":
    main()