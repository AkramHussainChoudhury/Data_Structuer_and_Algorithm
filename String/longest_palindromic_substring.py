'''
Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).



Problem Constraints
1 <= N <= 6000



Input Format
First and only argument is a string A.



Output Format
Return a string denoting the longest palindromic substring of string A.



Example Input
Input 1:
A = "aaaabaaa"
Input 2:
A = "abba


Example Output
Output 1:
"aaabaaa"
Output 2:
"abba"
'''


def longestPalindrome(A):
    def palindrome(i,j):
        while(i>=0 and j<len(A) and A[i]==A[j]):
            i-=1
            j+=1
        return A[i+1:j]
    res=''
    ans=0
    for l in range(len(A)):
        ret = palindrome(l,l)
        if len(ret)>ans:
            ans=len(ret)
            res=ret

    for l in range(len(A)-1):
        ret = palindrome(l,l+1)
        if len(ret)>ans:
            ans=len(ret)
            res=ret

    return res


A="aaabaaa"
print(longestPalindrome(A))

