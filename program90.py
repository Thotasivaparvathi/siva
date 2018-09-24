string=input()
a=[]
for i in string:
	if(i.isdigit()):
		a.append(i)
print("".join(a))
