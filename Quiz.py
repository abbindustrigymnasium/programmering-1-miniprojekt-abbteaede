import random, os, requests, json

os.system("cls")

a = "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"


Frågor = requests.get(a).json()

with open("bruh.json", encoding="utf-8") as txt:
    dict_text = json.loads(txt.read())
    txt.close()

Namn = dict_text["name"]
Fel = dict_text["wrong"]  # antal fel
Rätt = dict_text["correct"]  # antal rätt
Streaks = dict_text["streaks"]  # hur lång streak


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
# Gör en if sats i svaret för att om svaret är x så blir det en 2as
for i in a:
    b = i["answer"]
    random.shuffle(b)
    go = True

    while go:
        os.system("cls")
        Svar = input(
            "Fråga: "
            + i["question"]
            + "\n-----------------------------\n-Svars alternativ : 1="
            + b[0][0]
            + " 2="
            + b[1][0]
            + " 3="
            + b[2][0]
            + "\n>"
        )
        try:
            if b[int(Svar) - 1][1] == 1:
                print("Rätt svar")
                Rätt = Rätt + 1
                Streaks = Streaks + 1
                if (
                    Streaks == 5
                    or Streaks == 10
                    or Streaks == 15
                    or Streaks == 20
                    or Streaks == 25
                    or Streaks == 30
                ):
                    print("Whoop Whoop din streak är nu " + str(Streaks) + "!")
                go = False

            elif b[int(Svar) - 1][1] == 0:
                print("Fel svar")
                Fel = Fel + 1
                Streaks = 0
                go = False

        except:
            print("Vänligen välj ett av alternativen")
    input()

    os.system("cls")

dict_text["correct"] = Rätt
dict_text["wrong"] = Fel
dict_text["streaks"] = Streaks


txt = open("bruh.txt", "w")
inp = json.dumps(dict_text)
txt.write(inp)
txt.close()


print("You won with", Rätt, "correct answers and", Fel, "wrong answers.")

