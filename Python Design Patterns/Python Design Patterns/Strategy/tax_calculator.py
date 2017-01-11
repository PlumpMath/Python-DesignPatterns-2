from .budget import Budget
from .taxes import *

class Tax_Calculator(object):

    def do_calc(self, budget, tax):
        tax_calculated = tax.calc(budget)
        print(tax_calculated)
