import re

def solution(my_string):
    answer = []
    nums = re.findall('\d+', my_string)
    answer = list(map(int,nums))
    return sum(answer)

my_string = "1a2b3c4d123Z"
# result = 133
# 숫자 없으면 0
str = my_string.lower()
print(str)
# re 함수 참고!
alphas = re.findall('[a-zA-Z]', str)
nums = re.findall('\d', str)
nums1 = re.findall('\d+', str)
nums2 = re.findall('\d-', str)
print(nums)
print(nums1)
print(nums2)
print(alphas)
# a = 0
# for j in nums:
#     a += int(j)
# print(a)
print(solution(my_string))