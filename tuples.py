our_tuple = 1,2,3,"A", "B", "C"
print(type(our_tuple))
my_tuple = ("A", "B", "C", "D", 4,5,6)
print(my_tuple[0:3])
#tuples are immutable
our_list = [1,2,3,4,5,6]
our_list[2] = 100
print(our_list)

# my_tuple[2]= 100
A = [1,2,3,4,5]
print(tuple(A))
A = tuple(A)
print(type(A))
(A,B,C) = 1,2,3
print(A)
D,E,F = ['d', 'e', 'f']
print(D)
X,Y,Z = "pot"
print(Y)