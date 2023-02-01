print("\t\t\t\t\t 英雄联盟")
print("~"*55)
import time
incomplete_sign=50
print('='*23+'开始下载'+'='*25)
for i in range(incomplete_sign+1):
    completed="*"*i
    incomplete="."*(incomplete_sign-i)
    percentage=(i/incomplete_sign)*100
    print("\r{:.0f}%[{}{}]".format(percentage,completed,incomplete),end="")
    time.sleep(0.5)
print("\n"+'='*23+'下载完成'+'='*25)
print("="*55)
英雄=input("请输入英雄名字：")
攻击值=int(input("请输入英雄攻击值："))
怪兽=input("请输入怪兽名字：")
生命值=int(input("请输入怪兽生命值"))
防御值=int(input("请输入怪兽防御值"))
怪兽血量=生命值-攻击值+防御值
print("-"*55)
print(f"{英雄}向{怪兽}发起了{攻击值}点攻击")
print(f"{怪兽}剩余{怪兽血量}点血量")
print("-"*55)
怪兽临界点=100 #怪兽血量低于怪兽临界点后可以依靠药瓶补充血点
if 怪兽临界点>怪兽血量:
     print("您需要药瓶补充血点")
elif 怪兽血量>怪兽临界点:
     print("您无需药瓶补充血点")
药瓶num=int(input("请选择药瓶数量（每瓶25点血）：")) #一个药瓶补充血量25点
回血数值=怪兽血量+药瓶num*25
print(f"您共使用{药瓶num}瓶药，回血后怪兽血量为{回血数值}点")
print("-"*55)
print("程序编辑：张永豪\t\t工号：040410")
print("*"*55)




