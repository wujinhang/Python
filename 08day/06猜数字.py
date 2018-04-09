a = True

import random

c = random.randint(1,100)
while a:
	w = int(input("请输入数字"))
	if w > c:
		print("猜大了")
	if w == c:
		print("猜对了")

	if w < c:
		print("猜小了")
	a+=1
	if a > 10:
		a = False
		print("猜的次数太多了")
		break





