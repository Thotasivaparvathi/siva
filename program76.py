N=int(input())
for i in range(2,N-1):
	k=N%i
	if(k==0):
		print("yes")
		break
else:
            print("no")
