'''
Problem Description
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

Elements which are appearing twice are adjacent to each other.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints
1 <= |A| <= 100000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the single element that appears only once.



Example Input
Input 1:

A = [1, 1, 7]
Input 2:

A = [2, 3, 3]


Example Output
Output 1:

 7
Output 2:

 2

'''

def solve(A):
    if len(A)==1:
        return A[0]

    if A[0]!=A[1]:
        return A[0]
    n=len(A)
    if A[n-1]!=A[n-2]:
        return A[n-1]

    l=1
    r=n-2

    while(l<=r):
        mid=(l+r)//2
        if A[mid]!=A[mid-1] and A[mid]!=A[mid+1]:
            return A[mid]
        elif (mid%2==0 and A[mid]==A[mid+1]) or (mid%2==1 and A[mid]==A[mid-1]):
            l=mid+1
        else:
            r=mid-1


