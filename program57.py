N,K=map(int,input().split())
list=[int(x) for x in input().split()]
if N in list:
	count=list.count(N)
	print(count)
elif K in list:
	count=list.count(K)
	print(count)
else:
	print(0)
