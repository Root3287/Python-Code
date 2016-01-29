# Timothy A. Gibbons
# Acronym
import string;

def main():
	impt = input("Enter Phrase: ");
	impt = impt.split(' ');
	for i in impt:
		output = i[0]
		print (output.capitalize(), end="")
main();