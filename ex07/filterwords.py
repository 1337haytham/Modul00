import sys
import string

ll = []
i = 0


if len(sys.argv) == 3:
	try:
		int(sys.argv[2])
	except:
		print("ERROR")
		exit()
	lst = sys.argv[1].split()
	for el in lst:
		if (sum(1 for c in el if c not in string.punctuation)) > int(sys.argv[2]):
			ll.append(el)
	print(ll)
else:
	print("ERROR")
