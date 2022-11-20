import sys

if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
if len(sys.argv) == 2:
	try:
		i = int(sys.argv[1])
	except:
		print("AssertionError: argument is not an integer")
		exit()
	if i%2:
		print("I'm Odd.")
	elif i == 0:
		print("I'm Zero.")
	else:
		print("I'm Even.")
