N,A,D=map(int,input().split())
sum=0
i=0
while(i<N):
       sum+=A
       A+=D
       i+=1
print(sum)       
