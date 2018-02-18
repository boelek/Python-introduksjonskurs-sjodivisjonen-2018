# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 06:40:34 2018

@author: boele
"""

# 02, reading text files and converting from NED to XYZ

# open xyz file
f = open('test.xyz', 'r')
data = f.read()
xyz = data.split('\n')

# print first 5 rows
print(xyz[0:5])

#  create empty ned list
ned = []

# for each row convert xyz to ned and append to ned list
for row in xyz:
    values = row.split(' ')
    ned.append([values[1], values[0], '-'+values[2]])

#print first 5 ned rows
print(ned[0:5])


# print depth at row 15
print(ned[16][2])
