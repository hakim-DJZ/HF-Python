"""ex1ch5.py: Program reads data from file into a list.  Comma is used as delimeter, then print to
std.out to show it worked"""

import os
import pickle

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
        data = open(file)

        for eachLine in data:
            try:
                eachLine    = eachLine.strip()
                time        = eachLine.split(",",1)
                
                if   file == "james.txt":
                    james.append(time)
                elif file == "julie.txt":
                    julie.append(time)
                elif file == "sarah.txt":
                    sarah.append(time)
                elif file == "mikey.txt":
                    mikey.append(time)
            except ValueError:
                pass

        data.close()
    except IOError as err:
        print('The data file is missing' + str(err))

print(james)
print(julie)
print(sarah)
print(mikey)
        
