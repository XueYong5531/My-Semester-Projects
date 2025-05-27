#Rocketship Succession Simulation

#Initialize
import random
import time
from PIL import Image #Code provided by instrutor
import requests #Code provided by instrutor
from io import BytesIO #Code provided by instrutor
rockettype = ["Solid Propellant Rocket","Liquid Propellant Rocket","Hybrid Rocket","Nuclear Propulsion Rocket","Plasma Rocket"]

#Functions
def open_image(url): #Function provided by instructor
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def Rocketchoice():
    print("What type of rocket would you like to use?")
    choice = int(input("Solid Propellant Rocket (1) | Liquid Propellant Rocket (2) | Hybrid Rocket (3) | Nuclear Propulsion Rocket (4) | Plasma Rocket (5)")) #INPUT that asks for which rocket the user would like to use
    print("You have chosen a " + str(rockettype[choice-1]) + "!")
    if choice == 5:
        print("Plasma Rockets use electric and magnetic fields to transform gas into plasma, which accelerates the ions in the plasma to generate a thrust.")
        open_image("https://giloshop.com/media/magefan_blog/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.PNG")
        # (Rocket Image) https://giloshop.com/blog/post/the-pulsed-plasma-rocket-a-game-changer-for-mars-missions (Author: Williams Effah Tieku)
    elif choice == 4:
        print("Nuclear Propulsion Rockets uses the heat created by nuclear fission in the reactor to heat a gas that is expelled through a tight nozzle to generate thrust.")
        open_image("https://media.npr.org/assets/img/2021/02/24/ultrasafe_wide-2c44b07e67da5362730af47403eba891305943cf.jpg?s=800&c=85&f=webp")
        # (Rocket Image) https://www.npr.org/2021/02/24/970979229/echoiceperts-ponder-nuclear-rockets-to-send-humans-to-mars (Author: Geoff Brumfiel)
    elif choice == 3:
        print("Hybrid Rockets use a solid fuel with either a liquid or gaseous oxidizer where the oxidizier reacts with the solid fuel in the combustion chamber and generating thrust.")
        open_image("https://i0.wp.com/www.drewexmachina.com/wp-content/uploads/2016/05/SpaceShipOne_15P_feature.jpg?w=890&ssl=1")
        # (Rocket Image) https://www.drewexmachina.com/2020/06/21/the-spaceflights-of-spaceshipone/ (Author: Andrew LePage)
    elif choice == 2:
        print("Liquid Propellant Rockets mix liquid fuel and an oxidizer into a combustion chamber to produce high pressurized gases which is expelled through a nozzle and generating thrust.")
        open_image("https://cdn.firespring.com/images/1342c702-38be-4aaa-89db-5663555b7ff9.jpg")
        # (Rocket Image) https://www.cradleofaviation.org/history/history/saturn-v-rocket.html (Author: Unknown))
    elif choice == 1:
        print("Solid Propellant Rockets ignite a solid propellant, which is a mixutre of fuel and oxidizier, that makes hot pressurized gases that when expelled through a nozzle, creates thrust.")
        open_image("https://www.nasa.gov/wp-content/uploads/2023/03/atlas_v.jpg") # (Rocket Image) https://www.nasa.gov/image-article/atlas-v/ (Author: NASA)
    return choice #OUTPUT that is later used as a parameter to activate the simulation

def launch(choice): #PARAMETER that determines which rocket simulation plays
    PlasmaRocketFailMessages = ["Oh No! A leak was found in the propellant system and caused an explosion!", "Oh No! The Rocket subjected to immense stress from the launch and the structure couldn't stand the pressure, leading an explosion!", "Oh No! The Plasma Engine Loss Control Over The Plasma Stream and Caused An Explosion!"]
    NuclearPropulsionRocketFailMessages = ["Oh No! The process of nuclear fission created too much heat and caused an explosion!", "Oh No! The cooling system meant to cool the system down malfunctioned, leading to a nuclear meltdown and explosion!", "Oh No! The unexpected amount of energy caused by nuclear fission collapsed the core and caused an explosion!"]
    HybridRocketFailMessages = ["Oh No! The insulation on the combustion chamber failed which caused a gas leakage and explosion!", "Oh No! There was an excess of oxidizer in the combustion chamber which caused a overpressure spike and explosion!", "Oh No! Hot gases managed to get back into the combustion chamber and ignited the oxidizers, leading to an explosion!"]
    LiquidPropellantRocketFailMessages = ["Oh No! The tank containing the liquid propellants ruptured under significant pressure and caused explosion!", "Oh No! The propellants mixed violently and combusted unexpectedly!", "Oh No! A malfunction in the ignition system caused an ignition prematurely, leading to a firely explosion!"]
    SolidPropellantRocketFailMessages = ["Oh No! Pressure oscillations were caused by combustion instability and caused an explosion!", "Oh No! The seals in the motor failed to restrict hot gases from escaping and caused an explosion!" , "Oh No! The casing that houses the propellant collapsed from the immense pressure and caused an explosion!"]
    if choice == 5:
        print("You have a 1/5 chance of reaching outer space!")
        print("Launching...")
        time.sleep(4)
        chance = random.randint(1,5)
        if chance == 1:
            print("The Plasma Rocket Successfully Reached Outer Space! Congratulations!")
            open_image("https://cdn.arstechnica.net/wp-content/uploads/2017/08/MoonCargoShipHiRes.jpg")
            # (Rocket making it to space) https://arstechnica.com/science/2017/08/nasas-plasma-rocket-making-progress-toward-a-100-hour-firing/ (Author: Eric Berger)
        else:
            open_image("https://media.npr.org/assets/img/2021/09/03/ap21246642096510-5e8a9d0a7d7af656f7a39a90ef03be10815e935e.jpg?s=800&c=85&f=webp")
            # (Rocket Fail Explosion) https://www.npr.org/2021/09/03/1034208646/firelfy-rocket-explosion-vandenberg-space-force-base. (Author: The Associated Press)
            print(random.choice(PlasmaRocketFailMessages))
    elif choice == 4:
        print("You have a 1/4 chance of reaching outer space!")
        print("Launching...")
        time.sleep(4)
        chance = random.randint(1,4)
        if chance == 1:
            print("The Nuclear Propulsion Rocket controlled its energy release and made it in outer space! Congratulations!")
            open_image("https://astronautical.org/dev/wp-content/uploads/2021/01/NPP-5.jpg")
            # (Rocket making it to space) https://astronautical.org/2021/01/22/nuclear-thermal-propulsion-old-technology-renewed-purpose/ (Author: Victoria Woodburn)
        else:
            open_image("https://cloudfront-us-east-2.images.arcpublishing.com/reuters/EHPW7SCP7NIL7AX7LVTGSHQD6E.jpg")
            # (Rocket Fail Explosion) https://www.reuters.com/lifestyle/science/spacex-rocket-explosion-illustrates-elon-musks-successful-failure-formula-2023-04-20/ (Authors: Steve Gorman and Arlene Eiras)
            print(random.choice(NuclearPropulsionRocketFailMessages))
    elif choice == 3:
        print("You have a 1/3 chance of reaching outer space!")
        print("Launching...")
        time.sleep(4)
        chance = random.randint(1,3)
        if chance == 1:
            print("The Hybrid Rocket's fuel ignition was successful and generates hot expanding gases, leading to thrust through a nozzle and making it into space!")
            open_image("https://spaceaustralia.com/sites/default/files/2022-09/Gilmour%20Space%20Eris%202.jpg")
            # (Rocket making it through space) https://spaceaustralia.com/news/gilmour-space-achieves-hybrid-rocket-milestone (Author: Vanessa Chapman)
        else:
            open_image("https://hips.hearstapps.com/hmg-prod/images/spacexs-starship-spacecraft-and-super-heavy-rocket-explodes-news-photo-1725483126.jpg?crop=1.00xw:1.00xh;0,0&resize=1200:*")
            # (Rocket Fail Explosion) https://www.popularmechanics.com/space/rockets/a62047078/starship-explosion-ionosphere/ (Author: Darren Orf)
            print(random.choice(HybridRocketFailMessages))
    elif choice == 2:
        print("You have a 1/2 chance of reaching outer space!")
        print("Launching...")
        time.sleep(4)
        chance = random.randint(1,2)
        if chance == 1:
            print("The Liquid Propellant Rocket's combustion chamber stabalized and created a lot of thrust, allowing the rocket to reach space in no time!")
            open_image("https://cdn.mos.cms.futurecdn.net/omuLtwu6he7TdLrvi7iVXC-650-80.jpg.webp")
            # (Rocket making it through space) https://www.space.com/ariane-6-new-european-rocket-delays (Author: Elizabeth Howell)
        else:
            open_image("https://headedforspace.com/wp-content/uploads/2021/08/Rocket-Explosion.jpg")
            # (Rocket Fail Explosion) https://headedforspace.com/why-rockets-explode/ (Author: Wessel Wessels)
            print(random.choice(LiquidPropellantRocketFailMessages))
    elif choice == 1:
        print("You have a 1/2 chance of reaching outer space!")
        print("Launching...")
        time.sleep(4)
        chance = random.randint(1,2)
        if chance == 1:
            print("The Solid Propellant Rocket's ignited the right measure of fuel and oxidizer and propelled through the atmosphere and into space!")
            open_image("https://www.nasaspaceflight.com/wp-content/uploads/2018/01/NSF_20180104_184644-1170x679.jpg")
            # (Rocket making it to space) https://www.nasaspaceflight.com/2018/01/atlas-v-flies-dcr-ahead-starliner-debut/ (Authors: Chris Bergin and Danny Lentz)
        else:
            open_image("https://od2-image-api.abs-cbn.com/prod/editorImage/12094139.jpg")
            # (Rocket Fail Explosion) https://www.abs-cbn.com/news/2024/3/13/japan-space-rocket-explodes-seconds-after-launch-1722 (Author: Agence France-Presse and Hiroshi Hiyama)
            print(random.choice(SolidPropellantRocketFailMessages))

def Simulation():
    print("Welcome to the Rocketship Simulation!")
    print("Users will be able to choose their type of rocket which will simulate their chances of making it through Earth's atmosphere and into Space!")
    print("Would you like to start?")
    response = int(input("Yes (1) || No (2)"))
    if response == 1:
        while True: #ITERATION that keeps the simulation running until the user quits
            choice = Rocketchoice()
            launch(choice)
            print("Would you like to restart the simulation?")
            ans = int(input("Yes (1) || No (2)"))
            if ans == 1:
                continue
            else:
                print("Thanks For Using the Simulation!")
                break
    else:
        print("Thanks For Stopping By!")
#Main
Simulation()
