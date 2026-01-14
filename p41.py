# Veckouppgift 1-4-1

# 4 Fler övningar
# ----------------------------------------------------------------

# Lite mer avancerad nivå.
#
# 1a Det är ca 470 km mellan Stockholm och Göteborg.
# Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg.
# Du behöver fråga användaren hur fort man ska köra, i km/h. Svara i timmar.
#
# 1b Gör så att programmet svarar i minuter i stället för timmar.
#
# 1c (svårare) Nu ska programmet svara i hela timmar och minuter.
# Tips: använd operatorerna // och %. Heltalsdivision // dividerar och avrundar nedåt till närmaste heltal.
# Procent % räknar ut resten vid division med heltal. Exempel:
# 3 // 2 == 1      (3 / 2 == 1.5, avrundar nedåt)
# 60 % 60 == 0  (ingen rest)
# 70 % 60 == 10  (10 i rest)
# Be en AI förklara heltalsdivision och modulo i Python om du känner dig osäker!

# ----------------------------------------------------------------
# 4-1a
print("Uppgift 1-4-1a")

distance = 470  # 470 km
speed = input("Ange i km/tim, vilken hastighet man får köra i? ")
time = round(distance / int(speed))
print("Det tar " + str(time) + " timmar att köra sträckan")

print("")
print("----------------------------------------------------------------")

# ----------------------------------------------------------------
# 4-1b
print("Uppgift 1-4-1b")

distance = 470  # 470 km
speed = input("Ange i km/tim, vilken hastighet man får köra i? ")
time = round(distance / int(speed) * 60)
print("Det tar " + str(time) + " minuter att köra sträckan")

print("")
print("----------------------------------------------------------------")

# ----------------------------------------------------------------
# 4-1c
print("Uppgift 1-4-1c")
# a == (a // b) * b + (a % b)

distance = 470  # 470 km
speed = int(input("Ange i km/tim, vilken hastighet man får köra i? "))
hours = distance // speed
minutes = distance % speed
print("Det tar " + str(hours) + " timmar och " + str(minutes) + " minuter att köra sträckan.")

print("")
print("----------------------------------------------------------------")

# ----------------------------------------------------------------
