"""sketch.py parses the sketch.txt file by using the ':' sperator to split
the one speaking and their speach."""

import os
import hakim_nester

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
except IOError as err:
    print('The data file is missing' + str(err))

try:
    with open('man_data.txt', "w") as man_out:
        hakim_nester.print_lol(man, 0,0, man_out)
    with open('other_data.txt', "w") as other_out: 
        hakim_nester.print_lol(other,0,0, other_out)        

except IOError as err:
    print("Couldn't open file" + str(err))

