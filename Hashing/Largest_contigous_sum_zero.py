'''Largest Continuous Sequence Zero Sum
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints is now penalty free
Use Hint
Problem Description
Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.



Problem Constraints
1 <= N <= 106

-107 <= A[i] <= 107



Input Format
Single argument which is an integer array A.



Output Format
Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.



Example Input
A = [1,2,-2,4,-4]


Example Output
[2,-2,4,-4]


Example Explanation
[2,-2,4,-4] is the longest sequence with total sum of zero.'''

def lszero(A):
    ps=[]
    currsum=0
    for i in A:
        currsum+=i
        ps.append(currsum)
    print(ps)
    maxseq=-1
    frestart={0:-1}
    freend={}
    for i in range(len(ps)):
        if ps[i]==0:
            maxseq=max(maxseq,i)
        if ps[i] not in frestart:
            frestart[ps[i]]=i
        else:
            freend[ps[i]]=i
    print(frestart)
    print("freend ",freend)
    maxstart=0
    maxend=0
    maxlength=0

    for i in ps:
        if i in freend:
            length=freend[i]-frestart[i]
            print("lenght " , length)
            if length>maxlength:
                maxlength=length
                maxstart=frestart[i]
                maxend=freend[i]
    print("maxstart",maxstart)
    print("maxend ",maxend)

    if maxlength<= maxseq and maxseq!=-1:
        return A[:maxseq+1]
    else:
        print("here")
        return A[maxstart+1:maxend+1]


A = [1,2,-2,4,-4]
A=[-8,8,-1,-16,-28,-27,15,-14,14,-27,-5,-6,-25,-11,28,29,-3,-25,17,-25,4,-20,2,1,-17,-10,-25]
print(lszero(A))