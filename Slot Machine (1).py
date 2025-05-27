#Xue Yong Li
#1/28/25
#Slot Machine Project

#Init
symbols = ["7","♦","♣"]
credits = 100
import random
import time

#Functions
def slotmachine():
    global credits
    global ans
    global ans2
    print("===== Welcome to the 3-Slot Machine =====")
    print("Would You like to Play?")
    ans = int(input("Would you like to Spin? (1) I Would Not Like to Spin (2)"))
    while True:
        slot1 = random.choices([0,1,2], weights= [1,3,0.1], k = 1)[0]
        slot2 = random.choices([0,1,2], weights= [1,3,0.1], k = 1)[0]
        slot3 = random.choices([0,1,2], weights= [1,3,0.1], k = 1)[0]
        if credits >= 10 and ans == 1:
            print("Would you like to place a bet?")
            print("You have " + str(credits) + " credits.")
            betans = int(input("Would you like to bet a set amount at once? (1) Yes | (2) No "))
            if betans == 1:
                amount = int(input("How much would you like to bet at once? ( <50 = 2.5x | 50+ = 5x | 100+ = 10x | 200+ = 25x)"))
                credits = credits - amount
                print("Spinning...")
                time.sleep(1)
                print(symbols[slot1] + symbols[slot2] + symbols[slot3])
                if slot1 == 1 and slot2 == 1 and slot3 == 1:
                    print("Congratulations! You have just won!")
                    if amount >= 200:
                        credits = credits * 25
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 100:
                        credits = credits * 10
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 50:
                        credits = credits * 5
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    else:
                        credits = credits * 2.5
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break

                elif slot1 == 2 and slot2 == 2 and slot3 == 2:
                    print("Congratulations! You have just won!")
                    if amount <= 50:
                        credits = credits * 25
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 50:
                        credits = credits * 5
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 100:
                        credits = credits * 10
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 200:
                        credits = credits * 25
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break

                elif slot1 == 0 and slot2 == 0 and slot3 == 0:
                    print("CONGRATULATIONS! YOU HAVE JUST HIT THE JACKPOT!")
                    if amount <= 50:
                        credits = credits * 5
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 50:
                        credits = credits * 10
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 100:
                        credits = credits * 25
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                    elif amount >= 200:
                        credits = credits * 50
                        print("Your total credits amount is now " + str(credits))
                        print("Would you like to continue playing?")
                        ans2 = int(input("Yes (1) No (2)"))
                        if ans2 == 1:
                            continue
                        else:
                            break
                else:
                    print("You have just lost!")
                    print("Your total credits amount is now " + str(credits))
                    print("Would you like to continue playing?")
                    ans = int(input("Yes (1) No (2)"))
                    if ans == 1:
                        continue
                    else:
                        print("Thanks for Playing!")
                        print("Your final amount of credits is " + str(credits) + ".")
                        break
            if credits <= 0:
                print("Oh No! You have ran out of credits and cannot play anymore. Please go spend more money for credits!")
                break


            else:
                credits = credits - 20
                print("Spinning...")
                time.sleep(1)
                print(symbols[slot1] + symbols[slot2] + symbols[slot3])
                if slot1 == 1 and slot2 == 1 and slot3 == 1:
                    credits = credits + 40
                    print("Congratulations! You have just won!")
                    print("Your total credits amount is now " + str(credits))
                    print("Would you like to continue playing?")
                    ans2 = int(input("Yes (1) No (2)"))
                    if ans2 == 1:
                        continue
                    else:
                        break

                if slot1 == 2 and slot2 == 2 and slot3 == 2:
                    credits = credits + 40
                    print("Congratulations! You have just won!")
                    print("Your total credits amount is now " + str(credits))
                    print("Would you like to continue playing?")
                    ans2 = int(input("Yes (1) No (2)"))
                    if ans2 == 1:
                        continue
                    else:
                        break

                elif slot1 == 0 and slot2 == 0 and slot3 == 0:
                    credits = credits + 200
                    print("CONGRATULATIONS! YOU HAVE JUST HIT THE JACKPOT!")
                    print("Your total credits amount is now " + str(credits))
                    print("Would you like to continue playing?")
                    ans2 = int(input("Yes (1) No (2)"))
                    if ans2 == 1:
                        continue
                    else:
                        break
                else:
                    print("You have just lost!")
                    print("Your total credits amount is now " + str(credits))
                    print("Would you like to continue playing?")
                    ans = int(input("Yes (1) No (2)"))
                    if ans == 1:
                        continue
                    else:
                        print("Thanks for Playing!")
                        print("Your final amount of credits is " + str(credits) + ".")
                        break
        if credits <= 0:
                print("Oh No! You have ran out of credits and cannot play anymore. Please go spend more money for credits!")
                break


#Main
slotmachine()

