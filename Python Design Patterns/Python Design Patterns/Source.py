from Strategy.tax_calculator import *
import sys
from os import system

def main():

    Calculator = Tax_Calculator()
    budget = Budget(500)
    Calculator.do_calc(budget, ICMS())
    system("pause")
    





if __name__ == "__main__":
    sys.exit(int(main() or 0))