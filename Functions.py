import random, os, requests, json


def rightOrWrong(Frågor):
    a = []  # skapar en lista
    for i in Frågor["results"]:  # Frågor är en lista med dictionarys som körs igenom
        b = {}  # skapar en dictionary med bara frågan och svaren
        b["question"] = i["question"]
        svar = (
            []
        )  # Gör en lista där det läggs till 1 om svaret är rätt och 0 om svaret är fel

        svar.append([i["correct_answer"], 1])

        for x in i["incorrect_answers"]:
            svar.append([x, 0])

        b["answer"] = svar  # lägger till svaren i dictionaryn b som en lista

        a.append(b)  # lägger till dictionaryn b i listan a

    return a  # när det har gjorts med alla dictionarys i Frågor skickas a tillbaka


def go(a):
    Streaks = 0  # definerar värden
    Rätt = 0
    Fel = 0

    for i in a:  # för varje i listan
        b = i[
            "answer"
        ]  # sätter svaren hos frågorna som b och sätter dem i en slumpmässig ordning
        random.shuffle(b)
        t = True  # sätter t som true

        while t:  # körs när t är true
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
            )  # Skriver ut frågorna och svaren, [0] är för att få om det är rätt eller fel

            try:
                if (
                    b[int(Svar) - 1][1] == 1
                ):  # Om ens svar minus 1 har [1] lika med 1 är svaret rätt
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
                    t = False  # sätter t som false för att köra nästa fråga

                elif (
                    b[int(Svar) - 1][1] == 0
                ):  # Om ens svar minus 1 har [1] lika med 0 är svaret fel
                    print("Fel svar")
                    Fel = Fel + 1
                    Streaks = 0
                    t = False

            except:  # körs om svaret inte är en siffra
                print("Vänligen välj ett av alternativen")

        input()
        os.system("cls")

    return (
        Rätt,
        Fel,
        Streaks,
    )  # skickar tillbaka värdena när alla frågor har körts igenom
