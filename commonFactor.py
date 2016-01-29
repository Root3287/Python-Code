def commonFactor(x):
	for i in range(-x,x):
		for j in range(-x,x):
			if i*j == x:
				print (i," ",j)
def main():
	commonFactor(2);
main();
