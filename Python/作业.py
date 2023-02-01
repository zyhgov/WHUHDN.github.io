print("\t\t\t\t\t 哇哈哈中学-学生学习查询")
print("~"*55)
name=(input("请输入该生姓名："))
YW=int(input("该生的语文成绩是："))
if YW>=90:
    print("该生语文成绩优秀")
elif YW>=80:
    print("该生语文成绩良好")
elif YW>=60:
    print("该生语文成绩中等")
elif YW<60:
    print("该生语文成绩较差")
SX=int(input("该生的数学成绩是："))
if SX>=90:
    print("该生数学成绩优秀")
elif SX>=80:
    print("该生数学成绩良好")
elif SX>=60:
    print("该生数学成绩中等")
elif SX<60:
    print("该生数学成绩较差")
YY=int(input("该生的英语成绩是："))
if YY>=90:
    print("该生英语成绩优秀")
elif YY>=80:
    print("该生英语成绩良好")
elif YY>=60:
    print("该生英语成绩中等")
elif YY<60:
    print("该生英语成绩较差")
PJF=(YW+SX+YY)/3
print(f"{name}的三科平均分为{PJF}")
print("the end")
print("/"*55)