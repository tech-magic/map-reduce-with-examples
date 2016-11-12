# Count Number of Friends with MapReduce
# =======================================
#
# Here's a quick introduction to the idea of splitting tasks into a MapReduce model.
# The four important functions involved are:
#
# Map (the mapper function)  
# EmitIntermediate(the intermediate key,value pairs emitted by the mapper functions)  
# Reduce (the reducer function)  
# Emit (the final output, after summarization from the Reduce functions)
#
# ------- Problem -----------
# The input is a number of lines with pairs of name of friends, in the form:
# [Friend1] [Friend2]
# The required output is to print the number of friends of each person.
#
# Credits to Original Problem @ -> https://www.hackerrank.com/challenges/map-reduce-advanced-count-number-of-friends
#
# ------- Sample Input ------
# Joe Sue
# Sue Phi
# Phi Joe
# Phi Alice
#
# ------- Sample Output -----
# {"key":"Alice","value":"1"}
# {"key":"Joe","value":"2"}
# {"key":"Phi","value":"3"}
# {"key":"Sue","value":"2"}
#
# The solution is implemented as follows in python.
#

import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print "{\"key\":\""+item[0]+"\",\"value\":\"" + str(item[1]) + "\"}"

mapReducer = MapReduce()

def mapper(record):
    names = record.split()
    mapReducer.emitIntermediate(names[0], names[1])
    mapReducer.emitIntermediate(names[1], names[0])

def reducer(key, list_of_values):
    reducedRecord = [key, len(list_of_values)]
    mapReducer.emit(reducedRecord)
    
if __name__ == '__main__':
    inputData = []
    for line in sys.stdin:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)
