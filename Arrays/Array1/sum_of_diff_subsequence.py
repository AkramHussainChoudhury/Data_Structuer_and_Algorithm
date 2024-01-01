'''
Given an integer array, A of size N.
You have to find all possible non-empty subsequences of the array of numbers and then,
for each subsequence, find the difference between the largest and smallest number in that subsequence.
Then add up all the differences to get the number.

As the number may be large, output the number modulo 1e9 + 7 (1000000007).

NOTE: Subsequence can be non-contiguous.



Problem Constraints
1 <= N <= 10000

1<= A[i] <=1000



Input Format
First argument is an integer array A.



Output Format
Return an integer denoting the output.



Example Input
Input 1:

A = [1, 2]
Input 2:

A = [3, 5, 10]


Example Output
Output 1:

 1
Output 2:

 21
'''

def solve(A):
    A.sort()
    maxsum=0
    minsum=0
    n=len(A)
    for i in range(len(A)):
        maxsum = (maxsum + A[i]*(2**i))%1000000007
        minsum= (minsum + A[i]*(2**(n-i-1)))%1000000007

    return (maxsum-minsum)%1000000007
