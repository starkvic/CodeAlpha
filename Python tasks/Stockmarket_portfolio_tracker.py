stocks_list = {}
print(type(stocks_list))
"""
file_path = "stocks.txt" #This is the storage of the file that is used to store the list of stocks
with open(file_path,'r') as data:
#the with statement allows the execution and assigning of variables in a special way
#print(type(stocks)) #confirming that the type is dictionary
    line = data.readlines()
    print(len(line))
    print(line)
"""
import csv
import os
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir,'stocks.csv')
print(base_dir)
with open('stocks.csv') as data:
    reader = csv.reader(data,delimiter=',')
print(type(reader))