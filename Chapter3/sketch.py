"""sketch.py parses the sketch.txt file by using the ':' sperator to split
the one speaking and their speach."""

import os

os.chdir('C:/Users/hakim/Documents/HF-Python/Chapter3/')

try:
    data = open('sketch.txt')

    for eachLine in data:
        try:
            (role,line_spoken) = eachLine.split(":",1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The data file is missing')

