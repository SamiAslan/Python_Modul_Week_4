#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d_left=0
    d_right=0
    for i in range(0, n):
        d_left= d_left + arr[i][i]
        d_right= d_right + arr[i][n-i-1]
    return abs(d_left-d_right)

#--------------------------------------------------

def diagonalDifference(arr):
diag1 = 0 diag2 = 0

for i in range(n):
    row = arr[i]
    nums = [int(num) for num in row]
    diag1 += nums[i]
    diag2 += nums[(-1*(i+1))]

return abs(diag1 - diag2)


#--------------------------------------------------


def diagonalDifference(arr):

    n = len(arr)
    left_diag_sum = sum(arr[i][i] for i in range(n))
    right_diag_sum = sum(arr[i][n - i - 1] for i in range(n))
    return abs(left_diag_sum - right_diag_sum)


#--------------------------------------------------
def diagonalDifference(arr):
    diags = [0, 0]
    for i in range(len(arr)):
        diags[0] += arr[i][i]
        diags[1] += arr[i][-(i+1)]
    return abs(diags[0] - diags[1])

#--------------------------------------------------
def diagonalDifference(arr):
    p,s = 0,0
    n = len(arr)
    for i in range(0,n):
        p += arr[i][i]
        s += arr[i][n-i-1]
    
    return abs(p-s)

#--------------------------------------------------

