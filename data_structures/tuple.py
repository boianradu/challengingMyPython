# A tuple is essentially a static array. In other words, once a tuple is created, you cannot modify and resize it.

# What is the difference between tuple and list?
# The major difference between a Python tuple and the list is that list is mutable which means it can be changed and we can modify its values. whereas a tuple is immutable, hence it can not be changed.
# That’s why they perform different operations and functions.

my_tuple = (1, 2, 3)
print(my_tuple[0])

# my_tuple[0] = 'a' # ERROR

# concatenation
t1=(12, 34, 56)
t2=(78, 90)
print(t1+t2)

# repetition operator
t1=(12, 34, 56)
print( t1*3)


# For comparison, two tuples must-have elements of comparable types, otherwise, you will get an error.

#membership operator
t1=(12, 34, 56, 78, 90)
#membership operator
print(56 in t1)
print(12 not in t1)


# min max index count functions
t1 =( 12, 34, 56, 78,35, 34, 23 ,45 )
print( max(t1))
print( min(t1))
print(t1.index(34))
print(t1.count(34)) # counts how many elements with that value it has


#list to tuple
list1=[12,34,56]
t1= tuple(list1)
print(t1, type(t1), type(list1))