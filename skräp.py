# import requests, random, json

# a = "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"


# Frågor = requests.get(a).json()

# print(Frågor["response_code"])


# questions = Frågor["results"]

# myquestions = {}

# print(a.json())

# random.shuffle(questions)
# arr = []


# for i in questions:
#     arr.clear()
#     arr.append(i["correct_answer"])
#     arr.append(i["incorrect_answers"])
# print(arr)


# '
# {'response_code': 0, 'results':
# [
#     {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which of these TrackMania environments was NOT in the original game?', 'correct_answer': 'Bay', 'incorrect_answers': ['Desert', 'Snow', 'Rally']},
#     {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which one of the following titles by Valve is not based on a Community Mod?', 'correct_answer': 'Ricochet', 'incorrect_answers': ['Day of Defeat', 'Counter-Strike', 'Alien Swarm']},
#     {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'The map featured in Arma 3 named &quot;Altis&quot; is based off of what Greek island?', 'correct_answer': 'Lemnos', 'incorrect_answers': ['Ithaca', 'Naxos', 'Anafi']},
#     {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'How many copies of the notorious E.T. game for the Atari 2600 did Atari end up selling?', 'correct_answer': '1.5 Million', 'incorrect_answers': ['1 Million', '250 Thousand', 'Less than 250 Thousand']},
#     {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Why was the character Trevor Philips discharged from the Air Force?', 'correct_answer': 'Mental Health Issues', 'incorrect_answers': ['Injuries', 'Disease', 'Danger to Others']},
#     {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In the Animal Crossing series, which flower is erroneously called the &quot;Jacob&#039;s Ladder&quot;?', 'correct_answer': 'Lily of the Valley', 'incorrect_answers': ['Hydrangea', 'Harebell', 'Yarrow']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Meryl Silverburgh, a video game character from the Metal Gear series, was originally a character in which game?', 'correct_answer': 'Policenauts', 'incorrect_answers': ['Gradius', 'Contra', 'Castlevania: Symphony of the Night']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'According to Toby Fox, what was the method to creating the initial tune for Megalovania?', 'correct_answer': 'Singing into a Microphone', 'incorrect_answers': ['Playing a Piano', 'Using a Composer Software', 'Listened to birds at the park']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which was the first M-rated video game developed by Squaresoft/Square Enix?', 'correct_answer': 'Parasite Eve', 'incorrect_answers': ['Final Fantasy VIII', 'Front Mission', 'Vagrant Story']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What animal is on Link&#039;s pajamas in The Legend of Zelda: The Wind Waker?', 'correct_answer': 'Crawfish', 'incorrect_answers': ['Lobster', 'Salmon', 'Swordfish']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In Xenoblade Chronicles X, which class has a sniper rifle as it&#039;s primary weapon?', 'correct_answer': 'Partisan Eagle', 'incorrect_answers': ['Blast Fencer', 'Winged Viper', 'Bastion Warrior']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In the game Danganronpa: Happy Trigger Havoc, the character Aoi Asahina&#039;s ultimate ability is what?', 'correct_answer': 'Ultimate Swimmer', 'incorrect_answers': ['Ultimate Detective', 'Ultimate Gambler', 'Ultimate Dancer']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In Animal Crossing: New Leaf, which of these paintings from Redd&#039;s Art Gallery is always genuine?', 'correct_answer': 'Warm Painting',
# 'incorrect_answers': ['Jolly Painting', 'Neutral Painting', 'Wistful Painting']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What do the video games No Man&rsquo;s Sky and Mighty No. 9 have in common?', 'correct_answer': 'Both were announced in 2013.', 'incorrect_answers': ['Both were crowdfunded.', 'Both were developed by indie studios.', 'Both were released for the PlayStation 3.']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'How many trophies are there in &quot;Super Smash Bros. for Nintendo 3DS&quot;?', 'correct_answer': '685', 'incorrect_answers': ['1360', '716', '1155']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which of these games was NOT developed by Markus Persson?', 'correct_answer': 'Dwarf Fortress', 'incorrect_answers': ['Minecraft', 'Wurm Online', '0x10c']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which of the following games in the The Legend of Zelda franchise was released in Japan before North America?', 'correct_answer': 'The Legend of Zelda: The Minish Cap', 'incorrect_answers': ['The Legend of Zelda: Twilight Princess', 'The Legend of Zelda: Spirit Tracks', 'The Legend of Zelda: Four Swords']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which variant of the MP5 is depicted in Counter-Strike 1.6?', 'correct_answer': 'MP5N', 'incorrect_answers': ['MP5SD', 'MP5K', 'MP5RAS']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In the &quot;Little Lost Girl&quot; Easter Egg in Call of Duty: Black Ops II, what&#039;s the last step required for the achievement?', 'correct_answer': 'Raise Hell', 'incorrect_answers': ['Freedom', 'Skewer the Winged Beast', 'Ascend from Darkness']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What programming language was used to create the game &quot;Minecraft&quot;?', 'correct_answer': 'Java', 'incorrect_answers': ['HTML 5', 'C++', 'Python']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What was the first &quot;Call Of Duty: Zombies&quot; map to be directed
# by Jason Blundell?', 'correct_answer': 'Mob Of The Dead', 'incorrect_answers': ['Buried', 'Origins', 'Moon']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In &quot;Call Of Duty: Zombies&quot;, &quot;Richtofen&quot; is in possession of two filled blood vials belonging to who?', 'correct_answer': 'Sal DeLuca and Finn O&#039;Leary', 'incorrect_answers': ['Richtofen', 'Al Arlington and Sal DeLuca', 'Jessica Rose and Jack Vincent']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In &quot;Pok&eacute;mon Sun and Moon&quot;, Team Skull took over which town?', 'correct_answer': 'Po Town', 'incorrect_answers': ['Heahea City', 'Tapu Village', 'Iki Town']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In &quot;The Witness&quot;, how many lasers must be activated to get into the mountain area?', 'correct_answer': '7', 'incorrect_answers': ['8', '5', '12']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'In which game did the character &quot;Mario&quot; make his first appearance?', 'correct_answer': 'Donkey Kong', 'incorrect_answers': ['Super Mario Bros.', 'Super Mario Land', 'Mario Bros.']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'Which gaming series includes &quot;The Diabolical Box&quot; and &quot;The Curious Village&quot;?', 'correct_answer': 'Professor Layton', 'incorrect_answers': ['Persona', 'Etrian Odyssey', 'Sam &amp; Max']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': '&quot;Exile&quot; and &quot;Revelations&quot; were the third and fourth installments of which PC game series?', 'correct_answer': 'Myst', 'incorrect_answers': ['Shivers', 'Doom', 'Tropico']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What vault in the video game &quot;Fallout 3&quot; is the home of multiple clones named Gary?', 'correct_answer': 'Vault 108', 'incorrect_answers': ['Vault 101', 'Vault 87', 'Vault 21']}, {'category': 'Entertainment: Video Games', 'type': 'multiple', 'difficulty': 'hard', 'question': 'What is the name of the alien species introduced in Shadow the Hedgehog (2005)?', 'correct_answer': 'Black Arms', 'incorrect_answers': ['The Swarm', 'Black Hive', 'The Eclipse']}, {'category': 'Entertainment: Video Games', 'type': 'multiple',
# 'difficulty': 'hard', 'question': 'The creation of the  Entertainment Software Ratings Board (ESRB) is often associated with Mortal Kombat and what FMV video
# game?', 'correct_answer': 'Night Trap', 'incorrect_answers': ['Sewer Shark', 'The Daedalus Encounter', 'Corpse Killer']}]}'

# a = []

# for i in Frågor["results"]:
#     b = {}
#     b["question"] = i["question"]
#     svar = []

#     svar.append([i["correct_answer"], 1])

#     for x in i["incorrect_answers"]:
#         svar.append([x, 0])

#     b["answer"] = svar

#     a.append(b)

# print(a)
