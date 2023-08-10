# Find 2 no. whose sum is 10
A = [5,2,5,3,4,7,2,6,8]

dict = {}
# HERE TIME COMPLEXITY IS O(n2) 
i = 0
while(i<len(A)):
    j = i + 1
    while(j<len(A)):
        if A[i]+A[j] == 10:
            dict[i+1] = (A[i],A[j])
        j = j + 1
    i = i + 1

print(dict)

# *************************************************************************************************************************************

# HERE TIME COMPLEXITY IS O(n)
# l = []
# sum = 10
# while A:
#     n = A.pop()
#     diff = sum - n
#     if diff in A:
#         l.append((n,diff))  # l.append(n,diff) TypeError: list.append() takes exactly one argument (2 given)
# # you can use reverse like this l.reverse()
# l.reverse()
# print(l)