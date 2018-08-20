n=int(input())
list1 = [int(x) for x in input().split()]
list1.sort()
print(' '.join(map(str, list1)))
