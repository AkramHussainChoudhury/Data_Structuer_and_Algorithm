'''Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105
Sum of all elements of A <= 109


Input Format
First argument contains an array A of integers of size N


Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Example Input
Input 1:
A = [2, 1, 6, 4]
Input 2:

A = [1, 1, 1]


Example Output
Output 1:
1
Output 2:

3


Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
Therefore, the required output is 1.
Explanation 2:

Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Therefore, the required output is 3.'''


def solve(A):
    evenPS=[0]*len(A)
    oddPS=[0]*len(A)
    for i in range(len(A)):
        if i%2==0:
            if i==0:
                evenPS[0]=A[0]
            else:
                evenPS[i]=evenPS[i-1]+A[i]
                oddPS[i]=oddPS[i-1]
        else:
            oddPS[i]=oddPS[i-1]+A[i]
            evenPS[i]=evenPS[i-1]

    count=0
    l=len(A)-1
    for i in range(len(A)):
        if i==0:
            e=oddPS[l]-oddPS[i]
            o=evenPS[l]-evenPS[i]
        elif i==l:
            e=evenPS[i-1]
            o=oddPS[i-1]

        else:
            e=evenPS[i-1]+oddPS[l]-oddPS[i]
            o=oddPS[i-1]+evenPS[l]-evenPS[i]

        if e==o:
            count+=1

    return count


