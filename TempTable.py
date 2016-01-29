# Timothy A. Gibbons
# Temp Table
class temp:
    def CtoF(self,c):
        return c*1.8+32
    def FtoC(self,f):
        return (f-32)/1.8;
def main():
    t = temp()
    print "C    |    F";
    print "-----------";
    for i in range(11):
        print i*10,"  |  ",t.CtoF(i*10)