import sys

lst = sys.argv[1:]
ll  = []
for el in lst:
	ll.append(el)
l=' '.join(ll).swapcase()
print(l[::-1])
