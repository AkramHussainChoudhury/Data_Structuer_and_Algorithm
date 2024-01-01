'''
You are given an array of N integers, A1, A2, .... AN.

Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.



Problem Constraints
1 <= N <= 100000

-109 <= A[i] <= 109



Input Format
First argument is an integer array A of size N.



Output Format
Return an integer denoting the maximum value of f(i, j).



Example Input
Input 1:

A = [1, 3, -1]
Input 2:


A = [2]


Example Output
Output 1:

5
Output 2:

0
'''


def maxArr(A):
    maxsum=float('-inf')
    minsum=float('inf')
    maxdiff= float('-inf')
    mindiff=float('inf')
    for i in range(len(A)):
        # max((A[i]-i)-(A[j]-j),(A[i]+i)-(A[j]+j))
        maxsum = max(maxsum,A[i]+i)
        minsum = min(minsum,A[i]+i)
        maxdiff=max(maxdiff,A[i]-i)
        mindiff=min(mindiff,A[i]-i)

    return max((maxsum-minsum),(maxdiff-mindiff))

