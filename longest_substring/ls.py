class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        elif len(s)==0:
            return 0
        ss = "" 
        maxLength = 0 
        i=0
        while i<len(s):
            loc=0
            for iAux,n in enumerate(ss):
                if n==s[i]:
                    loc=i-len(ss)+1
                    print(loc,i,iAux,ss) 
            if loc==0:
                ss+=s[i] 
            if (len(ss)>maxLength):
                maxLength=len(ss)  
            if (loc!=0): 
                ss=""  
                i=loc 
                loc=0
                continue
            i+=1
        return maxLength
                
             
            
if __name__=="__main__":   
    print("start") 
    s=Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))