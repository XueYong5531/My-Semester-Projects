#Xue Yong Li
#1/8/25
#Multiplication Quiz
#Init
import random



#Functions

def quiz():
    score = 0
    print("Welcome to the Multiplcation Game!")
    while True:
        num = int(input("How many questions would you like?"))
        for i in range(num):
            ran_dom = random.randint(1,10)
            ran_dom2 = random.randint(1,10)
            print("What is " + str(ran_dom) + " x " + str(ran_dom2) + "?")
            num = int(input("Enter the answer"))
            if num == ran_dom*ran_dom2:
                score = score + 1
                print("Correct! Here is the next question")
            else:
                print("That was incorrect, here is the next question")
        print("Here is the last question")
        ran_dom = random.randint(1,10)
        ran_dom2 = random.randint(1,10)
        print("What is " + str(ran_dom) + " x " + str(ran_dom2) + "?")
        if num == ran_dom*ran_dom2:
            print("Your final score is " + str(score) + ".")
        else:
            print("That was incorrect, your final score is " + str(score) + ".")
        print("Would you like to continue playing?")
        ans = int(input("yes (1) no (2)"))
        if ans == 1:
            print("Here are the next questions")
            continue
        else:
            break


#Main
quiz()
