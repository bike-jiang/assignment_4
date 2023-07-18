# CMPT 145 Course material
# Copyright (C) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#    SOme functions to test.


def newtonraphson(x):
    """ Add the doc-string! """
    root = 1
    while abs(x - root * root) > 0.00001:
        root = (x/root + root) / 2.0
    return root
 
 
def gcd(a, b):
    """ Add the doc-string! """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)


def read_triangle(filename):
    """ Add the doc-string! """
    file = open(filename)
    triangle = []
    for line in file:
        line = line.rstrip().split()
        line = [int(d) for d in line]
        triangle.append(line)
    file.close()
    size = triangle[0][0]
    triangle = triangle[1:]
    return (size, triangle)

def remdup(alist):
    """ Add the doc-string! """
    alist.reverse()
    for i in range(len(alist)-1):
        while alist[i] in alist[i+1:]:
            del alist[i]
    alist.reverse()

