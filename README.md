# Quiz om spel
Det är ett program gjort i python som har 30 frågor angående olika spel på en svår nivå där det finns tre olika val alternativ.

Frågorna är hämtade ifrån en API som sedan kommer köras igenom. Det finns ett rätt och två fel på varje fråga och svaren kommer i en slumpad ordning varje gång. Om du antingen får rätt eller fel sparas det i en poängräknare som även hela tiden sparar din högsta streak under spelets gång. 

När frågorna har körts igenom får man reda på antalet rätt och fel man hade och resultaten sparas i en text fil med ditt namn som du skriver in i början.

Frågorna är hämtade ifrån denna API "https://opentdb.com/api.php?amount=30&category=15&difficulty=hard&type=multiple"

# Hur man kör det
Om du inte redan har python kan du ladda ner det härifrån - https://www.python.org/downloads/

För att starta programmet kan du trycka ner ctrl+alt+p för att komma till command line där du skriver "python" för att köra programmet.
# Hur det fungerar
![Bild på systemet](https://github.com/abbindustrigymnasium/programmering-1-miniprojekt-abbteaede/blob/master/Quiz%20i%20steg.png)

Jag har valt att exportera funktionerna från Functions.py som en modul för att ha en organiserad kod. Highscoren sparas i en serperat text fil kallad scoreboard.txt.

