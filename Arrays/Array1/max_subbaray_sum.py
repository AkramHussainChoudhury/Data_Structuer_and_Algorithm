'''Find the maximum sum of contiguous non-empty subarray within an array A of length N.



Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000



Input Format
The first and the only argument contains an integer array, A.



Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.



Example Input
Input 1:

 A = [1, 2, 3, 4, -10]
Input 2:

 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


Example Output
Output 1:

 10
Output 2:

 6 '''
from math import inf


def maxSubArray(A):
    maxsum = float(-inf)
    if len(A)==1:
        return A[0]

    sum=0
    for i in range(len(A)):
        sum=sum+A[i]
        if sum>maxsum:
            maxsum=sum
        if sum<0:
            sum=0



    return maxsum


A=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(A))