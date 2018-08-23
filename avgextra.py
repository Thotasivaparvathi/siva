N=int(input())
L=[int(x) for x in input().split()]
total=0
for i in range(0,N):
	total+=L[i]
avg=total//N
print(avg)
