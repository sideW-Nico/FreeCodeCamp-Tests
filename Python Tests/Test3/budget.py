class Category:
    name = None
    ledger = list()
    
    def __init__(self, categoryName):
        self.name = categoryName
    
    def deposit( self, amount, description = str() ):
        data = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(data)
        return
    
    def withdraw( self, amount, description = str() ):
        
        if self.ledger != []:        
            return False
        
        currentTotalBudget = 0     
        for dictionary in self.ledger:
            if dictionary["amount"] > 0: currentTotalBudget += dictionary["amount"]
        
        if (currentTotalBudget - amount) < 0:
            return False
        else:
            self.deposit(-amount, description)
            return True
        
    def get_balance(self):
        currentBalance = 0
        for dictionary in self.ledger:
            currentBalance += dictionary["amount"]
        return currentBalance
        
    #def transfer():
        
    #def check_funds():
        
class budget (Category):
    empty = 0 #This is just for testing
    




# def create_spend_chart(categories):