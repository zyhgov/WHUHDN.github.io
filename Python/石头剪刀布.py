import random

while True:
    a = input("你请出手(石头/剪刀/布 ps：别出脚)：")
    b = ["剪刀", "石头", "布"]
    win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
    pc = random.choice(b)
    print("你自己出手：", a)
    print("计算机假装出手：", pc)
    if a in b:
        if a == pc:
            print("你两平局")
        elif [a, pc] in win_list:
            print("恭喜，你把计算机比赢了")
        else:
            print("很遗憾，你的脑子被计算机吃了")
    else:
        print("输入的是啥，你自己看看😓")
