# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:40:34 2018

@author: boele
"""

# 04 functions...

# define function

def xyz_to_ned(in_xyz):
    #  create empty ned list
    out_ned = []

    # for each row convert xyz to ned and append to ned list
    for row in in_xyz:
        values = row.split(' ')
        out_ned.append([values[1], values[0], '-'+values[2]])
    return out_ned

# start program 
    
# open xyz file
f = open('test.xyz', 'r')
data = f.read()
xyz = data.split('\n')

# print first 5 rows
print(xyz[0:5])
print()

# call function
ned = xyz_to_ned(xyz)

#print first 5 ned rows
print(ned[0:5])


