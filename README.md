# Learning MapReduce with Examples

Here's a quick introduction to the idea of splitting tasks into a MapReduce model. 
The four important functions involved in MapReduce are:

1. Map (the mapper function)  
2. EmitIntermediate(the intermediate key,value pairs emitted by the mapper functions)  
3. Reduce (the reducer function)  
4. Emit (the final output, after summarization from the Reduce functions)

The usage of MapReduce is demonstrated with 3 distinct examples.

1. Calculating number of friends for each person based on a list of friendships between different people
2. Using MapReduce for natural join of records from 2 database tables; employee and department
3. Matrix Multiplication with MapReduce

For complete understanding on how MapReduce works, please examine the implementation of mapper() and reducer() functions in each of the solutions.

## Pre-requisites

Python (All programs were tested with Python 2.7.10 installed in Ubuntu 15)

## Running the Examples

1. Number of Friends -> `python no_of_friends_map_reduce.py < inputs/friends.txt`
2. Relational Join -> `python relational_join_map_reduce.py < inputs/relations.txt`
3. Matrix Multiplication -> `python matrix_multiplication_map_reduce.py < inputs/matrices.txt`
