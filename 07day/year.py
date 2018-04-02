while True:
	year = int(input("请输入年份\n"))
	if (year%4 == 0 and year%100 != 0) or year%400 == 0:
	     print("闰年\n")
	else:
	     print("平年\n")
