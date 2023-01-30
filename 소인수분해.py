# 소인수분해
def solution(n):
    answer = []
    div = 2
    while n > 1:
        if n % div == 0:
            answer.append(div)
            n /= div
            int(n)
        else:
            div += 1
    answer = sorted(list(set(answer)))
    return answer