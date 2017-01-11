class ICMS(object):
    def calc(self, budget):
        return budget.value * 0.06

class ISS(object):
    def calc(self, budget):
        return budget.value * 0.1
    