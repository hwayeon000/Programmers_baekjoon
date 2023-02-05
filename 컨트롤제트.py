def solution(a):
    a = a.split(" ")
    print(a)
    res = 0
    j = 0
    for i in a:
        if i == "Z":
            res -= (int(a[j-1]))
        else:
            res += int(a[j])
        j += 1
    return res