# Programmering med Python
# Veckouppgift 1
# 3 Använda variabler och datatyper
# ----------------------------------------------------------------
# 1a Använd input för att be användaren om ett heltal.
# Spara värdet i en variabel.
# Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
# Kodexempel med input:
# x = input("Fråga här")
#
# 1b Fråga användaren efter ett annat heltal.
# Skriv ut summan av talen, alltså tal1 + tal2.
# Testa genom att hitta på två tal och räkna ut summan i huvudet.
# Kontrollera om programmet räknar rätt.
# ----------------------------------------------------------------

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
# 1a
print("Uppgift 1-3-1a")
print("")

integer_input = input("Ange ett heltal: ")
integer_int = int(integer_input)
print("Du skrev talet: " + str(integer_int))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
# 1b
print("Uppgift 1-3-1b")
print("")

integer_1 = int(input("Ange ett heltal: "))
integer_2 = int(input("Ange ett heltal till: "))
print("Summan av talen är: " + str(integer_1 + integer_2))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
