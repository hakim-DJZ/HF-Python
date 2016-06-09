"""ex1ch5.py: Program reads data from file into a list.  Comma is used as delimeter, then print to
std.out to show it worked"""

import os
import pickle
from sanitize import sanitizer
from Coach import get_coach_data

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


james = get_coach_data(fileNames[0])
julie = get_coach_data(fileNames[1])
sarah = get_coach_data(fileNames[2])
mikey = get_coach_data(fileNames[3])

#set removes duplicate data, then we sort it and store top three into name[]
james = sorted( set([ sanitizer(each_t) for each_t in james ]))[0:3]
julie = sorted( set([ sanitizer(each_t) for each_t in julie ]))[0:3]
sarah = sorted( set([ sanitizer(each_t) for each_t in sarah ]))[0:3]
mikey = sorted( set([ sanitizer(each_t) for each_t in mikey ]))[0:3]


print("For James \n")
print(james)

print("\n\nFor Julie \n")
print(julie)

print("\n\nFor Sarah \n")
print(sarah)

print("\n\nFor Mikey \n")
print(mikey)
