'''
Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from array A.



Problem Constraints
1 <= N <= 106

-106 <= A[i] <= 106



Input Format
First argument is an integer array A of size N.



Output Format
Return an integer denoting the length of the longest set of consecutive elements from the array A.



Example Input
Input 1:

A = [100, 4, 200, 1, 3, 2]
Input 2:

A = [2, 1]


Example Output
Output 1:

 4
Output 2:

 2

'''

def longestConsecutive(A):
    s=set()
    for i in A:
        s.add(i)

    res=0
    for i in range(len(A)):
        if A[i]-1 in s:
            continue

        cnt=0
        j=A[i]
        while j in s:
            j+=1
            cnt+=1
        res=max(res,cnt)

    return res
