# Karolina Szafran Belzowska, 2018-03-18
# Today is?

import datetime
today = datetime.datetime.today()
f = "%A, %B %dth, %Y at %H:%M"
s = today.strftime(f)

if (3 <= day <= 21) or (23 <= day <= 31):

    s = str(s) + 'th'
else:
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    s = str(s) + suffixes[s % 10]
    
print("Today is:", s)
