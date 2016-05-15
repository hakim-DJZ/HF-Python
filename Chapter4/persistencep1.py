"""sketch.py parses the sketch.txt file by using the ':' sperator to split
the one speaking and their speach."""

import os

os.chdir('C:/Users/hakim/Documents/HF-Python/Chapter4/')

man     = []
other   = []

try:
    data = open('sketch.txt')

    for eachLine in data:
        try:
            (role,line_spoken) = eachLine.split(":",1)
            line_spoken = line_spoken.strip()
            if   role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print('The data file is missing')

try:
    man_out     = open('man_data.txt', "w")
    other_out   = open('other_data.txt', "w")

    print(man, file=man_out)
    print(other, file=other_out)

    man_out.close()
    other_out.close()

except IOError:
    print("Couldn't open file")
    
