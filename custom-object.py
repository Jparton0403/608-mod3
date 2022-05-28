class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
    
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100
    
    def calculateTip(self, taxPercent):
        return self.amount * taxPercent/100
    def calculateTotoal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100 + tipPercent/100)
    
purchase = Purchase(100)
taxPercent = 7.5
tipPercent = 20

tax = purchase.calculateTax(taxPercent)

tip = purchase.calculateTip(tipPercent)

print('tax:', tax)

print('tip:', tip)

print('total:', purchase.calculateTotoal(taxPercent, tipPercent))