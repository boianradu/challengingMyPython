#User function template for Python

global arr
class Solution:	
  def chunker(self, seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size)) 
  def reverseInGroups(self, arr, N, K):  
    newArr=[]
    for x in self.chunker(list(arr),K):  
      for i, e in reversed(list(enumerate(x))):
        newArr.append(e)  
        print(e,end=" ") 
    print()
    arr=set(newArr)
    return arr
 

import math
def main():
    N = 5
    K = 3
    arr = {1,2,3,4,5}
    ob = Solution()
    ob.reverseInGroups(arr,N,K)
    for i in arr:
        print(i,end=" ")
    print()

if __name__=="__main__":
    main()
 
  