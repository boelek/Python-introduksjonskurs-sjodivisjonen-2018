# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 22:40:34 2018

@author: boele
"""

# 03 read csv and find unique survey vessels...

# open csv file
f = open('fartoey_maaleoppdrag.csv', 'r')
data = f.read()
surveys_and_vessels = data.split('\n')

# print number of rows and show first 5 rows
print(len(surveys_and_vessels))
print(surveys_and_vessels[0:5])
print()

# remove header
surveys_and_vessels = surveys_and_vessels[1:]

#  create empty vessels list
vessels = []

# for each row extract second column and add to vessel list
for row in surveys_and_vessels:
    col = row.split(';')
    if len(col)>1:
        vessels.append(col[1])
 
# print first 5 ned rows
print(vessels[0:5])
print()

# create vessel_counts dictonary with vessel name as key and count as value
vessel_counts = {}
for item in vessels:
    if item in vessel_counts:
        vessel_counts[item] = vessel_counts[item] + 1
    else:
        vessel_counts[item] = 1
        
print(vessel_counts)
print('number of unique vessels: ' + str(len(vessel_counts)))

