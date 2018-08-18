import re
N = input()
new = re.sub('[\w]+' ,'', N)
print(len(new))

