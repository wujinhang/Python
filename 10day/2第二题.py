import random
n = random.randint(0,100)

for i in range(1,11):
	i = int(input("请输入数字"))
	if i>n:
		print("猜大了")
	elif i<n:
		print("猜小了")
	else:
		print("猜对了")
		break