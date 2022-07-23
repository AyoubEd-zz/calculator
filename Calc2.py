import math

class Add:
    def addition(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a+b
class Sub:
    def subtract(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a - b
class Mult:
    def multiply(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a * b
class Div:
    def division(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a/b
class Mod:
    def modulus(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a%b
class Exp:
    def exp(self):
        Base=float(input("\n Enter the Base NUmber whose powers you have to calculate : "))
        exponent=float(input("\n Enter the exponent Number which will be given as power to base  : "))
        power=Base**exponent
        return power
class Root:
    def root(self):
        Number=float(input("\n Enter the number whose root you want to find : "))
        exponent=float(input("\n Which Root You want ? "))
        result=pow(Number,1/exponent)
        return result
class Factorial:
    def fact(self):
        factorial=1
        Number=float(input("\n Enter a Number whose factorial You want to be Calculated : "))
        if (Number>=1) and Number.is_integer()==True:
            for fact in range(1, int(Number+1)):
                factorial=factorial*fact
            return factorial
        else:
            print("\n")
            for i in tqdm (range (100), desc=" ERROR !!!!..."):
                time.sleep(0.01)
                pass
            print("\n The FACTORIAL cannot be calculated for NEGATIVE NUMBERS and DECIMAL NUMBERS !!!!!!!!!", end="\n\n")
        return "NULL"
class Trig:
    def trig(self):
        print("\n WHICH TRIGNOMETRIC FUNCTION DO YOU WANT TO USE \n\n 1. SIN \n 2. COS \n 3. TAN \n 4. SEC \n 5. COSEC \n 6. COT ", end="\n")
        choice=float(input("\n Enter Choice (1-6)"))
        x=float(input("\n Enter the values in degrees "))
        x=(x/180)*3.14159265359
        if (choice==1):
            return math.sin(x)
        elif(choice==2):
            return math.cos(x)
        elif(choice==3):
            return math.tan(x)
        elif(choice==4):
            return 1/math.cos(x)
        elif(choice==5):
            return 1/math.sin(x)
        elif(choice==6):
            return 1/math.tan(x)
        else:
            print("\n\n INVALID CHOICE !!!! \n \n Please Enter a VALID CHOICE(1-6)",end="\n ")
        return(0)

class Logarithm:
    def log(self):
        print("\n Which type of logarithms do you want to calculate ?", end="\n")
        print("\n 1.  NATURAL LOGS , (Base=e or ln)", end="\n")
        print("\n 2. LOGS WITH A BASE AND VALUE", end="\n")
        choice=int(input("\n Enter 1 or 2 "))
        if choice==1:
            Base=float(input("\n Enter a Base Number whose log you want to calculate "))
            return math.log(Base)
        elif choice==2:
            Base=float(input("\n Enter a Base Number whose log you want to calculate "))
            Exponent=float(input("\n Enter a exponent number which will the log base "))
            return math.log(Base, Exponent)
        else:
            print("\n Print INVALID CHOICE!!!! \n\n")
            print("Enter a choice between 1 or 2 ")
        return 0

class All(Add,Sub,Mult,Mod,Div,Exp, Root, Factorial, Trig, Logarithm):
    pass

Math = All()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Modulus ")
    print("6: Exp")
    print("7: Root")
    print("8: Factorial")
    print("9: Trigonometry")
    print("10: Logarithm")
    print("0: Exit ")

    cd = int(input("Select operation: "))

    # Make sure the user have entered the valid choice
    if cd <= 10:

        # first check whether user want to exit
        if (cd == 0):
            break

        if (cd == 1):
            print("Result", Math.addition())
        elif (cd == 2):
            print("Result", Math.subtract())
        elif (cd == 3):
            print("Result", Math.multiply())
        elif (cd == 4):
            print("Result", Math.division())
        elif (cd == 5):
            print("Result", Math.modulus())
        elif cd == 6:
            print("Result", Math.exp())
        elif cd == 7:
            print("Result", Math.root())
        elif cd == 8:
            print("Result", Math.fact())
        elif cd == 9:
            print("Result", Math.trig())
        elif cd == 10:
            print("Result", Math.log())

    else:
        print("Invalid Input")
