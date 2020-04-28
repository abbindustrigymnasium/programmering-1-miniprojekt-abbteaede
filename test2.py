import random, os, requests, json, Functions

# from Functions import *

os.system("cls")

a = "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"


Frågor = requests.get(a).json()


Namn = "Människa"
Fel = 0
Rätt = 0
Streaks = 0


print("Hej " + Namn + ", du kommer få 30 frågor att svara på")
input()

a = []

for i in Frågor["results"]:
    b = {}

    b["question"] = i["question"]
    svar = []

    svar.append([i["correct_answer"], 1])
    for x in i["incorrect_answers"]:
        svar.append([x, 0])

    b["answer"] = svar

    a.append(b)

random.shuffle(a)

Functions.go(a)
