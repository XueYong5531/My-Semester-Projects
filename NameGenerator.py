#Name Generator




#Init






#Functions
def name():
    print("Welcome to the Name Generator")
    print("Answer the Following Questions to Find Out Your Name")
    ans = input("Winter (W) or Summer (S) ?")
    if ans == "W" and "w":
        ans == input("Video Games (VG) or Board Games (BG) ?")
        if ans == "VG" and "vg":
            ans = input("Sparking Water (SW) or Water (W) ?")
            if ans == "SW":
                print("Your Name is Apple!")
            else:
                print("Your Name is Blackberry!")
        else:
            ans == input("Popeyes (P) or KFC (KFC) ?")
            if ans == "P" and "p":
                print("Your Name is Banana!")
            else:
                print("Your Name is Avocado!")
    else:
        ans == input("Ketchup (K) or Mustard (M) ?")
        if ans == "K" and "k":
            ans == input("Drawing (D) or Painting (P) ?")
            if ans == "D":
                print("Your Name is Cherry!")
            else:
                print("Your Name is Plum!")
        else:
            ans == input("Christmas (C) or Halloween (H) ?")
            if ans == "C":
                print("Your Name is Grape!")
            else:
                print("Your Name is Strawberry!")







#Main
name()
