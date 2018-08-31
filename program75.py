S=input()
L=len(S)
S1=list(S)
k=round(L//2)
if(L%2==0):
	S1[k]='*'
	S1[k-1]='*'
else:
	S1[k]='*'
ans=''
for i in S1:
	ans=ans+i
print(ans)
