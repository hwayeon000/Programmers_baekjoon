# ========= 2444 별 찍기 -7 =========== 
# import sys
# num=int(sys.stdin.readline())
# for i in range(num):
#     a=num-i-1
#     print(' '*(a),end='')
#     print('*'*(i+1-1),end='')
#     print('*'*(i+2-1),end='')
#     print()
# for i in range(1,num):
#     print(' '*(i),end='')
#     print('*'*(num-i),end='')
#     print('*'*(num-i-1),end='')
#     print()

# ========= 10988 팰린드롬인지 확인하기 =========== 
# import sys
# s=sys.stdin.readline().strip()
# a=s[::-1]
# if s==a:
#     print(1)
# else:
#     print(0)

# ========= 1157 단어 공부 =========== 
# s=input().upper()
# a=list(set(s))
# b=[0 for i in range(len(a))]
# for i in range(len(s)):
#     index=a.index(s[i])
#     b[index]+=1
# m_num=max(b)
# cnt=0
# res=None
# for i in b:
#     if m_num==i:
#         cnt+=1
# if cnt>=2:
#     res='?'
# if not res:
#     res=a[b.index(max(b))]
# print(res)

# ========= 2941 크로아티아 알파벳 =========== 
# s=input()
# dic={'c=':'a','c-':'a','dz=':'a','d-':'a','lj':'a','nj':'a','s=':'a','z=':'a'}
# for k,v in dic.items():
#     s=s.replace(k,v)
# print(len(s))

# ========= 1316 그룹 단어 체커=========== 
# num=int(input())
# cnt=0
# for i in range(num):
#     s=input()
#     r=[]
#     for i in range(len(s)-1):
#         if s[i]!=s[i+1]:
#             r.append(s[i])
#     r.append(s[-1])
#     if len(set(s))==len(r):
#         cnt+=1
# print(cnt)

# ========= 25206 너의 평점은 =========== 
# dic={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
# total=0
# div=0
# for i in range(20):
#     a,b,c=input().split()
#     if c=='P':
#         continue
#     total+=float(b)*float(dic[c])
#     div+=float(b)
# print(total/div)


# arr=[[0 for j in range(cols)] for i in range(rows)]

# ========= 2738 행렬 덧셈 =========== 
# cols,rows=map(int,input().split())
# a=[]
# b=[]
# for i in range(cols):
#     n_list=list(map(int,input().split()))
#     a.append(n_list)
# for i in range(cols):
#     n_list=list(map(int,input().split()))
#     b.append(n_list)
# for i in range(cols):
#     for j in range(rows):
#         print(a[i][j]+b[i][j],end=' ')
#     print()
