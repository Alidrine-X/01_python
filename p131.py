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

# Användaren ombeds skriva in ett tal
# Inmatat värde omvandlas till ett heltal och skrivs ut
value_input = input("Ange ett heltal: ")
value_int = int(value_input)
print("Du skrev talet: " + str(value_int))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
# 1b
print("Uppgift 1-3-1b")
print("")

# Användaren ombeds skriva in två tal
value_1 = input("Ange ett heltal: ")
value_2 = input("Ange ett heltal till: ")

# Inmatade värden omvandlas till heltal
value_1_int = int(value_1)
value_2_int = int(value_2)

# Summera och skriv ut inmatade tal
print("Summan av talen är: " + str(value_1_int + value_2_int))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
