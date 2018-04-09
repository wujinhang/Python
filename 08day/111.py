count = 0
jishu = 0
oushu = 0
while count <= 100:
	if count%2 == 0:
		oushu+=count
	if count%2 != 0:
		jishu+=count
	count+=1
he = (jishu + oushu)
print("偶数%d"%oushu)
print("奇数%d"%jishu)
print("总和是%d"%he) 
