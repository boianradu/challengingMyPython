from typing import List
import copy

def getDivisors(nr)->List[int]:
    finalLlist = []
    n=int(nr/2)
    while n>0:
        if nr%n==0:
            finalLlist.append(n)
        n-=1
    return finalLlist

def maxProd(arr, n):
    divizors = getDivisors(n)
    maxProd=1
    n1=0
    n2=0
    arr.sort(reverse=True)
    for i,x in enumerate(arr):
        auxProd=1 
        n1Loc=0 
        if x%n==0:
            if x==arr[0]:
                n1=x 
                n2=arr[1]
                print("Setting loc 2:", n1,n2)
            else:
                n1=x
                n2=arr[0]
                print("Setting loc 1:", n1,n2)
            break
        else:
            okD=False
            for d in divizors:
                if x%d==0:
                    okD=True 
                    break
            if okD==False:
                continue    
            if n1Loc==0:
                n1Loc=x 
            for x2 in copy.deepcopy(arr[i+1:]): 
                if (n1Loc*x2) % n==0:
                    auxProd=n1Loc*x2
                    if auxProd>maxProd:
                        maxProd=auxProd 
                        n1=x
                        n2=x2
                    break

    print("Result is:", n1,n2, n1*n2)


n=15
arr=[7,8,3,6,12,5,10, 99]
print(getDivisors(n))
maxProd(arr,n)