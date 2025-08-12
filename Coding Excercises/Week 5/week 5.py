# WEEK 5
# coin purse class creation

class CoinPurse:
    def __init__(self, names):
        self.names = names
        self.initial_value = 0

    def add_coin(self, value):
        self.initial_value += value

    def print_information(self):
        print(name + " has " + str(self.initial_value) + " cents")

name= input('Enter owner name: ')
purse = CoinPurse(name)
while True:
    value = int(input('Enter coin value (cents): '))
    if value <=0:
        break
    purse.add_coin(value)
purse.print_information()

