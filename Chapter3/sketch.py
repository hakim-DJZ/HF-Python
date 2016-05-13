"""sketch.py parses the sketch.txt file by using the ':' sperator to split
the one speaking and their speach."""

import os

os.chdir('C:/Users/hsellaoui/Documents/HF-Python/HF-Python/Chapter3')

data = open('sketch.txt')

for eachLine in data:
    if eachLine.find(':') > 0:
        (role,line_spoken) = eachLine.split(":",1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    else:
        print(eachLine, end='')        

data.close()
