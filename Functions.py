import random, os, requests, json


def Frågor(url):
    a = url
    return requests.get(a).json()


# frågor_från_opentdb = Frågor(
#     "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"
# )

# rightOrWrong(frågor_från_opentdb)


def rightOrWrong(Frågor):
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

    return a


def go(a):
    print("he222jsan")
    streaks = 0
    for i in a:
        b = i["answer"]
        random.shuffle(b)
        t = True

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
            print("he222jsan")
            try:
                print("hejsan")
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
                    t = False

                elif b[int(Svar) - 1][1] == 0:
                    print("Fel svar")
                    Fel = Fel + 1
                    Streaks = 0
                    t = False

            except:
                print("Vänligen välj ett av alternativen")
        input()

        os.system("cls")

    return Rätt, Fel, Streaks
