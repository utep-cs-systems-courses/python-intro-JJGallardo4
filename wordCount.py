import string
import sys
import re

readf = open(sys.argv[1], "r")

dict = {}

for l in readf:
    newl = re.sub(r'[^\w\s]', ' ', l)
    newl = newl.lower()
    newl = newl.replace("\n", " ")
    line  = newl.split(" ")
    for word in line:
        if(word in dict):
            dict[word] += 1
        else:
            dict[word] = 1
        #end of if
    #end of for
#end of for
dict.pop("", None)

outputf = open(sys.argv[2], "w")
keys = list(dict.keys())
keys.sort()

for k in keys:
    outputf.write(str(k)+ " " + str(dict[k]) + "\n")

readf.close()
outputf.close()