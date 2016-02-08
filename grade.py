# Timothy A. Gibbons
# Grade
def grade(grade):
	if grade == 5:
		return "A"
	elif grade == 4:
		return "B"
	elif grade == 3:
		return "C"
	elif grade == 2:
		return "D"
	elif grade == 1:
		return "F"
	else: 
		return "F"
def main():
	inpt = int(input("Enter grade> "));
	print (grade(inpt))
main();
