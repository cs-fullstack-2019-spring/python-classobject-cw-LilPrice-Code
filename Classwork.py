class Dog:
    def __init__(self, name = "", breed = "", color = "", gender = ""):
        self.name = name
        self.breed = breed
        self.color = color
        self. gender = gender

    def printAll(self):
        print(self.name, self.breed, self.color, self.gender)

class PersonStats:
    def __init__(self, name = "", height = 0, weight = 0,):
        self.name = name
        self.height = height
        self. weight = weight
        self.BMI = (weight / (height * height)) * 703

    def printBMI(self):
        print(self.name, str(self.BMI))

class Product:
    def __init__(self, name = "", price = 0, quantity = ""):
        self.name = name
        self.price = price
        self.quantity = quantity

    def changeProduct(self, newname, newprice, newquantity):
        self.name = newname
        self. price += newprice
        self.quantity = newquantity

    def PrintOnline(self):
        print(self.name, self.price, self.quantity)





def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()

def problem1():
    myDog = Dog("Max", "Bulldog", "Black", "Male")
    myDog.printAll()

def problem2():
    userInput = input("Enter a word\n")
    while userInput.lower() != "=":
        userInput1 = input("Enter another word!!:\n")
        if userInput1 == "=":
            break

def problem3():
    person1 = PersonStats("John", 56, 150)
    person2 = PersonStats("Mason", 63, 198)
    person3 = PersonStats("Ricky", 78, 329)
    person1.printBMI()
    person2.printBMI()
    person3.printBMI()

def problem4():
    onlineBuy = Product("Evolve", 60, "Standard")
    onlineBuy.PrintOnline()
    onlineBuy.changeProduct("Evolve Deluxe", 0, onlineBuy.quantity)
    onlineBuy.PrintOnline()
    onlineBuy.changeProduct("Evolve Silver", 25, onlineBuy.quantity)
    onlineBuy.PrintOnline()
    onlineBuy.changeProduct("Evolve Gold ", 50, "Ultimate")
    onlineBuy.PrintOnline()





if __name__ == '__main__':
    main()