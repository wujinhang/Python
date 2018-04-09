#石头剪刀布
#石头 = 1
#剪刀 = 2
#布 = 3
i = 0
a = int(input("请输入次数"))
import random
while i<a:
	c = random.randint(1,3)
	m = int(input("请输入1.石头 2.剪刀 3.布\n"))
	if m <= 3 and m > 0:
		c = random.randint(1,3)
		if (c == 1 and m == 2) or (c == 2 and  m == 3) or (c == 3 and m == 1):
			print("you lose")
		elif (c == 1 and m == 3) or (c == 2 and m == 1) or (c == 3 and m == 2):
			print("you win")
		else:
			print("tie")
	i+=1
	print("玩了%s次"%i)
