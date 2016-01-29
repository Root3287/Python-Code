# Timothy A. Gibbons
# Dice
import random
class dice:
    def __init__(self):
        return;
    def role(self):
        return random.randint(1,6);
def main():
    d = dice()
    print "Trial    D1    D2    Total";
    print "-----    --    --    -----";
    for i in range(10):
        d1 = d.role();
        d2 = d.role();
        print i,"      ",d1,"   ",d2,"     ",d1+d2;