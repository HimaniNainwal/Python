A = [1,2,1,2,2,1,3,1,3,2,1,3,4]
A.sort()
# print(A)
dict = {}
i = 0
while(i<len(A)):
    count = 1
    j = i+1
    while(j<len(A)):
        if A[i]!=A[j]:
            break
        count+=1
        j=j+1
    dict[A[i]]=count
    i = j

print(dict)

# ************************************************************************************************************************************

# from collections import Counter
# A = [1,2,1,2,2,1,3,1,3,2,1,3,4]
# B = Counter(A)
# print(B)