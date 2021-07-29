A = [1,2,3,4,5,6]
A = A + [9]
print(A)
A = A + ["BCD"]
print(A)
A = A + list("XYZ")
print(A)
A = A + list(str(908))
print(A)
A = A + list("Suchitra")
print(A)
A = A + [[1,4,2,3]]
print(A[-1])
A.append([10,11, 12])
print(A)
X = [1,2,3,4,5]
X = X.append(10)
print(X)
print(type(X))

B = [1,2,3,4,5,6]
B.insert(2, 15)
print(B)
B.insert(2, [10,20,30])
print(B)