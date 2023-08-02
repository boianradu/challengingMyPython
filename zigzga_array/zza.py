#User function Template for python3
import copy

class Solution:
    def getMidElement(self, arrL, arrR):
        if (len(arr)==1):
            return arr
        arr.sort()
        return arr[int(len(arr)/2)]
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        print("ZZ:", arr, n, self.getMidElement(copy.deepcopy(arr)))


if __name__=="__main__":
    print("Something")
    arr = [4, 3, 7, 8, 6, 2, 1]
    n=7
    s=Solution() 
    print(s.zigZag(arr,n))