# Timothy A. Gibbons
# Lighning
def timeForSound(time):
    return 1100*float(time);

def ftToMi(feet):
    return float(feet/5280);

def main():
    inpt= input('Distance between lighning and thunder> ')
    print(ftToMi(timeForSound(inpt)), "Miles")
main();