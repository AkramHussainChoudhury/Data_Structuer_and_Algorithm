'''Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).



Problem Constraints
1 <= length of the array <= 105

1 <= A[i] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the number of inversions of A modulo (109 + 7).



Example Input
Input 1:

A = [1, 3, 2]
Input 2:

A = [3, 4, 1, 2]


Example Output
Output 1:

1
Output 2:

4
'''


def solve(A):
    global count
    count=0
    def merge(s,mid,e):
        global count
        s1=s
        e1=mid
        s2=mid+1
        e2=e
        i=0
        j=0
        ind=s1
        Arr1=A[s1:e1+1]
        Arr2=A[s2:e2+1]
        N1=len(Arr1)
        N2=len(Arr2)

        while(i<N1 and j <N2):
            if Arr1[i]<=Arr2[j]:
                A[ind]=Arr1[i]
                i+=1
            else:
                A[ind]=Arr2[j]
                j+=1
                count=(count+N1-i)%1000000007
            ind+=1

        while(i<N1):
            A[ind]=Arr1[i]
            i+=1
            ind+=1
        while(j<N2):
            A[ind]=Arr2[j]
            j+=1
            ind+=1


    def mergeSort(s,e):
        print(s,e)
        if s==e:
            return
        print("seconf",s,e)
        mid=(s+e)//2
        mergeSort(s,mid)
        mergeSort(mid+1,e)
        merge(s,mid,e)

    mergeSort(0,len(A)-1)
    return A

A = [3, 4, 1, 2]
print(solve(A))