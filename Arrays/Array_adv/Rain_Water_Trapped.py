'''
Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000



Input Format
First and only argument is the vector A



Output Format
Return one integer, the answer to the question



Example Input
Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output
Output 1:

1
Output 2:

0
'''


def trap(A):
    lmax=[0]*len(A)
    rmax=[0]*len(A)
    maxl=0
    maxr=0

    for i in range(len(A)):
        lmax[i]=maxl
        maxl=max(maxl,A[i])

    for j  in range(len(A)-1,-1,-1):
        maxr=max(maxr,A[j])
        rmax[j]=maxr


    total=0

    for i in range(len(A)):
        total+=max(min(lmax[i],rmax[i])-A[i],0)

    return total


A = [1, 2]
print(trap(A))