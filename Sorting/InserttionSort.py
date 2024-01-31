def InsertionSort(A):

    for i in range(1,len(A)):
        temp=A[i]
        j=i-1
        while(j>=0 and temp < A[j]):
            A[j+1]=A[j]
            j-=1

        A[j+1]=temp

    return A


A=[3,2,78,4,9,32]
print(InsertionSort(A))