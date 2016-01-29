'''
SQROOT
Timothy A. Gibbons
'''
import math;
def square(x):
	cont = 1;
	i=0
	while cont==1:
		if i == x*x:
			print (i)
			cont =0;
		i+=1
def sqroot(x):
	cont =1;
	i=0;
	while cont==1:
		if i*i == x:
			print (i) 
			cont=0
		i+=1;
def main(x):
	sqroot(x)
main(81);