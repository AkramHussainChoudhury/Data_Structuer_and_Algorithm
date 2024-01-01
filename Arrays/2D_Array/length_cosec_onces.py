'''Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format

The only argument given is string A.
Output Format

Return the length of the longest consecutive 1’s that can be achieved.
Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7'''


def solve(A):
    totalones=0
    for i in A:
        if i=="1":
            totalones+=1

    left=[]
    rigt=[0 for i in A]
    count=0
    for i in range(len(A)):
        if A[i]=="1":
            count+=1
        else:
            count=0

        left.append(count)
    count=0

    print(left)

    for i in range(len(A)-1,-1,-1):
        if A[i]=="1":
            count+=1
        else:
            count=0
        rigt[i]=count

    print(rigt)
    maxcount=left[0]
    for i in range(1,len(A)-1):
        total=left[i-1]+rigt[i+1]
        if total==totalones:
            maxcount=max(maxcount,total)
        if total+1<=totalones:
            maxcount=max(maxcount,total+1)


    return maxcount






A = "0111110110"
A="111011101"
print(solve(A))