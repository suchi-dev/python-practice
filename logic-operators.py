print(not True)
print(not 4 ==3)
x = 10
y = 20
if not y < x:
    print("It worked")


C = 10
D = 5
if C > 10 and D > 1:
    print("It worked!!")

if C >= 10 and D > 1:
    print("Condition met")

if not (C > 10 and D > 1):
    print("Not condition")

M = 5
N = -1
if M > 1 or N > 1:
    print("Or condition1 met")


N = 5
if not(M > 100 or N > 100):
    print("Or condition2 met")

C = 6
D = 2
if (C > 5 and D > 5) or (C > 1 and D > 1):
    print("Or - and condition met")