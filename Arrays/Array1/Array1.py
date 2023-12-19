'''Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.



Problem Constraints
1 <= A.size() <= 104

1 <= A[i] <= 109

1 <= B <= 109



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return 1 if good pair exist otherwise return 0.'''

def solve(A, B):
    A.sort()
    count=0
    i=0
    j=len(A)-1
    while i<j:
        if(A[i]+A[j]==B):
            count+=1
            break
        if A[i] + A[j]>B:
            j-=1
        else:
            i+=1


    if count>=1:
        return 1
    else:
        return 0;



A=[1,2,3,4]
B=7


print(solve(A,B))