'''You are given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.


Problem Constraints
1 <= N <= 3 * 105



Input Format
The only argument given is string A.



Output Format
Return the string A after reversing the string word by word.



Example Input
Input 1:
A = "the sky is blue"
Input 2:
A = "this is ib"


Example Output
Output 1:
"blue is sky the"
Output 2:
"ib is this"


Example Explanation
Explanation 1:
We reverse the string word by word so the string becomes "blue is sky the".
Explanation 2:
We reverse the string word by word so the string becomes "ib is this".'''


def solve(A):
    A=list(A)
    i=0
    j=len(A)-1
    while(i<j):
        t=A[i]
        p=A[j]
        A[i]=p
        A[j]=t
        i+=1
        j-=1

    print(''.join(A))
    i=0
    j=0
    N=len(A)

    while(i<N and j<N):
        while(j <N and A[j]!=" "):
            j+=1
        k=j-1
        while(i<k):
            temp=A[i]
            A[i]=A[k]
            A[k]=temp
            i+=1
            k-=1
        i=j+1
        j=j+1

    return ''.join(A)


A = "the sky is blue"
A='crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv'
print(solve(A))