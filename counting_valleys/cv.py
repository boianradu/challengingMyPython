import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here 
    height=0
    totalValleys=0
    i=0
    while i < steps:
      if path[i]=='D':
        height-=1
      elif path[i]=='U':
        height+=1
      if height==-1 and path[i]=='D':
        totalValleys+=1
      i+=1
    return totalValleys

if __name__ == '__main__':
  steps=8
  path = "DDUUUUDD"
  print(countingValleys(steps, path))