# Timothy A. Gibbons
# FIB
def fib(x):
    if x <=1:
        return 1;
    return fib(x-1) + fib(x-2);
def main():
    for i in range(10):
        print fib(i);