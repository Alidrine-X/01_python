# Programmering med Python
# Veckouppgift 1
# 2 Diskutera i grupp
# ----------------------------------------------------------------
# Denna kod ska räkna ut hur mycket som blir kvar, efter att man betalat en biljett.
# Pengarna som blir över ska du dela med en vän.
# Men koden är inte testad. Finns det några fel i koden?

# x = 100  # biljettpris
# y = 200  # pengar på fickan
# print("Det blir " + (y - x) " kronor över.")  # Saknar str() och plustecken efter
# z = y - x / 2                                 # Saknar parentes om y-x, som ska räknas ut före division med 2
# print("Varje person får " + z)                # Saknar str() (och ev int() om det önskas och inte används på fg rad)

# Försök rätta fel, så att programmet kan ge rätt svar.
# Hitta på bättre namn, i stället för x, y och z.
# ----------------------------------------------------------------

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
# Punkt 2
print("Uppgift 1-2-0")
print("")

# Räkna ut hur mycket pengar vardera person får efter att biljetten är betalad
price = 100 # biljettpris
wallet = 200 # pengar på fickan
split_in_half = int((wallet - price)/ 2)

print("Det blir " + str(wallet - price) + " kronor över.")
print("Varje person får " + str(split_in_half) + " kronor.")

# Annan lösning i gruppen att kommatecken kan användas, istället för plustecken och str()
# Notera att blanktecken utelämnats efter/före i textsträngarna, annars blir det
# dubbla blanka när det skrivs ut
#print("Det blir" , (wallet - price), "kronor över.")
#split_in_half = (wallet - price)/ 2
#print("Varje person får", int(split_in_half))

print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------





