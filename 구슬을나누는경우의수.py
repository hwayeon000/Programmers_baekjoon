def solution(balls, share):
    res1 = 1
    res2 = 1
    a = (balls-share)
    for i in range(a):
        res1 *= balls
        balls -= 1
        res2 *= (i + 1)
    return int(res1/res2)

# 팩토리얼
n = 5
res = 1
for i in range(n):
    res *= (i + 1)
#----------------------
balls = 5
share = 3
# 10
res1 = 1
res2 = 1
a = (balls-share)
for i in range(a):
    res1 *= balls
    balls -= 1
    res2 *= (i + 1)
print(int(res1/res2))


