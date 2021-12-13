class Category:    
    def __init__(self, categoryName):
        self.name = categoryName
        self.ledger = list()

    def __str__(self):
        objectString = str()

        nameLength = len(self.name)
        characters = round( (30-nameLength) / 2 )

        objectString += '*' * characters + self.name + ('*' * characters) + '\n'

        for dictionary in self.ledger:
            amount = str(format(dictionary["amount"], '.2f'))
            freeSpace = 30 - len(dictionary["description"]) - len(amount)

            if len(dictionary["description"]) >= 30 - len(amount):
                objectString += dictionary["description"][:30 - len(amount) - 1] + ' ' + amount + '\n'
            else:
                objectString += dictionary["description"] + (' ' * freeSpace) + amount + '\n'
        
        objectString += 'Total: ' + str(self.get_balance())
        return objectString

    def deposit( self, amount, description = str() ):
        data = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(data)
        return
    

    def withdraw( self, amount, description = str() ):
        if self.ledger == []:        
            return False

        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        else: 
            return False
            
    def get_balance(self):
        currentBalance = 0
        for dictionary in self.ledger:
            currentBalance += dictionary["amount"]
        return currentBalance
    
    
    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total+= item["amount"]
        return total

  
    def transfer(self, amount, budgetObject):
        result = self.withdraw(amount, 'Transfer to ' + budgetObject.name)
        if result:
            budgetObject.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        currentTotalBudget = 0 
        for dictionary in self.ledger:
            currentTotalBudget += dictionary["amount"]
        return (currentTotalBudget - amount) >= 0

def maxLength(categories):
    maxName = 0
    for oneCategory in categories:
        if len(oneCategory.name) > maxName: maxName = len(oneCategory.name)
    return maxName

def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
        
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i-=10
    
    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    actualLen = 0
    for x in range(len(maxi)):
        actualLen += 1
        nameStr = '     '
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        if actualLen != len(maxi):
            nameStr += '\n'
        x_axis += nameStr

    res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res