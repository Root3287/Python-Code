# Timothy A. Gibbons
# Cypher
import string;
def helper(message, shift):
	message = message.lower()
	secret = ""
	for c in message.split():
		print (c);
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			if num > ord("z"):     # wrap if necessary
				num -= 26
			elif num < ord("a"):
				num += 26
			secret = secret + chr(num)
		else:
			# don't modify any non-letters in the message; just add them as-is
			secret = secret + c
	return secret
def main():
	impt = input("Enter String to be encoded: ");
	offset = int(input("Enter offset"));
	print(helper(impt, offset))