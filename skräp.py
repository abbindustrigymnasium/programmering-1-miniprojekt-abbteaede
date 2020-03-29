import random, os, requests, json, Functions

os.system("cls")

# frågor_från_opentdb = Functions.Frågor(
#     "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"
# )

with open("bruh.json", encoding="utf-8") as txt:
    score_list = json.loads(txt.read())
    txt.close()

Namn = ""
Fel = 0
Rätt = 0
Streaks = 0

print("Hej " + Namn + ", du kommer få 30 frågor att svara på")
input()

hej = Functions.Frågor(
    "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"
)

hejsan = Functions.rightOrWrong(hej)

random.shuffle(hejsan)

tjoho = Functions.go(hejsan)

print(tjoho)
# from FrågeBot import FrågeBot

# Frågebot = FrågeBot(randomize=False, verbose=True) # Initiera frågebotten, randomisera svars alternativ                                                       # Skriv också ut om det bler rätt eller fel
# Frågebot.loadConfig("frågor.json", file=True) # ladda frågor fån en fil (kan vara string eller dict också)
# Frågebot.fråga(randomize=True) # Fråga alla fråga i slumpmässig ordning
# Frågebot.finalscore() # visa slutresultat

