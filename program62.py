B=input()
count=0
for i in B:
	if((i=='0') or (i=='1')):
		count+=1
if(count==(len(B))):
	print("yes")
else:
	print("no")
