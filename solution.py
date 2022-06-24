# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = sorted(A)
    temp = 0
    counter = 0
    for i in range(0,len(A)-1):
        if(A[i] != A[i+1] or A[i] != A[i+1]+1):
            if(A[i] < 0):
                temp = 1
            else:
                temp = A[i] + 1
        else:
            temp = A[len(A)-1] + 1

        if(A[i] == A[i+1] or A[i] == A[i+1]+1):
            print("Came here")
            counter += 1

    print(counter)
    if(counter == len(A) - 1):
        temp = A[len(A)-1]+1
    return temp

    pass

# print(solution([1, 3, 6, 4, 1, 2]))
# print(solution([-1, -3]))
print(solution([1,2,3]))
