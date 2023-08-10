A = [10,2,5,4,6,1,8,0]

# HERE TIME COMPLEXITY IS O(n^2)
for i in range(len(A)-1):    # range() method can't take list as an input instead take len(A), also range(0,stop(not included),1) by default.
    for j in range(len(A)-1):    # Without -1 in len(A)-1 out of range error can be avoided
        if A[j]>A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]

print(A)