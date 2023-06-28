# User function Template for python3

import math


class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        max = arr[0]
        i = 0
        while i < N:
            print("i;", i)
            j = i + 1
            per = 1
            while per + j-1 < N:
                localMax = 0
                marj = j
                it = per
                while it > 0 and marj < N:
                    print("mars:", marj, arr[marj])
                    localMax += arr[marj]
                    marj += 1
                    it -= 1
                if localMax > max:
                    max = localMax
                    print("max", max)
                per += 1
            print("next:", per,i,j, max)
            i += 1
        return max


def main():
    N = 5
    # N = 9
    Arr = [1, 2, 3, -2, 5]
    # Arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ob = Solution()
    print(ob.maxSubArraySum(Arr, N))


if __name__ == "__main__":
    main()
