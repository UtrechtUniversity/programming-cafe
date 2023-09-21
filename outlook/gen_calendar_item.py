from ics import Calendar, Event
from datetime import datetime
c = Calendar()
e = Event()
e.name = "Programming Cafe"
e.begin = datetime.fromisoformat("2023-11-30T15:00:00+02:00")
e.end = datetime.fromisoformat("2023-11-30T17:00:00+02:00")
e.location = "Bucheliuszaal 6.18, University Library (Utrecht Science Park)"
c.events.add(e)
c.events
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('pcafe_dec2023.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
# and it's done !
