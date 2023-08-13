# Check whether given no is prime no. or not
# Time Complexity is O(n)
n = int(input("Enter a no. to find if it's prime or not : "))
# if n == 1 or n < 0:
#     print("Non Prime No.")
# else:
#     i = 2
#     while(i < n):
#         if n%i == 0:
#             print("Non Prime No.")
#             break
#         i+=1
#     if(i == n):
#         print("Prime No.")

# **************************************************************************************************************************************

# Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of a smaller factor that has been already checked.
# Time Complexity is O(sqrt(n))
from math import sqrt
flag = 0
if n <= 1:
    print("Non Prime No.")
else:
    for x in range(2,int(sqrt(n))+1):
        if n%x == 0:
            flag = 1
            break
    if flag == 0:
        print("Prime No.")
    else:
        print("Non Prime No.")

# ************************************************************************************************************************************
# RECURSION
