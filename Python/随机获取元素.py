import random
lst=["🎅","😚","🤟","🤖","⚖","🚀","⚠"]
print("原顺序",lst)
random.shuffle(lst)
print("打乱顺序",lst)
num=random.choice(lst)
lst1=list(range(1,37))
random.shuffle(lst1)

# print(num)