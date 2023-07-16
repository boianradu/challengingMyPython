from typing import List
import copy

class Solution:
    def minOrderedSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res=0
        if nums[len(nums)-1]>=target:
            return 1
        sum=0
        exists=False
        for nr in nums:
            sum+=nr
            res+=1
            if (sum>=target):
                exists=True
                break
        if exists:
            return res
        return 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==1:
            if nums[0]>=target:
                return 1
            return 0  
        local = copy.deepcopy(nums)
        local.sort(reverse=True)
        res=0
        if local[0]>=target:
            return 1 
        exists=False
        window=2
        while True:
            for i in range(0, len(nums)-window+1):
                localSum=0 
                for j in range(i, i+window):
                    localSum+=nums[j]
                if localSum>=target:
                    res=window 
                    exists=True
                    break
            if exists:
                break
            if window==len(nums):
                break
            window+=1
                
        if exists:
            return res
        return 0
        

if __name__=="__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    s=Solution()
    print(s.minOrderedSubArrayLen(target, copy.deepcopy(nums)))
    print(s.minSubArrayLen(target, copy.deepcopy(nums)))
    target = 4
    nums = [1,4,4]
    print(s.minOrderedSubArrayLen(target, copy.deepcopy(nums)))
    print(s.minSubArrayLen(target, copy.deepcopy(nums)))
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(s.minOrderedSubArrayLen(target, copy.deepcopy(nums)))
    print(s.minSubArrayLen(target, copy.deepcopy(nums)))
    target=213
    nums=[12,28,83,4,25,26,25,2,25,25,25,12]
    print(s.minOrderedSubArrayLen(target, copy.deepcopy(nums)))
    print(s.minSubArrayLen(target, copy.deepcopy(nums)))
    target=15
    nums=[1,2,3,4,5]
    print(s.minOrderedSubArrayLen(target, copy.deepcopy(nums)))
    print(s.minSubArrayLen(target, copy.deepcopy(nums)))