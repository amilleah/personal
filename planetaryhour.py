'''''
this is a very basic calculator meant to
get a rough estimate of current planetary time

check an actual planetary time online
(planetaryhours.net)

'''''

from datetime import datetime

planets = ['sun','moon','mars','mercury','jupiter','venus','saturn']
today = int(datetime.today().strftime('%w'))
tohour = int(datetime.today().strftime('%H'))

days = list(range(0,7))
daychart = {}

for day in days:
    plans = planets[day:] + planets[:day]
    daychart[day] = plans + plans + plans + plans   #will index by the hour, is fine 

dc = daychart[today]

planetaryday = dc[0]
planetaryhour = dc[tohour]

print('day - ',planetaryday)
print('hour - ',planetaryhour) #+/- 15 mins, is fine

    