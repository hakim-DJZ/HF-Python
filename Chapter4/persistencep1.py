"""sketch.py parses the sketch.txt file by using the ':' sperator to split
the one speaking and their speach."""

import os
import hakim_nester
import pickle

#hsellaoui/Documents/HF-Python/HF-Python

os.chdir('C:/Users/hakim/Documents/HF-Python/Chapter4/')
#os.chdir('C:/Users/hsellaoui/Documents/HF-Python/HF-Python/Chapter4/')

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
    with open('man_data.txt', "wb") as man_out:
        pickle.dump(man, man_out)
    with open('other_data.txt', "wb") as other_out: 
        pickle.dump(other, other_out)        

except PickleError as err:
    print("Couldn't open file" + str(err))

"""Test to see if it worked"""
try:
    with open('man_data.txt', "rb") as man_out:
        pickle.load(man_out)
    with open('other_data.txt', "rb") as other_out: 
        pickle.load(other_out)        

except pickle.PickleError as perr:
    print("Couldn't open file" + str(perr))

print(man)
print("\n\n\nNow other man\n\n\n\n")
print(other)
