n=int(input())
f1=1
f2=1
i=2
if(n<=0):
	print("positive number")
elif(n==1):
	print(f1)
else:
	print (f1, end=' ')
	print (f2, end=' ')
	while(i<n):
		f3=f1+f2
		print (f3, end=' ')
		f1=f2
		f2=f3
		i+=1
		
