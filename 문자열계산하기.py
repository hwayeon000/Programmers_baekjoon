def solution(a):
    a = a.split(" ")
    b = int(a[0])
    for i in range(1, len(a), 2):
        if a[i] == "+":
            b += int(a[i+1])
        elif a[i] == "-":
            b -= int(a[i+1])
    return b