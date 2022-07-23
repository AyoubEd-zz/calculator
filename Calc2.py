class Add:
    def addition(self, a, b):
        return a+b
class Sub:
    def subtract(self, a, b):
        return a - b
class Mult:
    def multiply(self, a, b):
        return a * b
class Div:
    def division(self, a,b):
        return a/b
class Mod:
    def modulus(self,a,b):
        return a%b
class All(Add,Sub,Mult,Mod,Div):
    pass

Math = All()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Modulus ")
    print("6: Exit ")

    cd = int(input("Select operation: "))

    # Make sure the user have entered the valid choice
    if cd in (1, 2, 3, 4, 5, 6):

        # first check whether user want to exit
        if (cd == 6):
            break

        # If not then ask fo the input and call appropiate methods
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if (cd == 1):
            print(a, "+", b, "=", Math.addition(a,b))
        elif (cd == 2):
            print(a, "-", b, "=", Math.subtract(a, b))
        elif (cd == 3):
            print(a, "*", b, "=", Math.multiply(a, b))
        elif (cd == 4):
            print(a, "%", b, "=", Math.division(a, b))
        elif (cd == 5):
            print(a, "\ ", b , "=",Math.modulus(a,b))

    else:
        print("Invalid Input")