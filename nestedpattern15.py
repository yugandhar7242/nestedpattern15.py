# 1.rotation matrix
# m=[]
# n=3
# for i in range(n):
#     l=list(map(int,input().split()))
#     m.append(l)
# for i in range(n):
#     for j in range(n-1,-1,-1):
#         print(m[j][i],end=" ")
#     print()


# 2.rectangle hollow pattern..


n=5
for i in range(n):
    for j in range(n+2):
        if i==0 or i==n-1 or j==0 or j==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


## 3.HALLOW DAIMOND PATTERN:

# # Upper part of the diamond
# n=5
# for i in range(1, n + 1):
#     s = " " * (n - i)
#     if i == 1:
#         print(s + "*")
#     else:
#         print(s + "*" + " " * (2 * (i - 1) - 1) + "*")

# # Lower part of the diamond
# for i in range(n - 1, 0, -1):
#     s = " " * (n - i)
#     if i == 1:
#         print(s + "*")
#     else:
#         print(s + "*" + " " * (2 * (i - 1) - 1) + "*")



