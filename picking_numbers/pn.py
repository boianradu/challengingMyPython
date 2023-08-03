 
def picking_numbers_subarray(a): 
    print("Array:", a)
    maxC=0
    finalArray=[]

    for i, pivot in enumerate(a[0:len(a)-2]):
        counter=1
        localArray=[]
        localArray.append(pivot)
        direction=0 
        for el in a[i+1:]:
            if direction==0:
                if pivot-el==1:
                    direction=1
                elif pivot-el==-1:
                    direction=-1
            if pivot-el == direction or pivot-el==0:
                localArray.append(el)
                counter+=1
            else: 
                break

        if counter>=maxC:
            maxC=counter
            finalArray=localArray
    print("Max counter:", maxC, finalArray)
    return maxC


def picking_numbers_any(a):  
    maxC=0
    finalArray=[]

    for i, pivot in enumerate(a[0:len(a)-1]):
        for direction in [-1,1]:
            counter=0
            localArray=[]
            localArray.append(pivot) 
            for el in a[i+1:]: 
                if pivot-el == direction or pivot-el==0: 
                    localArray.append(el)
                    counter+=1 

            if counter>=maxC:
                maxC=counter
                finalArray=localArray
    print("Max counter:", maxC, finalArray)
    return maxC
        

if __name__ == '__main__': 
    a = [1,1,2,2,4,4,5,5,5]

    result = picking_numbers_subarray(a) 
    result = picking_numbers_any(a) 

    a=[4, 6, 5, 3, 3, 1]
    result = picking_numbers_subarray(a) 
    result = picking_numbers_any(a) 

    a=[4, 6, 5, 3, 3, 1]
    result = picking_numbers_subarray(a) 
    result = picking_numbers_any(a) 

    a=[1, 2, 2, 3, 1, 2]
    result = picking_numbers_subarray(a) 
    result = picking_numbers_any(a) 
