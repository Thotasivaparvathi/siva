N=int(input())
L=[int(x) for x in input().split()]
sum=0
for i in range(0,N):
	sum+=L[i]
print(sum)
