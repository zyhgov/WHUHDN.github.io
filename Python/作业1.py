str=input("输入字符串：")
A={}
for a in str:
    A[a]=str.count(a)
print(A)