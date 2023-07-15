# Lists
# Python Lists are ordered collections of data just like arrays in other programming languages. It allows different types of elements in the list.

List = [1, 2, 3, "GFG", 2.3]
print(List)
print(List[3])
print(List[3][0])

print(List[-2])


# list of integers
integer_list = [1, 2, 3, 1, 8, 1]
# max(), min()
print(max(integer_list)) # 8
print(min(integer_list)) # 1
# count(), index()
print(integer_list.index(3)) # 2
print(integer_list.index(1)) # 0
print(integer_list.count(1)) # 3
print( integer_list.count(88)) # 0


# extend(other_list): Adds the elements in other_list to the end of the original list;

string_list = ['data', 'science']
# extend()
integer_list.extend(string_list)#[1, 2, 3, 'data', 'science']
print(integer_list)
integer_list.extend('rocks') #[1, 2, 3, 'data', 'science', 'r', 'o', 'c', 'k', 's']
print(integer_list) 


# insert(index, element): Inserts a single element at the given index and shifts the elements after to the right.


# insert()
string_list.insert(1,'-') #['data', '-', 'science']
print(string_list)
string_list.insert(3,'rocks') #['data', '-', 'science', 'rocks']
print(string_list)

onlyIntegers=[3,5,-7,2,1,0,66]
# sort  
onlyIntegers.sort()
print(onlyIntegers)
onlyIntegers.sort(reverse=True)
print(onlyIntegers)


# reverse() — Reverse simply reverse the list order. This function does not return a new list.
# remove(element): Finds the first instance of the given element and removes it. Throws ValueError, if the given element is not present.
# pop(index): Removes and returns the element at the given index. Removes and returns the last element if the index is no provided.


# List Comprehensions
# new_list = [expression for member in iterable(if conditional)]

comprehensionIntegerList = [x for x in range(10) if x % 2 == 0 and x>3]
print(comprehensionIntegerList) #[0, 10, 20, 30]