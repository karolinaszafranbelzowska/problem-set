# solution to problem number 9
# Karolina Szafran Belzowska, 2019/03/27
# Command Line arguments

import sys

# A function that take the filename from an argument on the command line.
# Adapted from: https://www.youtube.com/watch?v=qjdeQ83T9sQ
# sys.argv[0] = solution-9.py
# sys.argv[1] = my_text

filename = "my_text.txt"
f = open(filename, "r+")
# output will be every second line from my_text

text = f.readline()
text1 = f.readline()
text2 = f.readline()
text3 = f.readline()
text4 = f.readline()
text5 = f.readline()
text6 = f.readline()
text7 = f.readline()
text8 = f.readline()
text9 = f.readline()
text10 = f.readline()
text11 = f.readline()
text12 = f.readline()
text13 = f.readline()
text14 = f.readline()
text15 = f.readline()
text16 = f.readline()
text17 = f.readline()
text18 = f.readline()
text19 = f.readline()
text20 = f.readline()

print(text, text2, text4, text6, text8, text10, text12, text14, text16, text18, text20)
f.close()



# This will print two arguments I used in solution-9.py
print(sys.argv[0], sys.argv[1])








