def my_solution(n):
    answer = 1
    check = 1
    res = n
    while res > 0:
        res /= answer
        if int(res) <= 1:
            break
        answer += 1
    for i in range(1,answer+1):
        check *= i
    if n < check:
        answer -= 1
    return answer
# 답 : 10
a = 3628800  
# 답 : 2
# a = 5  
print(my_solution(a))

# 다른사람
def solution(n):
    base = 1
    m = 1
    while base <= n:
        m += 1
        base *= m
    return m-1