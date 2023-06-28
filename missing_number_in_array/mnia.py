#User function Template for python3


class Solution:
    def missingNumber(self,array,n): 
        # code here
        if n==2 and array[0]==1:
            return 2
        if n==2 and array[0]==2:
            return 1
        array.sort() 
        i=0
        while i<n-1:
            if array[i]!=i+1:
                return i+1
            i+=1
        return n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

N = 10
N = 5
A = [6,1,2,8,3,4,7,10,5]
A = [1,2,3,4]
s=Solution().missingNumber(A,N)
print(s)
# } Driver Code Ends