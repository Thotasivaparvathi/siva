string=input()
char=0
word=0
for i in string:
	char+=1
	if i==' ':
		word+=1
print(char-word)		
