#Xue Yong Li
#2/5/25
#Tetris Score Analysis
# List of Tetris scores (unsorted)
scores = [3600460, 1388900, 5435960, 4222920, 8063900, 1362703, 6529560, 2043580, 1390000, 1696224,
    1372600, 2535840, 2605320, 2275996, 11966100, 1472600, 1390780, 1768400, 1333731, 1317580,
    1777456, 4899280, 2790920, 1626880, 1476400, 29486164, 4570640, 1649100, 4890220, 6492500,
    1614120, 5157860, 1582980, 1357480, 2382340, 1532660, 2378832, 1316520, 2529080, 13793540,
    1386260, 1352620, 1442340, 1406260, 1705680, 12409180, 2281848, 3222400, 1349060, 2302480,
    1571120, 3067100, 3740500, 1606732, 2153480, 2011360, 1344740, 1371060, 1345420, 2373940,
    1702940, 2077552, 2108820, 1322485, 1404800, 2555620, 1405580, 4213540, 3835120, 6563440,
    1350742, 1537800, 1657560, 1333995, 1632505, 2743060, 1509751, 1554880, 1316540, 1323680,
    2433160, 1340460, 1659860, 1608500, 7220241, 1834120, 7081880, 1483360, 16700760, 1435280,
    1702640, 1371040, 1316900, 2114180, 1374100, 1412260, 1379220, 1319573, 1623160, 6787420]

#Functions
#1. Create a function that finds and prints the highest score in the list.
def highscore():
    global scores
    max = 0
    for number in scores:
        if number > max:
            max = number
    print(max)

#2. Create a function that finds and prints the lowest score in the list.
def lowestscore():
    global scores
    low = 100000000000000
    for number in scores:
        if number < low:
            low = number
    print(low)
    return low
#3. Create a function that calculates and prints the average score in the list.
def avgScore():
    global scores
    sum = 0
    for number in scores:
        sum = sum + number
    print(sum/100)

#4. Create a function that allows the user to input a score. If the score is greater than the lowest score on the tetris score list, remove the lowest score and the new score will be added to the list. Reject any scores that are not in the top 100 scores.
def newScore():
    global scores
    tetrisscore = int(input("Enter your tetris score"))
    if tetrisscore > lowestscore():
        scores.remove(lowestscore())
        scores.append(tetrisscore)
        print("Congratulations your score is within the top 100!")
        print("The new leaderboard for tetris is ")
        print(scores)
    else:
        print("Your score is not higher than the top 100")

def tetrisanalysis():
    ("Welcome to Tetris Analysis, what would you like to do?")
    print("""1. Find Largest Score
2. Find Smallest Score
3. Find Average Score
4. Input Your Own Score""")
    ans = int(input("Enter your option (1-4)"))
    if ans == 1:
        highscore()
    elif ans == 2:
        lowestscore()
    elif ans == 3:
        avgScore()
    elif ans == 4:
        newScore()

#Main
tetrisanalysis()
