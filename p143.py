# Programmering med Python
# Veckouppgift 1
# 4 Fler övningar
# ----------------------------------------------------------------
# 3a Skriv ett program som talar om dagens datum.
# Resurs: Hantera datum i Python
#
# 3b (svårare) Ändra programmet så att det kan tala om vilket datum det är om 7 dagar.
# ----------------------------------------------------------------

print("")
print("----------------------------------------------------------------")

# Importera modulen (paketet) datetime för att kunna använda
# funktionen date till att hämta dagens datum och
# funktionen timedelta för att addera antal dagar till dagens datum
import datetime

# ----------------------------------------------------------------
# 4-3
print("Uppgift 1-4-3a")
print("")

today = datetime.date.today()
print("Dagens datum är: " + str(today))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
print("Uppgift 1-4-3b")
print("")

today = datetime.date.today()
add_days = today + datetime.timedelta(days=7)
print("Det nya datumet är: " + str(add_days))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------



