#Xue Yong Li
#1/14/25
#Zombie Apocalypse Survival Story (Final)

#Functions
def play():
    print("Welcome to the Zombie Apocalypse Survival Story where you make decisions that will determine your ultiamte fate!")
    while True:
            health = 100
            water = 100
            stamina = 100
            Johnstamina = 100
            Johnwater = 100
            Johnhealth = 100
            print("You wake up in an abandoned city overrun by zombies, everything and everyone is gone, execpt another lone body lying next to you. Do you try to wake them up?")
            decision_1 = int(input("Wake them up (1) | Ignore them (2)"))
            if decision_1 == 1:
                print("You successfully wake them up and learn their name is John. You both agree to teamup to survive")
                print("You and John find a box of half destroyed wooden planks and started creating your shelter at impressive speeds")
                water = water - 10
                stamina = stamina - 10
                Johnstamina = Johnstamina - 10
                Johnwater = Johnwater - 10
                print("With two sets of hands working at once, you conserve a lot more energy. You and John have levels of stamina of " + str(stamina) + " and water levels of " + str(water) + ".")
                print("You and John start living comfortably in the shelter, until a sudden noise comes from the outside which prompts you both to look. You both realize it is a zombie that has started to chase you. Do you and John try to fend off against the zombie or run away?")
                decision_2 = int(input("Fight Back (1) | Run Away (2) "))
                if decision_2 == 1:
                    Johnhealth = Johnhealth - 25
                    Johnwater = Johnwater - 10
                    Johnstamina = Johnstamina - 10
                    health = health - 30
                    water = water - 10
                    stamina = stamina - 10
                    print("You and John successfully killed the zombie but the zombie put up a good fight, causing you and John to lose vital health and such.")
                    print("John's health, water and stamina: " + str(Johnhealth) + "," + " " + str(Johnwater) + "," + " " + str(Johnstamina))
                    print("Your health, water and stamina: " + str(health) + "," + " " + str(water) + "," + " " + str(stamina))
                    print("Hurt and exhausted from the battle, you and John decide to search for food.")
                    print("You and John find a perfectly clean bottle of water but covered in poisonous substances and two cans of preserved meat. Which do you take?")
                    decision_3 = int(input("Take the water (1) | Take the cans of meat (2)"))
                    if decision_3 == 1:
                        print("You try to pick up the water but instantly fall unconcious to the poisonous fumes. You later die and leave John all alone to survive")
                        print("Mourning the loss of his only companion, John gets approached by a hoard of zombies hungry for flesh. Should John fight or run away?")
                        Johndecision_1 = int(input("Take on the hoard (1) | Run Away (2)"))
                        if Johndecision_1 == 1:
                            print("John tries to fight against the hoard but without You, he ultimately fails and dies too.")
                            Johnhealth = Johnhealth - 75
                            Johnwater = Johnwater - 80
                            Johnstamina = Johnstamina - 80
                            health = health - 70
                            water = water - 80
                            stamina = stamina - 80
                            print("John's health, water and stamina: " + str(Johnhealth) + "," + " " + str(Johnwater) + "," + " " + str(Johnstamina))
                            print("Your health, water and stamina: " + str(health) + "," + " " + str(water) + "," + " " + str(stamina))
                            print("Would you like to continue playing?")
                            continue_1 = int(input("Continue playing (1) | Quit (2)"))
                            if continue_1 == 1:
                                continue
                            else:
                                break
                        else:
                            print("John tries to run away but trips over a rock, where a zombie grabs his leg and pulls him into the hoard to get eaten.")
                            Johnhealth = Johnhealth - 75
                            Johnwater = Johnwater - 80
                            Johnstamina = Johnstamina - 80
                            health = health - 70
                            water = water - 80
                            stamina = stamina - 80
                            print("John's health, water and stamina: " + str(Johnhealth) + "," + " " + str(Johnwater) + "," + " " + str(Johnstamina))
                            print("Your health, water and stamina: " + str(health) + "," + " " + str(water) + "," + " " + str(stamina))
                            print("Would you like to continue playing?")
                            continue_1 = int(input("Continue playing (1) | Quit (2)"))
                            if continue_1 == 1:
                                continue
                            else:
                                break

                    else:
                        print("You and John take the cans of meat and bash it open on a set of conincidentally placed rocks. You enjoy the meal and regain some health and stamina.")
                        Johnhealth = Johnhealth + 10
                        Johnstamina = Johnstamina + 10
                        health = health + 10
                        stamina = stamina + 10
                        print("John's health, water and stamina: " + str(Johnhealth) + "," + " " + str(Johnwater) + "," + " " + str(Johnstamina))
                        print("Your health, water and stamina: " + str(health) + "," + " " + str(water) + "," + " " + str(stamina))
                        print("After continuing to fend off zombies and living off of preserved canned food, you and John see the light from rescuing helicopters who had eradicated all the zombies and looking for survivors.")
                        print("You are thankful because John is in critical condition, as you fought zombies out of your shelter during the night when one got to John.")
                        print("You and John esacpe on the helicopters with okay vitals while John is in urgent care.")
                        Johnhealth = Johnhealth - 73
                        Johnwater = Johnwater - 67
                        Johnstamina = Johnstamina - 71
                        health = health - 35
                        water = water - 26
                        stamina = stamina - 53
                        print("John's health, water and stamina: " + str(Johnhealth) + "," + " " + str(Johnwater) + "," + " " + str(Johnstamina))
                        print("Your health, water and stamina: " + str(health) + "," + " " + str(water) + "," + " " + str(stamina))
                        print("Would you like to continue playing?")
                        continue_2 = int(input("Continue (1) | Quit (2)"))
                        if continue_2 == 1:
                            continue
                        else:
                            break
                else:
                    print("You and John try to run away from the zombie but you both run into each other and fall. The zombie catches up to you and starts to eat John while you get mauled by another suspecting zombie")
                    Johnhealth = 0
                    Johnwater = 0
                    Johnstamina = 0
                    health = 0
                    water = 0
                    stamina = 0
                    print("John's health, water and stamina: " + str(Johnhealth) + "," + " " + str(Johnwater) + "," + " " + str(Johnstamina))
                    print("Your health, water and stamina: " + str(health) + "," + " " + str(water) + "," + " " + str(stamina))
                    print("Would you like to continue playing?")
                    continue_1 = int(input("Continue playing (1) | Quit (2)"))
                    if continue_1 == 1:
                            continue
                    else:
                        break

            else:
                print("You ignore the body and continue to venture throughout the city for supplies.")
                print("That is until you find a box of half destroyed wooden planks and attempt to create a shelter but is tough with just one person.")
                water = water - 20
                stamina = stamina - 20
                print("The draining task depletes a lot of your energy, where your water percentage is now " + str(water) + " and your stamina percentage is at " + str(stamina) + ".")
                print("You realize surviving on your is harder than you realized it, so you return to the body to try to wake them up.")
                print("To your horror, you see a scene of three zombies feasting on the unconcious body, knowing you are prey next.")
                print("You try to run as fast as you can but one of them catches up to you, slamming your face into the dirt and starts to eat you limb by limb.")
                health = 0
                water = 0
                stamina = 0
                print("Your health, water and stamina: " + str(health) + "," + " " + str(water) + "," + " " + str(stamina))
                print("Would you like to continue playing?")
                continue_4 = int(input("Continue (1) | Quit (2)"))
                if continue_4 == 1:
                    continue
                else:
                    break

#Main
play()
