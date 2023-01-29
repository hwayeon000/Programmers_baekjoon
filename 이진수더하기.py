
def my_solution(bin1, bin2):
    a = int(bin1,2)
    b = int(bin2,2)
    answer = bin(a+b)
    return answer[2:]

bin1 = "1001"
bin2 = "1111"

print(my_solution(bin1,bin2))

# 다른사람
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer