lower,upper=map(int,input().split())
for num in range(lower,upper):
   sum=0
   temp=num
   while(temp>0):
      dig=temp%10
      sum+=dig**3
      temp//=10
   if(sum==num):
      print(sum), 
