bu=int(input())
if(bu>1):
	for i in range(2,bu):
		if(bu%i)==0:
			print("no")
			break
		else:
			print("yes")
else:
	print("no")
