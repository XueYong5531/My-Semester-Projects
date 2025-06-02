1#11/21/24
#Xue Yong Li
#Pokemon Evolution Game

#Main

#Init
import random
#Global Variables
pokemon_level = 0
pokemon_name = "Pichu"

#Functions

def train():
    global pokemon_level
    pokemon_level = pokemon_level + 1
    print("Your Pokemon did 5 pushups and gained one power level!")
    print("Your Pokemon's power level is now " + str(pokemon_level) + "!")
    evolution()
    if pokemon_level >= 10 and pokemon_level <= 20:
        print("Congratulations! Your Pichu evolved into a Pikachu!")
    if pokemon_level >= 20:
        print("Congratulations! Your Pikachu evolved into a Raichu!")

def gymbattle():
    outcome = random.randint(1,2)
    if outcome == 1:
        global pokemon_level
        global pokemon_name
        pokemon_level = pokemon_level + 2
        print(str(pokemon_name) + " entered a gym battle and won! " + str(pokemon_name) + "'s" + " power level increases by 2.")
        print(str(pokemon_name) + "'s" + " power level is now " + str(pokemon_level) + "!")
        evolution()
        if pokemon_level >= 10 and pokemon_level <= 20:
            print("Congratulations! Your Pichu evolved into a Pikachu!")
        if pokemon_level >= 20:
            print("Congratulations! Your Pikachu evolved into a Raichu!")
    else:
        pokemon_level = pokemon_level + 0
        print(str(pokemon_name) + " entered a gym battle but lost! " + str(pokemon_name) + "'s" " power level increased by 0.")

def rest():
    global pokemon_level
    global pokemon_name
    evolution()
    print(pokemon_name)
    print("Your " + str(pokemon_name) + " has a current power level of " + str(pokemon_level) + ".")
    if pokemon_level <= 10:
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠟⢻⣿⣿⣿⣿
⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠿⠋⠀⠀⠈⢡⣿⣿⡇
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣄⠀⠀⠀⠀⠀⠀⠟⠁⠀⠀⠀⠀⠀⣼⣿⣿⠁
⠀⠹⣿⣿⣿⠿⡄⠉⠉⠙⠛⠻⢿⠀⠀⠀⣀⡀⠀⠘⠄⠀⠀⠀⠀⢠⣿⣿⡟⠀
⠀⠀⠙⣿⣿⣷⡀⠀⠀⠀⠀⠀⢸⠤⠂⠁⠀⠀⠀⠀⠀⠀⠀⠠⡀⠚⠛⠛⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢤⣄⠀⠐⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⠦⢲⠁⠀⢀⢀⠀⠀⠀⠀⠀⠸⣾⡿⢃⣠⡅⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢸⠀⠐⣷⣾⡇⠀⠀⠂⠀⡀⠀⠀⣾⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣠⣤⣌⠉⠀⠀⠒⠒⠊⠀⠀⠀⢙⣟⠤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⡇⠀⠀⠀⠀⠀⣀⣤⣶⠉⠀⠀⢠⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠀⠀⠉⠉⡽⣿⣿⣿⢿⣿⠁⠀⢀⠔⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⢤⢴⠀⠋⠀⠁⠀⠉⠀⠸⣠⣴⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠘⠀⢣⠀⠀⠀⠀⠀⠀⢀⠿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⢀⠀⠀⠀⠀⠀⢀⠈⠀⠈⠻⣿⠟⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⢠⠀⠀⠐⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣀⣌⠇          """)
    if pokemon_level >= 10 and pokemon_level <= 20:
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠃⠀⠀⠐⠚⠻⢷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠙⢿⣦⣄⠀⠀⠀⠀⣼⠏⣼⣧⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⡾⢿⠐⣿⡿⠃⠀⠀⠀⢀⡖⠒⣦⡀⠀⠀⠀⠀⠈⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⢸⠀⠀⣤⡄⠀⠀⠀⢸⣧⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠀⠀
⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⡠⠃⠀⣀⡈⠀⠀⠀⠀⠘⢿⣿⣿⠟⠀⠀⠀⠀⠠⣄⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀
⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢹⡟⠓⣶⠀⠀⠀⠀⣨⣤⣤⡀⠀⠀⠀⠀⢸⣿⣶⣦⣤⣶⣾⣿⣿⣿⣆
⢠⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠘⣧⠀⠀⠈⣄⠀⡏⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣸⡟⠀⠉⠙⠛⠛⠿⠿⠿⠛
⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⣹⣿⠟⠋⠀⠀⣠⣴⡿⠿⣷⣄⠀⠈⠓⠁⠀⠀⠀⠈⠿⣿⡿⠏⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⢾⣿⣯⡀⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠛⠛⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣶⣦⣤⣀⠈⠙⢿⣶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⠃⣠⣿⢋⣽⣷⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣷⣶⣿⣧⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⠻⢦⣤⣤⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠋⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣧⡀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⢀⡗⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⠙⠓⠶⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠛⠋⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣤⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⠁⠀⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣉⣀⣀⣀⣤⣾⣿⣷⣶⣶⣶⣿⡿⠿⠿⠛⠛⠿⣷⣤⣄⡈⠀⠉⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠁⠀⠀⠀⠀""")
    if pokemon_level >= 20:
            print("""⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟫⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟫🟫⬛⬜⬜⬜⬜⬛⬛🟫🟫🟫⬛⬜⬜⬛🟨⬛⬜⬜⬜
⬜⬜⬜⬛🟫⬛⬜⬜⬜⬜⬛🟫🟫🟨🟨⬛⬜⬜⬜⬛🟨⬛⬜⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬜⬛🟫🟫🟨🟨⬛⬜⬜⬜⬜⬛🟨🟨⬛⬜⬜
⬜⬜⬛⬛🟧🟧🟧🟧⬛🟫🟫🟨🟨⬛⬜⬜⬜⬜⬜⬛🟨🟨⬛⬜⬜
⬜⬛🟧🟧🟧🟧🟧🟧⬛🟫🟫🟨🟨🟨⬛⬛⬜⬜⬜⬛🟨🟨🟨⬛⬜
⬜⬛🟧🟧🟧🟧🟧🟧⬛⬛🟫🟫⬛⬛⬜⬛⬜⬛⬛⬛🟨🟨🟨⬛⬜
⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬛⬛⬜⬜⬜⬜⬛🟨⬛🟨🟨🟨🟨⬛
⬛🟧🟧🟧🟧🟧⬜⬛🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬛🟨🟨⬛⬛🟨⬛
⬜⬛🟧🟧🟧🟧⬛⬛🟨🟨🟧🟧🟧⬛⬜⬜⬜⬜⬛🟨🟨⬛⬜⬛⬛
⬜⬜⬛🟧🟧🟧🟧🟧🟨🟨🟧🟧🟧🟧⬛⬜⬜⬜⬜⬛🟨⬛⬜⬜⬜
⬜⬛🟧⬛🟧🟧🟧🟧🟧⬛🟧🟧🟧🟫⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬛🟧⬛⬜⬜🟧⬛⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬛⬛⬛⬜⬛🟫🟧🟧🟧🟧🟧🟧🟫⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬛🟫🟫🟧⬛🟧🟧🟫🟫⬛⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬜⬛🟧⬜⬛⬛⬛🟧🟧🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛🟫⬛⬛⬛⬜⬜🟧🟧🟧🟧⬛⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫🟫🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ """)


def evolution():
    global pokemon_level
    global pokemon_name
    if pokemon_level >= 10 and pokemon_level <= 20:
        pokemon_name = "Pikachu"
    elif pokemon_level >= 20:
        pokemon_name = "Raichu"

def bossbattle():
    global pokemon_name
    global pokemon_level
    if pokemon_level <= 30:
        print("Your " + str(pokemon_name) + "s" + " power level is too low and cannot enter the battle")

    if pokemon_level >= 30 and pokemon_level <= 35:
        outcome1 = random.randint(1,4)
        print("Your pokemon has a power level between 30 and 35, meaning it has a 1/4 chance to beat the boss.")
        if outcome1 == 1:
            print("Your " + str(pokemon_name) + " challenges the final boss and barely won! Congratulations, you have beat the pokemon game!")
        else:
            print("Your " + str(pokemon_name) + " lost the boss battle! Try to train longer and come back.")

    if pokemon_level >= 35 and pokemon_level <= 40:
        outcome2 = random.randint(1,3)
        print("Your pokemon has a power level between 35 and 40, meaning it has a 1/3 chance to beat the boss.")
        if outcome2 == 1:
            print("Your " + str(pokemon_name) + " challenges the final boss and won! Congratulations, you have beat the pokemon game!")
        else:
            print("Your " + str(pokemon_name) + " lost the boss battle! Try to train longer and come back.")

    if pokemon_level >= 40 and pokemon_level <= 50:
        outcome3 = random.randint(1,2)
        print("Your pokemon has a power level between 40 and 50, meaning it has a 1/2 chance to beat the boss.")
        if outcome3 == 1:
            print("Your " + str(pokemon_name) + "challeges the final boss and one shots! Congratulations, you have beat the pokemon game!")
        else:
            print("Your " + str(pokemon_name) + " lost the boss battle! Try to train longer and come back.")
    if pokemon_level >= 50:
        print("Your pokemon has a power level of 50 or greater, meaning it instantly one shots the boss! Congratulations, you have beat the pokemon game!")

def pokemongame():
    while True:
        print("Welcome to Pokemon Evolution!")
        print("Choose today's activity: ")
        print("""1. Train
2. Gym Battle
3. Rest(Display Info)
4. Quit
5. FINAL BOSS""")
        option = int(input("What do you choose for today? (1-5)"))
        if option == 1:
            train()

        if option == 2:
            gymbattle()

        if option == 3:
            rest()

        if option == 4:
            break

        if option == 5:
            bossbattle()


#Main
pokemongame()

