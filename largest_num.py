# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = list(sorted(A))
    big = A[len(A) - 1]
    counter = 0

    for i in range(len(A)):
        if -big in A:
            break
        else:
            big = A[len(A) - i - 1]
            counter += 1

    if counter == len(A):
        return 0
    else:
        return big

    pass

print(solution([-3,2,-2,5,-3]))
print(solution([1,1,2,-1,2,-1]))
print(solution([1,2,3,-4]))
