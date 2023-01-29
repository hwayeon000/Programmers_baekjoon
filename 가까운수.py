def my_solution(array, n):
    arr_num = []
    array.sort()
    for i in array:
        a = n-i
        arr_num.append(a*a)
    index = arr_num.index(min(arr_num))
    answer = array[index]
    return answer

arr = [3, 10, 28]
n = 20

print(my_solution(arr,n))

# 다른사람
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

