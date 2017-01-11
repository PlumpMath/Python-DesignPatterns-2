class Budget(object):

    def __init__(self, value):
        self.__value = value

    #The property tag will create the Ilusion that the programmer is acessing the attribute Value, but it's just the return of a funcion.
    #Example: BudgetObject.value, it will not be alterable but readable
    @property
    def value(self):
        return self.__value


