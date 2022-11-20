import string
import sys

def text_analyzer(s):
	"""
	This function counts the number ... 
	rak 3aref
	"""
	if isinstance(s,str):
		print("The text contains "+str(len(s))+" character(s)")
		print("- "+str(sum(1 for c in s if c.isupper()))+" upper letter(s)")
		print("- "+str(sum(1 for c in s if c.islower()))+" lower letter(s)")
		print("- "+str(sum(1 for c in s if c in string.punctuation))+" punctuation mark(s)")
		print("- "+str(sum(1 for c in s if c.isspace()))+" space(s)")
	else:
		print("AssertionError: arguments is not a string")

if __name__ == "__main__":
	if(len(sys.argv) == 2):
		text_analyzer(sys.argv[1])
	else:
		print("AssertionError: too many arguments")
