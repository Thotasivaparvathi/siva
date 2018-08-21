n,m=input().split()
k,s=input().split()
if(m=='1' and s=='3') or (m=='2' and s=='1') or (m=='3' and s=='2'):
	print(n,"wins")
elif(m==s):
	print("tie")
else:
	print(k,"wins")
