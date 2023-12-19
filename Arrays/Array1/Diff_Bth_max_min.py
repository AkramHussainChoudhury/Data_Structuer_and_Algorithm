'''Given an array of integers A and an integer B, find and return the difference of B'th max element and B'th min element of the array A.


Input Format

The first argument given is the integer array A.
The second argument given is integer B.
Output Format

Return the value of B'th max element of A - B'th min element of A.
Constraints

1 <= B <= length of the array <= 100000
-10^9 <= A[i] <= 10^9
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 2
Output 1:
    2   (4 - 2 = 2)

Input 2:
    A = [5, 17, 100, 11]
    B = 1
Output 2:
    95  (100 - 5 = 95)'''


def solve(A, B):
    A.sort()
    l=len(A)
    print(l)
    diff= A[l-B]-A[B-1]
    return diff


A=[34,7,96,37,12,13,22,86,17,78,95,61,42,1,42,58,98,78,92,85,10,97]
B=22

print(solve(A,B))
