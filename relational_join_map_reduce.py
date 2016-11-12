# Relational Join with MapReduce
# ===============================
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
# The input is a number of lines with records from two tables Employee and Department. A tuple from Employee table 
# will look like:
# Employee [Person_Name] [SSN]
#
# A tuple from Department table will look like:
# Department [SSN] [Department_Name]
#
# Credits to Original Problem @ -> https://www.hackerrank.com/challenges/map-reduce-advanced-relational-join
#
# ------- Sample Input ------
# Department,1234,Sales
# Employee,Susan,1234
# Department,1233,Marketing
# Employee,Joe,1233
# Department,1233,Accounts
#
# ------- Sample Output -----
# ('1233', 'Joe', 'Accounts')
# ('1233', 'Joe', 'Marketing')
# ('1234', 'Susan', 'Sales')
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
            print item

mapReducer = MapReduce()

def mapper(record):
    myrecord = record.replace('\n', '')
    fields = myrecord.split(',')
    if fields[0] == 'Department': 
        mapReducer.emitIntermediate(fields[1], fields[2] + '_dept_');    
    else:
        mapReducer.emitIntermediate(fields[2], fields[1] + '_emp_');    
    
def reducer(key, list_of_values):
    depts = []
    emps = []
    for record in list_of_values:
        fields = record.split('_')
        if(fields[1] == 'dept'):
            depts.append(fields[0])
        else:
            emps.append(fields[0])
    for dept in depts:
        for emp in emps:
            mapReducer.emit((key, emp, dept))
            
            
if __name__ == '__main__':
    inputData = []
    for line in sys.stdin:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)
