n = int(input("Enter the no. whose Factorial is needed : "))
# Using Recursion
def fact(x):
    if x == 1:
        return x
    else:
        return x*fact(x-1)
print(fact(n))

# ********************************************************************************************************************************

# import math
# print("Factorial of 10 : ",math.factorial(10))