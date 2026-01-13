# Veckouppgift 1-3-2

# 3 Använda variabler och datatyper
# ----------------------------------------------------------------

# 2a Nu är det dags att köpa vinterkläder.
# Du ser en fin jacka som kostar 2000 kronor. Jackan är på rea och kostar 75% av originalpriset.
# Skriv ett program som räknar ut hur mycket du behöver betala.
# Använd variabeln:  rea_procent = 75.0
# Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.
#
# 2b Gör om programmet så att användaren kan skriva in en procentsats.
# Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det.
# Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.

# ----------------------------------------------------------------
# 2a
print("Uppgift 1-3-2a")

pris = 2000
rea_procent = 75.0
slut_pris = pris * rea_procent / 100

print("Jackans slutpris: " + str(slut_pris))
print("")
print("----------------------------------------------------------------")
# ----------------------------------------------------------------
# 2b
print("Uppgift 1-3-2b")

pris = 2000
rea_procent = int(input("Ange en procentsats: "))
slut_pris = pris - (pris * rea_procent / 100)

print("Jackans slutpris: " + str(slut_pris))
print("")
print("----------------------------------------------------------------")

# ----------------------------------------------------------------
