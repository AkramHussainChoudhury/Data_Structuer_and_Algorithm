'''

Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.



Problem Constraints
1 <= N, length of each word <= 105

Sum of the length of all words <= 2 * 106



Input Format
The first argument is a string array A of size N.

The second argument is a string B of size 26, denoting the order.



Output Format
Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.



Example Input
Input 1:

 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"
Input 2:

 A = ["fine", "none", "bush"]
 B = "qwertyuiopasdfghjklzxcvbnm"


Example Output
Output 1:

 1
Output 2:

 0

'''

def solve(A, B):
    seq={}
    for i in range(0,len(B)):
        seq[B[i]]=i

    for i in range(1,len(A)):
        j=0
        current=list(A[i])
        last=list(A[i-1])
        minlength=min(len(current),len(last))

        while(j<minlength-1 and current[j]==last[j]):
            j+=1

        if seq[current[j]]<=seq[last[j]]:
            return 0

    return 1


A = ["fine", "none", "bush"]
B = "qwertyuiopasdfghjklzxcvbnm"

print(solve(A,B))