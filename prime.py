N=int(input())
k=0
if(N<=1000):
            for i in range(2,N//2+1):
                        if(N%i==0):
                                    k=k+1
            if(k<=0):
                        print("Yes")
            else:
                        print("no")
else:
                        print("no")
