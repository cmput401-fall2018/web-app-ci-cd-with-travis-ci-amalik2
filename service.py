import random

class Service():

    # returns a random number
    def bad_random():
        file = open('/Users/dchui1/datafile', 'r')
        numberStrings = file.readlines()
        numbers = [int(x) for x in numberStrings]
        return random.randint(0, len(numberStrings)-1)

    def divide(self, y):
        return self.bad_random() / y

    def abs_plus(self, x):
        return abs(x) + 1

    def complicated_function(x):
        return divide(x), bad_random % 2
