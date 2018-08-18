h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
t1=(h1*60)+m1
t2=(h2*60)+m2
tmin=abs(t1-t2)
m=tmin%60
hrs=(tmin-m)//60
print(hrs,m)
