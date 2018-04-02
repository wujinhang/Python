while True:
	x = int(input("请输入一个数字"))
	y = int(input("请输入一个数字"))
	z = int(input("请输入算法符号1.加 2.减 3.乘 4.除:"))
	if z == 1:
		num = x+y
		print(num)
	elif z == 2:
		num = x-y
		print(num)
	elif z == 3:
		num = x*y
		print(num)
	elif z == 4:
		num = x/y
		print(num)




