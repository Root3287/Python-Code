# Timothy A. Gibbons
# Coin flip
import random
def flip():
    return random.randint(0,1)
    
def main():
    for i in range(6):
        print flip(), flip(), flip(), flip(), flip()
