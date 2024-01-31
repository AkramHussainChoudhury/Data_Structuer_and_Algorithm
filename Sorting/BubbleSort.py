def BubbleSort(A):
    n=len(A)
    for i in range(n):
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]

    return  A


A=[8,2,1,4,9]
print(BubbleSort(A))