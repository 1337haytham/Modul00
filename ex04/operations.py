import sys

if len(sys.argv) == 3:
	try:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	except:
		print("AssertionError: only integers")
		exit()
	print("Sum:        "+str(a+b))
	print("Difference: "+str(a-b))
	print("Product:    "+str(a*b))
	if b == 0:
		print("Quotient:   ERROR (division by zero)")
		print("Remainder:  ERROR (modulo by zero)")
	else:
		print("Quotient:   "+str(a/b))
		print("Remainder:  "+str(a%b))
if len (sys.argv) > 3:
	print("AssertionError: too many arguments")
