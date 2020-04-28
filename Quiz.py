import random, os, requests, json, Functions

os.system("cls")

url = "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"  # Hämtar en API med frågor

Frågor = requests.get(url).json()

Namn = input("Skriv in ditt namn \n>")

print("Hej " + Namn + ", du kommer få 30 frågor att svara på")
input()

nya_frågor = Functions.rightOrWrong(
    Frågor
)  # kör en funktion som gör om frågorna till bara frågorna och svaren och lägger till om svaret är rätt eller fel
Stats = Functions.go(
    nya_frågor
)  # kör funktionen med den nya dictionaryn där frågorna körs igenom

dict_out = {
    "name": Namn,
    "correct": Stats[0],
    "wrong": Stats[1],
    "streaks": Stats[2],
}  # gör en lista med ens statistik

text_file = open("Scoreboard.txt", "a")  # skriver in dictionaryn i text filen
text_file.write("\n" + str(dict_out))
text_file.close()

print("Du vann med", Stats[0], "rätta svar och", Stats[1], "fel svar.")
