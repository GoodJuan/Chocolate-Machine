from Tkinter import *

#creating the main window
window = Tk()
#hiding it for input dialog
window.withdraw()

#class for balance object
class money:
    enoughMoney = True
    money = 0.0

    countFive = 0
    countSingle = 0
    countDime = 0

    def __init__(self, money):
        self.money = float(money)
        print(isinstance(self.money, str))

    def setBalance(self, input):
        self.money = input

    def deductBalance(self, input):
        self.money = float(self.money)
        if input == 1.1 and self.money <= 1.0:
            self.enoughMoney = False

        elif input == 0.9 and self.money <= 0.8:
            self.enoughMoney = False

        elif input == 0.5 and self.money <= 0.4:
            self.enoughMoney = False

        elif self.money <= 0.4:
            self.enoughMoney = False
        else:
            self.enoughMoney = True
            self.money -=  input



    def getBalance(self):
        return self.money

    def calculateMoney(self):
        tempBalance = self.money
        tempBalance = float(tempBalance)
        count = 0

        while count is not 3:

            #calculating 5 dollar bills
            if count is 0:
                #getting the int amount of time 5 goes into tempBalance (number of 5 dollar bills)
                temp = tempBalance/5
                self.countFive = int(temp)

                #getting remainder
                tempBalance = tempBalance % 5.0

                count += 1

            #calculating 1 dollar bills
            elif count is 1:
                #getting the int amount of time 1 goes into tempBalance (number of 1 dollar bills)
                temp = tempBalance/1
                self.countSingle = int(temp)
                #print(self.countSingle)

                #getting remainder
                tempBalance = tempBalance % 1.0

                count += 1

            #calculating dimes
            elif count is 2:
                #getting the int amount of time 0.1 goes into tempBalance (number of 0.1 coins)
                temp = tempBalance/0.1
                #print("temp: " + str(temp))
                self.countDime = temp
                #getting remainder
                tempBalance = tempBalance % 0.1

                count += 1

    def getBills(self):
        self.calculateMoney()
        return "Your Balance is: " + str(self.money) +"$\n5 dollar: " + str(self.countFive) +"\n1 Dollar: " + str(self.countSingle) + "\n10 Cent: " + str(self.countDime)

balance = money(0)
purchases = []

#class for popup input
class MyDialog:
    entry = 0
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Please enter your balance to one decimal place.").pack()

        self.entry = Entry(top)
        self.entry.pack(padx=5)
        self.entry.focus_set()


        b = Button(top, text="OK", command=self.die)
        b.pack(pady=5)

    def die(self):
        global balance
        #setting input to balance as a global variable
        balance.setBalance(self.entry.get())
        balance.calculateMoney()
        print(balance.getBills())
        self.top.destroy()

class imageDialog:
    entry = 0
    def __init__(self, parent, inputImage):

        top = self.top = Toplevel(parent)
        Label(top, image = inputImage).pack()

    def die(self):
        global balance
        #setting input to balance as a global variable
        balance.setBalance(self.entry.get())
        balance.calculateMoney()
        print(balance.getBills())
        self.top.destroy()

popup = MyDialog(window)

#main window pops up after popup dialog destroyed
window.wait_window(popup.top)
window.deiconify()


window.title("Chocolate Machine")
window.configure(background = "black")

kitkat = PhotoImage(file="newkitkat.gif")
snickers = PhotoImage(file="newsnickers.gif")
hershey = PhotoImage(file="newhershey.gif")

#Label thing
title = Label (window, text="PLEASE CLICK ONE OF THE BARS TO BUY SOME CHOCOLATE", bg="black", fg="orange", font = "none 35 bold").pack(side="top")

#adding the photo
photo1 = PhotoImage(file="dispenser.gif")
Label(window, image=photo1, bg ="black").pack(side="left")

########################buttons#########################
kitButton = Button(window, width=12, command = lambda: click(0))
kitButton.pack(fill=X, side="top")
kitButton.config(image=kitkat, width="230",  height="120")

snickButton = Button(window, width=12, command=lambda: click(1))
snickButton.pack(fill=X, side="top")
snickButton.config(image=snickers, width="230",  height="120")

hershButton = Button(window, width=12, command=lambda: click(2))
hershButton.pack(fill=X, side="top")
hershButton.config(image=hershey, width="230",  height="120")
########################################################

displayBalance = Label(window, text=balance.getBills(), bg="black", fg="orange", font = "none 30 bold")
displayBalance.pack(side="top")

#keydown
def click(type):
    if type is 0:
        balance.deductBalance(0.50)
        displayBalance.config(text=balance.getBills())
        if (balance.enoughMoney):
            imageDialog(window, kitkat)

    elif type is 1:
        balance.deductBalance(1.1)
        displayBalance.config(text=balance.getBills())
        if (balance.enoughMoney):
            imageDialog(window, snickers)


    elif type is 2:
        balance.deductBalance(0.9)
        displayBalance.config(text=balance.getBills())
        if (balance.enoughMoney):
            imageDialog(window, hershey)




""""
#text entry
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column = 0, sticky = W)

#submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

output = Text(window, width = 25, height = 6, wrap=WORD, background = "white")
output.grid(row = 5, column = 0, columnspan = 2, sticky=W)
"""


window.mainloop()

