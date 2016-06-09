"""ex1ch5.py: Program reads data from file into a list.  Comma is used as delimeter, then print to
std.out to show it worked"""

import os
import pickle
from sanitize import sanitizer

#hsellaoui/Documents/HF-Python/HF-Python

#os.chdir('C:/Users/hakim/Documents/HF-Python/Chapter5/')
os.chdir('C:/Users/hsellaoui/Documents/HF-Python/HF-Python/Chapter5/')

#List variables
james = []
julie = []
sarah = []
mikey = []

#List of file names
fileNames = ["james.txt", "julie.txt", "sarah.txt", "mikey.txt"]

for file in fileNames:
    try:
        with open(file) as data:
            for eachLine in data:
                try:                   
                    if   file == "james.txt":                        
                        james  = eachLine.strip().split(",")
                    elif file == "julie.txt":
                        julie = eachLine.strip().split(",")
                    elif file == "sarah.txt":
                        sarah = eachLine.strip().split(",")
                    elif file == "mikey.txt":
                        mikey = eachLine.strip().split(",")
                except ValueError:
                    pass
                
    except IOError as err:
        print('The data file is missing' + str(err))

jamesNew = sorted([ sanitizer(each_t) for each_t in james ])
julieNew = sorted([ sanitizer(each_t) for each_t in julie ])
sarahNew = sorted([ sanitizer(each_t) for each_t in sarah ])
mikeyNew = sorted([ sanitizer(each_t) for each_t in mikey ])

print("For James \n")
print(sorted(james))    
print(sorted(jamesNew))

print("\n\nFor Julie \n")
print(sorted(julie))
print(sorted(julieNew))

print("\n\nFor Sarah \n")
print(sorted(sarah))
print(sorted(sarahNew))

print("\n\nFor Mikey \n")
print(sorted(mikey))
print(sorted(mikeyNew))
