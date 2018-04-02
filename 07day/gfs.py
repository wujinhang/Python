high = int(input("请输入你的身高"))
money = int(input("请输入你的身价"))
yanzhi = int(input("请输入你的颜值分"))


if high >= 180 and money >= 1000000 and yanzhi >= 90:
    print("高富帅")
elif money >= 1000000 and yanzhi >=90:
    print("富帅")
elif yanzhi >=90:
    print("帅")
elif high <=160 and money <=100 and yanzhi <=60:
    print("矮穷矬")
else:
    print("系统出错")

