from budget import Budget

class Tax_Calculator(object):
    def calc(self, budget):
        tax_calculated = budget.value * 0.1
        print(tax_calculated)
