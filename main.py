import math

print("Welcome to the Scientific Calculator")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
opeartion = input("What math opeartion would you like to perform. ")


def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1,num2):
    result = num1 - num2
    return result

def multi(num1,num2):
    result = num1 * num2
    return result

def div(num1,num2):
    result = num1 / num2
    return result

def sqrt(num):
    result = math.sqrt(num)
    return result

def absolute(num):
    result = math.fabs(num)
    return result

def square(num1,num2):
    result = math.pow(num1,num2)
    return result

if opeartion == "addtion" or opeartion == "add" or opeartion == "Add" or opeartion == "Addtion" or opeartion == "+" or opeartion == "1":
  print(add(number1,number2) , "is the sum of " + str(number1) + " and " + str(number2))

elif opeartion == "subtraction" or opeartion == "subtract" or opeartion == "Subtract" or opeartion == "Subtraction" or opeartion == "-" or opeartion == "2":
  print(sub(number1,number2) , "is the difference of " + str(number1) , "and " + str(number2))

elif opeartion == "multiplication" or opeartion == "multiply" or opeartion == "Multiply" or opeartion == "Multiplication" or opeartion == "Times" or opeartion == "times" or opeartion == "*" or opeartion == "3":
  print(multi(number1,number2) , "is the product of " + str(number1) , "and" , str(number2))

elif opeartion == "division" or opeartion == "divide" or opeartion == "Divide" or opeartion == "Division" or opeartion == "/" or opeartion == "4":
  print(div(number1,number2) , "is the quotient of " + str(number1) , "and" , str(number2))

elif opeartion == "root" or opeartion == "square root" or opeartion == "Root" or opeartion == "Square Root" or opeartion == "√ ":
    option = input("Which number do you choose to find the square root of: number 1 or number 2. Type 1 for the first number and 2 for the second.")
    if option == "2" or option == "Two" or option == "two" or option == str(number2):
        print(sqrt(number2) , "is the square root of" , str(number2))


    if option == "1" or option == "One" or option == "one" or option == str(number1):
        print(sqtr(number1) , "is the square root of" , str(number1))


elif opeartion == "^" or opeartion == "power" or opeartion == "**" or opeartion == "square" or opeartion == "power of":
    optionCd = input("Which number do you choose to be the base: number 1 or number 2. Type 1 for the first number and 2 for the second.")
    if optionCd == "2" or optionCd == "Two" or optionCd == "two" or optionCd == str(number2):
        print(str(number2) , "to the power of" , str(number1) , "is" , square(number2,number1))
        if square(number1,number2)%2 == 0:
            print("It is an even number")
        else:
            print("It is an odd number")

    if optionCd == "1" or optionCd == "One" or optionCd == "one" or optionCd == str(number1):
        print(str(number1) , "to the power of" , str(number2) , "is" , square(number1,number2))

elif opeartion == "absolute value" or opeartion == "Absolute value" or opeartion == "Absolute Value" or opeartion == "absolute Value" or opeartion == "| |" or opeartion == "||":
    optionAb = input("Which number do you choose to find the absolute value of: number 1 or number 2. Type 1 for the first number and 2 for the second.")
    if optionAb == "2" or optionAb == "Two" or optionAb == "two" or optionAb == str(number2):
        print(absolute(number2) , "is the square root of" , str(number2))

    if optionAb == "1" or optionAb == "One" or optionAb == "one" or optionAb == str(number1):
        print(absolute(number1) , "is the square root of" , str(number1))


else:
  print("Invalid Input")