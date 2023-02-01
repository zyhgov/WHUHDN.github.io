import random

lst=["剪刀", "石头", "布"]
winlst=[["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
count1=count2=0
for i in range(5):
    pc=random.choice(lst)
    user=input("看啥呢，出手哈：")
    if user in lst:
        if [user,pc] in winlst:
            count1+=1
            print(f"计算机出{pc}，你赢了哈")
        elif user == pc:
            print(f"计算机出{pc},平局哈")
        else:
            count2+=1
            print(f"计算机出{pc},计算机赢了")
    else:
        print("输入的是啥，要不你自己看看😓")
if count1>count2:
    print("你笑到了最后")
elif count2>count1:
    print("计算机战胜了你")
else:
    print("你俩五五开")