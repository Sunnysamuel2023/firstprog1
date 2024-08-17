tuple1 = (10, 23, 0, "Sunny", True)
print(tuple1[1])  # tuple indexing
print(type(tuple1))  # to know class of data
# tuples are immutable
# to create tuple we have to put comma in the end of single character tuple = (10, )
# duplicates items are allowed
# tuples are arranged in ordered manner
print(len(tuple1))  # to find number of elements in tuple
tuple2 = (1, 4, "Christina")
# tuple3 = (tuple1, tuple2)  # nested tuple
tuple3 = tuple1 + tuple2  # Concatenate the two tuples
# print(min(tuple3))  # to find minimum value
# It will not support if it is a mixed list
# print(max(tuple3))  # to find minimum value
tuple1.count(10)  # to count occurances of particular item/ element
list = [1, 2, 34, 32]
print(tuple(list))  # converts list into tuple
# * multiplication of tuple will
tuple4 = ("Jenny", )*5
print(tuple4)
