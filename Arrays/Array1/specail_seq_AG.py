'''
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



Problem Constraints
1 <= length(A) <= 105



Input Format
First and only argument is a string A.



Output Format
Return an integer denoting the answer.



Example Input
Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


Example Output
Output 1:

 3
Output 2:

 0
'''


def solve(A):
    total=0
    countA=0
    for i in A:
        if i=='A':
            countA+=1
        if i=='G':
            total=(total + countA)%1000000007


    return total%1000000007
