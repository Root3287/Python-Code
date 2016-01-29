#Timothy A. Gibbons
#Pizza Cost

class Pizza:
    area = 0;
    cost = 0;
    def __init__(self, d, cost):
        self.area = pow((0.5*d), 2)*3.14;
        self.cost = cost;
    def costPerInch(self):
        return self.cost/self.area;
def main():
    inp = input("Diameter of pizza> ");
    inp2 = input("Cost of pizza> ")
    p = Pizza(inp, inp2)
    print "Cost per inch: ", round(p.costPerInch(), 2);
    