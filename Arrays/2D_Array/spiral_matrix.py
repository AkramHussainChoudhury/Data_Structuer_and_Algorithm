'''Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.



Problem Constraints
1 <= A <= 1000



Input Format
First and only argument is integer A


Output Format
Return a 2-D matrix which consists of the elements added in spiral order.



Example Input
Input 1:

1
Input 2:

2
Input 3:

5


Example Output
Output 1:

[ [1] ]
Output 2:

[ [1, 2],
  [4, 3] ]
Output 2:

[ [1,   2,  3,  4, 5],
  [16, 17, 18, 19, 6],
  [15, 24, 25, 20, 7],
  [14, 23, 22, 21, 8],
  [13, 12, 11, 10, 9] ]'''


def generateMatrix(A):
    T=0
    L=0
    B=A-1
    R=A-1
    k=1
    C=[[0]*A for i in range(A)]
    print(C)
    k=1

    while(L<R and T<B):
        for j in range(L,R+1):
            C[T][j]=k
            k+=1

        T=T+1
        for j in range(T,B+1):
            C[j][R]=k
            k+=1
        R-=1
        for j in range(R,L-1,-1):
            C[B][j]=k
            k+=1

        B-=1
        for j in range(B,T-1,-1):
            C[j][L]=k
            k+=1
        L+=1

    return C

A=[[1,2,3,4,5],
 [6,7,8,9,10],
 [11,12,13,14,15],
 [16,17,18,19,20],
 [21,22,23,24,25]]


print(generateMatrix(5))
