import math
N,M=map(int,input().split(' '))
P=N*M
if math.sqrt(P)==int( math.sqrt(P)):
    print ("yes")
else:
    print ("no")
