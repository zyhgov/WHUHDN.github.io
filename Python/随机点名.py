import random
file=open("stus.csv",encoding="utf-8")
lst=[]
for line in file:
    lst.append(line.strip("\n"))#去除每行换行符

lst=lst[1:]
print(lst)
random.shuffle(lst)
print(lst)
print(random.choice(lst))