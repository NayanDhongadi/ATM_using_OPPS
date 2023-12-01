class Bank:

    def verify(self):
        temp = int(input(' \n \nEnter pin to verify :-'))
        if temp == self.pin:
            print(' \n \npin verify suyccesfully')
            return True
        else:
            print(' \n \nincorrect pin')
            return False
            

    def new_Resitration(self):

        self.name = input('Enter Your Name :- ')
      
        self.number = input('\nenter your number :- ')

        self.pin = int(input('\nEnter Pin :- '))
     
        Bank.retry(self)




    def check_Balance(self):
        if Bank.verify(self):
            print(self.balance)
      
        Bank.retry(self)



    def deposit(self):

        if Bank.verify(self):
            
            depamt = int(input(' \nEnter amount :- '))
            self.balance = self.balance + depamt
            print (' \n \nBalance deposit succesfully')
        Bank.retry(self)



    def withdraw(self):
        if Bank.verify(self):
            temp1 = int(input(' \nEnter amount to0 withdraw :- '))
            if temp1 < self.balance:
                self.balance = self.balance - temp1
            else:
                print(' \nyou have insufficient balance ')

        Bank.retry(self)


    def changepin(self):
        if Bank.verify(self):
            temp = int(input('Enter new pin :- '))
            self.pin = temp
        Bank.retry(self)



    def getdetails(self):
        print('name :- ',self.name,'\n','number :- ',self.number,'\n','pin :- ',self.pin,'\n','Balance :- ',self.balance)
        Bank.retry(self)

    def history(self):
        print('sorry you have no history yet ')
        Bank.retry(self)


    def exit(self):
        print(' \n \nGood Byeee Visit again')
        

   
    
    
    def retry(self):
        temp = input('do you want to view menu ? (Y/N): ') 
        if temp == 'y' or 'Y':
            Atm.menu(self)
        elif temp == 'n' or 'N':
            Bank.exit(self)
        else:
            print('invalid Input ')
            Bank.retry(self)




# -------------`````````````````-----------------------`````````````----------------------






class Atm:

    def __init__(self):
        self.name = ''
        self.number = ''
        self.balance = 0
        self.pin = None
        self.menu( )
    def menu(self):
        print('''
        Welcome to 'APKA APNA BANK'
         --------------------------------------------------------------------------
        |   Press 1 for new registration        Press 5 for Change_Pin             |
        |   Press 2 for Check_Balance           Press 6 for Get_Details            |
        |   Press 3 for Deposit                 Press 7 for Transaction_History    |
        |   Press 4 for Withdraw                Press 8 for exit                   |
         --------------------------------------------------------------------------
         

        ''')
        self.choice()



    def choice(self):
        cho = int(input())
        if cho  == 1:
            Bank.new_Resitration(self)
        elif cho == 2:
            Bank.check_Balance(self)
        elif cho == 3:
            Bank.deposit(self)
        elif cho == 4:
            Bank.withdraw(self)
        elif cho == 5:
            Bank.changepin(self)
        elif cho == 6:
            Bank.getdetails(self)
        elif cho == 7:
            Bank.history(self)
        elif cho == 8:
            Bank.exit(self)
        
        else:
            print(' \nInvalid Input ')


obj = Atm()