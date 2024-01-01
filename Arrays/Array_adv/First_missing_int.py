'''
Given an unsorted integer array, A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.



Problem Constraints
1 <= N <= 1000000

-109 <= A[i] <= 109



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the first missing positive integer.



Example Input
Input 1:

[1, 2, 0]
Input 2:

[3, 4, -1, 1]
Input 3:

[-8, -7, -6]


Example Output
Output 1:

3
Output 2:

2
Output 3:

1
'''


def firstMissingPositive(A):
    N=len(A)
    for i in range(N):
        while A[i]<N and A[i]>0 and A[i]!=A[A[i]-1]:
            temp=A[i]
            A[i]=A[temp-1]
            A[temp-1]=temp
            print(A)

    c=1
    print(A)
    for i in range(N):
        if A[i]==c:
            c+=1
        else:
            break
    return c



A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20]

print(firstMissingPositive(A))