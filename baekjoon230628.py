# ========= 2566 최댓값 =========== 
# arr=[]
# for i in range(9):
#     n=list(map(int,input().split()))
#     arr.append(n)
# num=max(map(max,arr))
# for i in range(9):
#     for j in range(9):
#         if arr[i][j]==num:
#             print(num)
#             print(i+1, j+1)

# ========= 10798 세로읽기 =========== 
# arr=[]
# a_len=[]
# for i in range(5):
#     n=list(input())
#     a_len.append(len(n))
#     arr.append(n)
# res=''
# cnt=0
# for i in range(max(a_len)):
#     for j in range(5):
#         try:
#             res+=arr[j][cnt]
#         except:
#             continue
#     cnt+=1
# print(res)

# ========= 2563 색종이 =========== 
res=0
xy=[]
n=int(input())
res+=100*n
for i in range(n):
    x,y=map(int,input().split())
    a=[x,x+10,y,y+10]
    xy.append(a)
print(xy)
# for i in range(n):
#     for j in range(n):
#         if xy[i][0]>=xy[i+1][0]