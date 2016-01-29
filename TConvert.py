# Timothy A. Gibbons
# Tempeture Convert
class temp:
    def CtoF(self,c):
        return c*1.8+32
    def FtoC(self,f):
        return (f-32)/1.8;
def main():
    t = temp()
    for i in range(5):
        ask = input("Temp to convert to F> ");
        print t.CtoF(ask);
    
    for i in range(5):
        ask = input("Temp to convert to C> ");
        print t.FtoC(ask);