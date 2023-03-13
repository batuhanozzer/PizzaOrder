import time
import csv

class Pizza:
    #Attributes
    cost = int(0)
    description = ""

    #Methods
    def getDescription(self):  return self.description
    def getCost(self):  return self.cost


class Classic(Pizza):
  def __init__(self):
      self.description = "Classic Pizza"
      self.cost = 100

class Margherita(Pizza):
     def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 200


class TurkishPizza(Pizza):
     def __init__(self):
        self.description = "Turkish Pizza"
        self.cost = 300

class PlainPizza(Pizza):
     def __init__(self):
       self.description = "Plain Pizza"
       self.cost = 400

class Decorator(Pizza):
    def __init__(self):
        self.cost = 0
        self.description = ""

class Olive(Decorator):
    def __init__(self):
        self.cost = 10
        self.description = "Olive"


class Mushroom(Decorator):
    def __init__(self):
        self.cost = 20
        self.description = "Mushroom"

class GoatCheese(Decorator):
    def __init__(self):
        self.cost = 30
        self.description = "GoatCheese"

class Meat(Decorator):
    def __init__(self):
        self.cost = 40
        self.description = "Meat"

class Onion(Decorator):
    def __init__(self):
        self.cost = 40
        self.description = "Onion"

class Corn(Decorator):
    def __init__(self):
        self.cost = 50
        self.description = "Corn"

def PrintPizzaDoughMenu():
    myfile = open("PizzaDoughMenu.txt", "r");
    print(myfile.read())
    myfile.close();

def PrintPizzaSauceMenu():
    myfile = open("PizzaSauceMenu.txt", "r");
    print(myfile.read())
    myfile.close()

def PayementProcedure(cost, description):
    myfile = open("Orders_Database.csv", "a")

    name      = input("Enter your Name: ")
    ID        = input("Enter your Card ID: ")
    password  = input("Enter your password: ")

    myfile.write(f"Name: {name}, Card ID: {ID}, Password: {password}, Pizza Cost: {cost}, Pizza Description: {description}, Order Time: {time.ctime()}\n")
    myfile.close()

def MakePizza():

    PrintPizzaDoughMenu()
    choice = int(input("Choose your pizza type: "))

    #Creating the pizza dough
    if choice == 1:
      obj = Classic()

    elif choice == 2:

      obj = Margherita()
    elif choice == 3:

      obj = TurkishPizza()
    elif choice == 4:

      obj = PlainPizza()
    else:
      print("Invalid choice!!!")
      exit (-1)

    while True:
      PrintPizzaSauceMenu()
      choice = int(input("Choose your pizza sauce: "))

      if choice == 1:
        temp = Olive()
        obj.cost += temp.getCost()
        obj.description += ", " + temp.getDescription()
      elif choice == 2:
        temp = Mushroom()
        obj.cost += temp.getCost()
        obj.description += ", " + temp.getDescription()
      elif choice == 3:
        temp = GoatCheese()
        obj.cost += temp.getCost()
        obj.description += ", " + temp.getDescription()
      elif choice == 2:
        temp = Meat()
        obj.cost += temp.getCost()
        obj.description += ", " + temp.getDescription()
      elif choice == 4:
        temp = Onion()
        obj.cost += temp.getCost()
        obj.description += ", " + temp.getDescription()
      elif choice == 2:
        temp = Corn()
        obj.cost += temp.getCost()
        obj.description += ", " + temp.getDescription()
      else:
        print("There is no such that choice!!!")

      decision = input("Do you want to add more sauce? <y/n>: ")

      if decision == 'n':
        break

    print(f"Pizza Description: {obj.getDescription()}, Pizza Cost: {obj.getCost()}")
    PayementProcedure(obj.getCost(), obj.getDescription())

while True:
    MakePizza()
    decision = input("Do you want to continue <y/n>? ")

    if decision == 'n':
      break

myfile = open("Orders_Database.csv", "r")
print(myfile.read())
myfile.close()