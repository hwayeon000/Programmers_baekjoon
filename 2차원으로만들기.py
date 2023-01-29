def solution(num_list, n):
    answer = [[j for j in my_list[i*n:(i*n)+n]] for i in range(int(len(my_list)/n))]
    return answer

# answer = [[1, 2], [3, 4], [5, 6], [7, 8]]
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
b = [[0 for j in range(3)] for i in range(3)]
print(b)

print(solution(my_list, n))

# 다른사람
import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()