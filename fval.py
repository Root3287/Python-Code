'''
	Fval1 and fval2
	Timothy A. Gibbons
'''
def fval1():
	yearly = float(input("Enter the yearly investment: "))
	apr = float(input("Enter the annual interest rate: "))
	years = int(input("Enter the number of years: "))

	for i in range(years):
	    yearly = yearly * (1+apr)
	print ("The value in ",years," years is: %f" % yearly)

def fval2():
	yearly = float(input("Enter the yearly investment: "))
	apr = float(input("Enter the annual interest rate: "))
	years = int(input("Enter the number of years: "))
	depo = float(input("Enter yearly deposite"))

	for i in range(years):
	    yearly = yearly * (1+apr) + depo
	print ("The value in ",years," years is: %f" % yearly)
def main():
	fval1();
	fval2();

main();