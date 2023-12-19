'''Problem Description
Given an integer array A of size N and an integer B, you have to print the same array after rotating it B times towards the right.


Problem Constraints
1 <= N <= 106
1 <= A[i] <=108
1 <= B <= 109


Input Format
There are 2 lines in the input

Line 1: The first number is the size N of the array A. Then N numbers follow which indicate the elements in the array A.

Line 2: A single integer B.


Output Format
Print array A after rotating it B times towards the right.

'''


def solve(A,B):
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    B=B%len(A)
    C=A[::-1]
    print(C)
    k=0
    l=B-1
    while(k<l):
        C[k],C[l]=C[l],C[k]
        k+=1
        l-=1
    m=B
    n=len(A)-1
    while(m<n):
        C[m],C[n]=C[m],C[n]
        m+=1
        n-=1

    print(C)

    return C

if __name__ == '__main__':
    A = [ 1, 2, 3, 4, 5 ]
    B = 3
    solve(A,B)