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
            amount = str(float(dictionary["amount"]))
            freeSpace = 30 - len(dictionary["description"]) - len(amount)

            if len(dictionary["description"]) > 30 - len(amount):
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


def create_spend_chart(categories):
    chart = str()

    totalWithdrawals = 0
    categoryBalance = 0

    percentages = list()

    for oneCategory in categories:
        for categoryLedger in oneCategory.ledger:
            if categoryLedger["amount"] >= 0: continue

            totalWithdrawals += categoryLedger["amount"]
            categoryBalance = oneCategory.get_balance()
            percentageCalculation = (categoryBalance * -(totalWithdrawals)) / (categoryBalance + (totalWithdrawals))
            percentages.append( percentageCalculation )

    for n in range(100, -1, -10):
        chart += (" " * (3 - len(str(n)))) + str(n) + "| "
        for percentage in percentages:
            if percentage >= 0 and percentage < 10: chart += "o "
            elif percentage > n - 10: chart += "o "
        chart += '\n'
    return chart
