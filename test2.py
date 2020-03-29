# import random, os, requests, json


# def Frågor(url):
#     a = url
#     return requests.get(a).json()

#     c = []
#     for i in a["results"]:
#         b = {}
#         b["question"] = i["question"]
#         svar = []

#         svar.append([i["correct_answer"], 1])

#         for x in i["incorrect_answers"]:
#             svar.append([x, 0])

#         b["answer"] = svar

#         c.append(b)

#     return c


# def go(a):
#     for i in a:
#         b = i["answer"]
#         random.shuffle(b)
#         go = True

#         while go:
#             os.system("cls")
#             Svar = input(
#                 "Fråga: "
#                 + i["question"]
#                 + "\n-----------------------------\n-Svars alternativ : 1="
#                 + b[0][0]
#                 + " 2="
#                 + b[1][0]
#                 + " 3="
#                 + b[2][0]
#                 + "\n>"
#             )
#             try:
#                 if b[int(Svar) - 1][1] == 1:
#                     print("Rätt svar")
#                     Rätt = Rätt + 1
#                     Streaks = Streaks + 1
#                     if (
#                         Streaks == 5
#                         or Streaks == 10
#                         or Streaks == 15
#                         or Streaks == 20
#                         or Streaks == 25
#                         or Streaks == 30
#                     ):
#                         print("Whoop Whoop din streak är nu " + str(Streaks) + "!")
#                     go = False

#                 elif b[int(Svar) - 1][1] == 0:
#                     print("Fel svar")
#                     Fel = Fel + 1
#                     Streaks = 0
#                     go = False

#             except:
#                 print("Vänligen välj ett av alternativen")
#         input()


# frågor_från_opentdb = Frågor(
#     "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"
# )

