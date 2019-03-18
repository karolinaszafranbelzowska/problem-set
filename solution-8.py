# Karolina Szafran Belzowska, 2018-03-18
# Today is?

import datetime
today = datetime.datetime.today()
f = "%A, %B %dth, %Y at %H:%M"
s = today.strftime(f)

print("Today is:", s)
