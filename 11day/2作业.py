name_list = ["老王","老张","老宋"]
for i in name_list:
	print(i+"找个地方聚聚喝两瓶")



print(name_list[1]+"临时有事来不了")
name_list[1] = "老刘"
print(name_list)
print(name_list[1]+"找个地方聚聚喝两瓶")


name_list.insert(0,"老郭")
name_list.insert(3,"老何")
name_list.append("老毕")
print(name_list)
for e in name_list:
	print(e+"找个地方聚聚喝两瓶")


print(name_list.pop(0)+"人多了，下次再聚")
print(name_list.pop(0)+"人多了，下次再聚")
print(name_list.pop(0)+"人多了，下次再聚")
print(name_list.pop(0)+"人多了，下次再聚")
print(name_list)
for j in name_list:
	print(j+"来喝酒")

del name_list[0]
del name_list[0]
print(name_list)



