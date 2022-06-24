# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    hour1 = int(A[0:2])
    hour2 = int(B[0:2])
    num1 = int(A[3:5])
    num2 = int(B[3:5])
    counter = 0
    loops = 0

    if(0 < num1 < 15):
        num1 = 15
    if(15 < num1 < 30):
        num1 = 30
    if(30 < num1 < 45):
        num1 = 45

    if(hour2 > hour1):
        if(hour2 - hour1 > 0):
            if(num2 != 0):
                loops = 1 + (hour2 - hour1)
        else:
            loops = 0

    if(hour2 < hour1):
        temph1 = 24 - hour1
        temph2 = hour2
        loops = (temph1 + temph2)

    if(loops == 0):
        if(num2 == 0):
            num2 = 60
        while(num1 <= num2):
            num1 += 15
            if(num1 <= num2):
                counter += 1

    if (loops > 0):
        num2 = 60
        i = 0
        while(num1 <= num2):
            num1 += 15

            if(num1 <= num2):
                counter += 1

            if(num1 == 60):
                num1 = 0
                i += 1

            if(i == loops - 1):
                num2 = int(B[3:5])
                if(num2 == 0):
                    num2 = 60

            if(i == loops):
                break

    return counter
    pass

print(solution("11:05", "12:49"))
solution("12:01", "12:44")
solution("20:00", "06:00")
solution("00:00", "01:00")
solution("00:00", "23:59")
solution("12:03", "12:03")
