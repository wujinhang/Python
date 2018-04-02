#石头剪刀布
#石头 = 1
#剪刀 = 2
#布 = 3
import random
while True:
	c = random.randint(1,3)
	m = int(input("请输入\n"))
	if m <= 3 and m > 0:
		c = random.randint(1,3)
		if (c == 1 and m == 2) or (c == 2 and  m == 3) or (c == 3 and m == 1):
			print("you lose")
		elif (c == 1 and m == 3) or (c == 2 and m == 1) or (c == 3 and m == 2):
			print("you win")
		else:
			print("tie")

