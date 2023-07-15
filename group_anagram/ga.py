from typing import List
class Solution:
    def areAnagrams(self, s1: str, s2) ->bool:  
        if (len(s1)!=len(s2)):
            return False
        c1=0
        c2=0
        for i, c in enumerate (s1):
            c1+=ord(s1[i])
        for i, c in enumerate (s2):
            c2+=ord(s2[i]) 
        if (c1==c2):
            return True
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i=0
        if strs==[""]:
            return [[""]]
        rezultGrup=[]
        while i<len(strs): 
            if strs[i]=="":
                i+=1
                continue
            anagramGroup = []
            anagramGroup.append(strs[i])
            j=i+1
            while j<len(strs):
                if self.areAnagrams(strs[i], strs[j]):
                    anagramGroup.append(strs[j]) 
                    strs[j]=""
                j+=1
            i+=1
            if (anagramGroup!=[]): 
                rezultGrup.append(anagramGroup)
        return rezultGrup
    
if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    s=Solution()
    print(s.groupAnagrams(strs))