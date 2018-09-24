N,M=map(int,input().split())
if(N>M):
	greater=N
else:
	greater=M
while(1):
	if(greater%N==0 and greater%M==0):
		print(greater)
		break
	else:
		greater+=1
