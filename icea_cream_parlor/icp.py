import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    # Write your code here 
    i=0
    while i < len(cost)-1:
      j=i+1
      while j < len(cost):
        if cost[i]+cost[j]==money:
          print(i+1,+j+1)
          return
        j+=1
      i+=1
          

if __name__ == '__main__': 
  cost = [2,1,3,5,6]
  money=5
  
  cost=[1,4,5,3,2]
  money=5
  print(whatFlavors(cost, money))
