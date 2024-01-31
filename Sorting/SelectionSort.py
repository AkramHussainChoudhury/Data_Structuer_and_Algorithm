


def SelectionSort(A):
    N=len(A)-1

    for i in range(len(A)):
        max=A[0]
        c=0
        for j in range(len(A)-i):
            if A[j]>max:
                max=A[j]
                c=j
        A[j],A[c]=A[c],A[j]
    return A



A=[122,43,111,578,2,411,897]

print(SelectionSort(A))
