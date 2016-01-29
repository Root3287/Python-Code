class futval1:
    pricipal = 0
    rate = 0.0
    years = 0
    def __init__(self, pricipal, rate, years):
        self.pricipal = pricipal
        self.rate = rate
        self.years = years
        
    
class futval2:
    principle = 0
    deposite = 0
    intrest = 0
    year = 0
    def __init__(self, principle, deposite, interest, years):
        self.principle = principle
        self.deposite = deposite
        self.intrest = interest
        self.year = years
def main():
    futval_in1 = input("Enter inital pricipal>")
    futval_in2 = input("Enter annual intrest rate>")
    futval_in3 = input("Enter numbers of years>")
    futval_assign1 = futval1(futval_in1, futval_in2, futval_in3)