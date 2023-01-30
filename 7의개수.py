# 7의 개수
def my_solution(array):
    answer = 0
    a = ""
    for j in array:
        a += str(j)
    for i in a:
        if i == "7":
            answer += 1
    return answer


# 다른사람 1
def solution1(array):
    return ''.join(map(str, array)).count('7')
# 다른사람 2
def solution2(array):
    return str(array).count('7')
