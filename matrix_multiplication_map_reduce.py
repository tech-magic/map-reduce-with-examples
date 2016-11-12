# Matrix Multiplication with MapReduce
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
# The input is a number of test cases with two matrices each. A single test case will look like:
#
# [#Rows_Matrix_1] [#Columns_Matrix_1]
# [Row_1_Matrix_1]
# .
# .
# [Row_N_Matrix_1]
# [#Rows_Matrix_2] [#Columns_Matrix_2]
# [Row_1_Matrix_2]
# .
# .
# [Row_N_Matrix_2]
# 
# Credits to Original Problem @ -> https://www.hackerrank.com/challenges/map-reduce-advanced-matrix-multiplication
#
# Note that in our sample input we have only 1 test case. This is why the first line is 1.
# For this single test case we have the first matrix with 3 rows and 2 columns;
# | 1 2 |
# | 2 3 |
# | 4 5 |
#
# We have the second matrix with 2 rows and 3 columns;
# | 2 4 5 |
# | 3 6 7 |
#
# Upon multiplication we should get the Sample Output Matrix
# | 8 16 19| 
# |13 26 31| 
# |23 46 55|
#
# -------- Sample Input -----
#
# 1
# 3 2
# 1 2
# 2 3
# 4 5
# 2 3
# 2 4 5
# 3 6 7
#
# -------- Sample Output ----
#
#  8 16 19 
# 13 26 31 
# 23 46 55
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
        self.result[value[0]][value[1]] = value[2] 

    def execute(self, matrix1, matrix2, mapper, reducer):
        n = len(matrix1)
        m = len(matrix2[0])
        for i in xrange(0,n):
            self.result.append([0]*m)
        
        mapper(matrix1, matrix2)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for i in xrange(0,n):
            row = ""
            for j in xrange(0,m):
                 row += str(self.result[i][j]) + " "
            print row

mapReducer = None

# The mapper is; {m1RowId, [(m1Row, m2Col1), (m1Row, m2Col2), ... , (m1Row, m2Coln)]}
def mapper(matrix1, matrix2):
    m1RowLen = len(matrix1)
    m2ColLen = len(matrix2[0])
    m2RowLen = len(matrix2)
    for i in xrange(0, m1RowLen):
        m1CurrRow = matrix1[i]
        for j in xrange(0, m2ColLen):
            currCol = []
            for k in xrange(0, m2RowLen):
                currCol.append(matrix2[k][j])
            mapReducer.emitIntermediate(i, [m1CurrRow, currCol]) 

# In the reducer; key is the row id of the answer matrix
def reducer(key, list_of_values):
    for j in xrange(0, len(list_of_values)):
        value = list_of_values[j]
        m1Row = value[0]
        m2Col = value[1]
        result = 0
        for i in xrange(0, len(m1Row)):
            result += m1Row[i] * m2Col[i]
        mapReducer.emit([key, j, result])
    
    
if __name__ == '__main__':
    testcases = int(sys.stdin.readline().strip())
    for t in xrange(0, testcases):
        mapReducer = MapReduce()
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        matrix1 = []
        matrix2 = []
        for i in range(0, row):
            read_row = sys.stdin.readline().strip()
            matrix1.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix1[i].append(int(row_elems[j]))
                
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        for i in range(0, row):
            read_row = sys.stdin.readline().strip()
            matrix2.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix2[i].append(int(row_elems[j]))
        mapReducer.execute(matrix1, matrix2 , mapper, reducer)
