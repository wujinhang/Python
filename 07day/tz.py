high = float(input("请输入你的身高"))
体重 = float(input("请输入你的体重"))
tizhong = float(体重/(high**2))

print("你的tizhong指数为:%d"%tizhong)
if tizhong <= 18.5:
	print("过轻")
elif (tizhong >= 18.5 and tizhong <= 25):
	print("正常")
elif (tizhong >= 25 and tizhong <= 28):
	print("过重")
elif (tizhong >= 28 and tizhong <= 32):
	print("肥胖")
elif tizhong >= 32:
	print("严重肥胖")



