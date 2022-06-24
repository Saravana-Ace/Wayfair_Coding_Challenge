# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    i = 0
    big = A[i]
    slices = 0
    big_list = []

    while(i < len(A) - 1):
        if(big < A[i+1]):
            big = A[i+1]
            big_list.append(big)
        i += 1

    if(big == A[len(A) - 1]):
        big_list.append(big)

    return len(big_list)

    pass

print(solution([2,4,1,6,5,9,7]))
print(solution([4,3,2,6,1]))
print(solution([2,1,6,4,3,7]))
