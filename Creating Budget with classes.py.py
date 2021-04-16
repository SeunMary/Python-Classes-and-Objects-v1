print('Welcome Mary')    
selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) balance (4) transfer \n")) 
if selected_option == 1:
        
            deposit()
elif selected_option == 2:
        
    withdrawal()
elif selected_option == 3:

    balance()
elif selected_option == 4:

    transfer()
else:

    print("Keep on updating your budget")
    
class budget:
    budget_category1 = 'food'
    budget_category2 = 'clothing'
    budget_category3 = 'entertainment'
    
    def __init__(self, name):
        self.name = name        
class food(budget):
    food_1 = budget('rice')
    food_2 = budget('beans')

    def deposit(self):
        current_funds = 5000
        deposit_funds = int(input(f'how much will you like to deposit to buy {self.name}? \n'))
        deposited_funds = current_funds + deposit_funds
        print('Available balance is %d' %deposited_funds)
    deposit()
       
    def withdraw(self):
    
        current_funds = 5000
        withdraw_funds = int(input(f'how much will you like to withdraw from {self.name}? \n'))
        withdrawn_funds = current_funds - withdraw_funds
        print('Available balance is %d' %withdrawn_funds)
                 
    def balance(self):
        
        print(f'Available Balance is %d' %current_funds)
     
        
    def transfer(self):
        
        int(input(f'how much will you like to transfer to {self.name}? \n'))
        

class clothing(budget):
    clothing_1 = budget('shirt')
    clothing_2 = budget('skirt')
        
    def deposit(self):
        current_funds = 5000
        deposit_funds = int(input(f'how much will you like to deposit to buy {self.name}? \n'))
        deposited_funds = current_funds + deposit_funds
        print('Available balance is %d' %deposited_funds)
    
       
    def withdraw(self):
    
        current_funds = 5000
        withdraw_funds = int(input(f'how much will you like to withdraw from {self.name}? \n'))
        withdrawn_funds = current_funds - withdraw_funds
        print('Available balance is %d' %withdrawn_funds)
                 
    def balance(self):
        
        print(f'Available Balance is %d' %current_funds)
     
        
    def transfer(self):
        
        int(input(f'how much will you like to transfer to {self.name}? \n'))

     

class entertainment(budget):
    entertainment_1 = budget('music')
    entertainment_2 = budget('games')
    def deposit(self):
        current_funds = 5000
        deposit_funds = int(input(f'how much will you like to deposit to buy {self.name}? \n'))
        deposited_funds = current_funds + deposit_funds
        print('Available balance is %d' %deposited_funds)
    
       
    def withdraw(self):
    
        current_funds = 5000
        withdraw_funds = int(input(f'how much will you like to withdraw from {self.name}? \n'))
        withdrawn_funds = current_funds - withdraw_funds
        print('Available balance is %d' %withdrawn_funds)
                 
    def balance(self):
        
        print(f'Available Balance is %d' %current_funds)
     
        
    def transfer(self):
        
        int(input(f'how much will you like to transfer to {self.name}? \n'))

    __init__(self, name)  
