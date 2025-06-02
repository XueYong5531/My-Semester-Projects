#Xue Yong Li
#Simple Calculator

#Init
#Functions
#Add num1 with num2 and print the result
def add(num1, num2):
    result = num1 + num2 #One possible solution
    print(result)

def simplecalculator():
    print("Welcome to Simple Calculator")
while True:
    print("Select an operation: ")
    print("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit""")
    option = int(input("(1-5) Select option: "))
    if option == 1:
        int1 = input("Enter first number: ")
        int2 = input("Enter second number: ")
        print(int(int1) + int(int2))
    if option == 2:
        inte1 = input("Enter first number: ")
        inte2 = input("Enter second number: ")
        print(int(inte1) - int(inte2))
    if option == 3:
        integ1 = input("Enter first number: ")
        integ2 = input("Enter second number: ")
        print(int(integ1) * int(integ2))
    if option == 4:
        intege1 = input("Enter first number: ")
        intege2 = input("Enter second number: ")
        print(int(intege1) / int(intege2))
    if option == 5:
     break

#Main

simplecalculator()
