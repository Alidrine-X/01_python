# Programmering med Python
# Veckouppgift 1
# 4 Fler övningar
# ----------------------------------------------------------------
# Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel.
# Användaren behöver skriva in längden på de två kortare sidorna.
# Tips 1: fråga en AI om formeln Pythagoras sats, i fall du behöver. Men var noga med att inte fråga efter kod som löser uppgiften!
# "Förklara kortfattat hur formeln för Pythagoras sats fungerar."
# Tips 2: räkna ut roten med math.sqrt().

# Som testdata (alltså för att kontrollera om ditt program räknar rätt) kan du använda triangeln
# med sidorna 3, 4 och 5:

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
# 4-2
print("Uppgift 1-4-2")
# squared = x ** 2
# square_root = math.sqrt(x)

# Importera modulen math för att kunna använda funktionen sqrt till uträkning av kvadratrot
import math

print("Pythagoras sats: I varje rätvinklig triangel råder följande samband ")
print("mellan längden på triangelns sidor: a2 + b2 = c2, ")
print("där a och b är längderna på kateterna, och c är längden på hypotenusan. ")
print("Summan av kateternas kvadrater är alltså lika med hypotenusan i kvadrat.")
print("")

# Användaren får ange längd på de båda kateterna
cathetus_1_input = input("Ange längden på första kateten: ")
cathetus_2_input = input("Ange längden på andra kateten: ")

# Värde på respektive kateter i kvadrat med en decimal
cathetus_1_squared = round(float(cathetus_1_input) ** 2,1)
cathetus_2_squared = round(float(cathetus_2_input) ** 2,1)

# Värde på hypotenusan med en decimal
hypotenusa = round(math.sqrt(cathetus_1_squared + cathetus_2_squared),1)

# Skriv ut längden på hypotenusan
print("Hypotenusan i triangeln är: " + str(hypotenusa))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------

