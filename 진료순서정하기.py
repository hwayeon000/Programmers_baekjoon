# 내 풀이
def my_solution(emergency):
    answer = []
    copy_list = emergency.copy()
    emergency.sort(reverse=True)
    compare = [i for i in range(1,len(emergency)+1)]
    dictionary = dict(zip(emergency,compare))
    for i in copy_list:
        print(i)
        answer.append(dictionary[i])
    return answer

# 다른 사람 풀이
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

a = [30, 10, 23, 6, 100]
print(my_solution(a))
# 답 : [2, 4, 3, 5, 1]