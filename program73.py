N=int(input())
L,R=map(int,input().split())
if(L<N<R):
	print("yes")
elif(N==L or N==R):
	print("no")
else:
	print("no")
