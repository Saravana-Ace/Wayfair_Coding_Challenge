# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, A):
    letters = list(S)
    i = 0
    word = ""
    while(A[i] != 0):
        word = ""
        word += letters[i] + letters[A[i]]
        letters[A[i]] = word
        i = A[i]
    return word
    pass

print(solution("cdeo", [3,2,0,1]))
#make the string into a list
#make a string with S[0] and S[A[0]]
#at the S[A[0]] is the new word
