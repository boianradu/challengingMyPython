
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        rez=[]
        nums.sort()
        while i+2<len(nums):
            j=i+1
            while j<len(nums):
                k=j+1
                while k<len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ll=[nums[i], nums[j] ,nums[k]]
                        # print(nums[i], nums[j] ,nums[k])
                        ll.sort()
                        rez.append(ll) if ll not in rez else rez
                    k+=1
                j+=1
            i+=1
        # rez = [i for n, i in enumerate(rez) if i not in rez[:n]] 
        # rez=set(rez)
        return rez 
            


def main():
    nums = [-1,0,1,2,-1,-4]
    x = Solution()
    print(x.threeSum(nums))


if __name__ == "__main__":
    main()