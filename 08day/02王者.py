ID = "wujinhang"
pwd = 123456
count = True
while count:
	iD = input("请输入账号:")
	Pwd = int(input("请输入密码"))
	if iD == ID and Pwd == pwd:
		print("登录成功")
		a = int(input("请选择英雄0.ADC 1.肉 2.法师"))
		if a == 0:
			print("鲁班大师")
		elif a == 1:
			print("程咬金")
		elif a == 2:
			print("王昭君")
	elif iD != ID or Pwd != pwd:
		print("账号或密码错误，请重新输入")
		count+=1
		if count == 4:
			count = False
			print("次数过多")
			break












