# =========  바구니 뒤집기 =========== 
# import sys
# s_num,e_num = map(int,sys.stdin.readline().split(' '))
# num_list=list(i for i in range(1,s_num+1))
# for i in range(e_num):
#     s,e=map(int,sys.stdin.readline().split(' '))
#     if s-1==0:
#         num_list[:e] = num_list[e-1::-1]
#     else:
#         num_list[s-1:e]=num_list[e-1:s-2:-1]
# print(' '.join(map(str,num_list)))

# =========  평균 =========== 
# num=sys.stdin.readline()
# num_list=list(map(int,sys.stdin.readline().split(' ')))
# div=max(num_list)
# total = 0.0
# for i in num_list:
#     total+=i/div*100
# print(total/int(num))


# =========  문자와 문자열 =========== 
# s=sys.stdin.readline()
# num=int(sys.stdin.readline())
# print(s[num-1])

# ========= 단어 길이 재기 =========== 
# s=sys.stdin.readline()
# print(len(s)-1)

# ========= 문자열 =========== 
# import sys
# num=int(sys.stdin.readline())
# for i in range(num):
#     a=sys.stdin.readline()
#     print(a[0],end='')
#     print(a[len(a)-2])

# ========= 아스키 코드 =========== 
# s=str(sys.stdin.readline()).strip()
# print(ord(s))

# ========= 숫자의 합 =========== 
# n=int(sys.stdin.readline())
# s=sys.stdin.readline().strip()
# num=0
# for i in range(len(s)):
#     num+=int(s[i])
# print(num)

# 알파벳 딕셔너리타입 
# dict={}
# for i in range(26):
#     dict[chr(97+i)]=i

# ========= 알파벳 찾기 =========== 
# s=sys.stdin.readline()
# dict={}
# res=[]
# for i in range(len(s)):
#     if s[i] not in dict:
#         dict[s[i]]=i
# for i in range(26):
#     if chr(97+i) in dict:
#         res.append(dict[chr(97+i)])
#     else:
#         res.append(-1)
# print(' '.join(map(str,res)))

# ========= 문자열 반복 =========== 
# num=int(sys.stdin.readline())
# res=[]
# for i in range(num):
#     n,s=sys.stdin.readline().split(' ')
#     rs=''
#     n=int(n)
#     for i in range(len(s)-1):
#         rs+=s[i]*n
#     res.append(rs)
# print('\n'.join(res))

# ========= 단어의 개수 =========== 
# s=(sys.stdin.readline()).strip().split()
# print(len(s))
# split(' '), split() 유의

# ========= 상수 =========== 
# n1,n2=(sys.stdin.readline()).split()
# n1=int(n1[::-1])
# n2=int(n2[::-1])
# res=n1 if n1>n2 else n2
# print(res)

# ========= 다이얼 =========== 
# s=(sys.stdin.readline())
# res=0
# for i in s:
#     n=0
#     if i in 'ABC':
#         n=3
#     elif i in 'DEF':
#         n=4
#     elif i in 'GHI':
#         n=5
#     elif i in 'JKL':
#         n=6
#     elif i in 'MNO':
#         n=7
#     elif i in 'PQRS':
#         n=8
#     elif i in 'TUV':
#         n=9
#     elif i in 'WXYZ':
#         n=10
#     res+=n
# print(res)


# ========= 그대로 출력하기 =========== 
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
