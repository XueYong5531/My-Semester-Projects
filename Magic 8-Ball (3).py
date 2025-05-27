#Xue Yong Li
#1/24/25
#Magic 8 Ball

#Init
import random
import time
Magiclist = ["Of Course!", "Definitely!", "Yes!", "Certainly!", "Absoluetly!", "No!", "Definitely NOT!", "Certainly NOT!", "Absolutely NOT!", "Of Course NOT!", "Maybe", "Could Happen", "Perhaps", "Possibly", "Perchance"]

#Fuctions
def magicball():
    while True:
        print("Welcome to the Magic 8-Ball Game!")
        print("Please enter a question")
        try:
            question = input("Enter your question (a yes/no question and include a question mark!): ")
            if '?' not in question:
                raise ValueError("YOUR QUESTION MUST INCLUDE A QUESTION MARK!")
            print("Oh Magic 8-Ball. " + str(question))
            print("shake...")
            time.sleep(2)
            print("shake....")
            time.sleep(2)
            print("shake.....")
            time.sleep(2)
            print("shake.......")
            time.sleep(2)
            print("The ball says " + str(random.choice(Magiclist)))
        except ValueError as e:
            print(e)
            continue

        ans = int(input("Would you like to continue playing? (Yes (1) No (2)): "))
        if ans == 1:
            continue
        else:
            print("Thanks for playing!")
            break
#Main
magicball()
