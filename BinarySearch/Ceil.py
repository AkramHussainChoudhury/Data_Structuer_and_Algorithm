'''Problem Description

You are given a sorted array A of size N and a target value B.
Your task is to find the index (0-based indexing) of the target value in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater than equal to B.
If the target value is not found and least number greater than equal to target is also not present, return the length of array (i.e. the position where target can be placed)
Your solution should have a time complexity of O(log(N)).


Problem Constraints

1 <= N <= 105
1 <= A[i] <= 105
1 <= B <= 105



Input Format

The first argument is an integer array A of size N.
The second argument is an integer B.



Output Format

Return an integer denoting the index of target value.



Example Input

Input 1:

A = [1, 3, 5, 6]
B = 5
Input 2:

A = [1, 4, 9]
B = 3


Example Output

Output 1:

2
Output 2:

1


Example Explanation

Explanation 1:

The target value is present at index 2.
Explanation 2:

The target value should be inserted at index 1.

'''

def searchInsert(A, B):
    ans=len(A)
    l=0
    r=len(A)-1

    while(l<=r):
        mid=(l+r)//2
        if A[mid] == B:
            return mid
        elif A[mid] > B:
            ans=mid
            r=mid-1
        else:
            l=mid+1

    return ans

