# Karolina Szafran Belzowska, 2019-03-15
# Is it a day that begins with letter T?
# Adapted from Dr Ian McLoughlin's video (Module Programming and scripting - week 1)

import datetime

if datetime.datetime.today().weekday() == 1 and 3:
    print("Yes,today is a day which begins with a letter T")
else:
    print("No, today is a day which does not begins with a letter T")
