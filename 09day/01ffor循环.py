a = int(input("输入初始值"))
b = int(input("输入终止值"))
c = 0
if a < b:
	for i in range(a,b+1):
		print(i)
		c = c + i
else:
	print("输入有误")


print(c)





sum1 = 0
while a <= b:
	sum1 = sum1 + a
	a+=1
