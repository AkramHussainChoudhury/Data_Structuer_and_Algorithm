'''Given an array of integers A and an integer B. Find and return the maximum value of | s1 - s2 |

where s1 = sum of any subset of size B, s2 = sum of elements of A - sum of elemets of s1

Note |x| denotes the absolute value of x.


Input Format

The arguments given are the integer array A and integer B.
Output Format

Return the maximum value of | s1 - s2 |.
Constraints

1 <= B < length of the array <= 100000
1 <= A[i] <= 10^5
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 2
Output 1:
    9

Input 2:
    A = [5, 17, 100, 11]
    B = 3
Output 2:
    123
'''


def solve(A, B):
    A.sort()
    sum1=0
    sum2=0
    n=len(A)-1
    for i in range(B):
        sum1+=A[i]
        sum2+=A[n-i]

    totalsum=sum(A)
    sumrem1=totalsum - sum1
    sumrem2=totalsum - sum2
    return max(abs(sum1-sumrem1),abs(sum2-sumrem2))


