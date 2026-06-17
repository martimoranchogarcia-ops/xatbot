import random
import string

print("🔵🔴 Hola! Soc BarçaBot, el teu assistent personal del FC Barcelona!")
print("Et puc fer preguntes sobre el club, jugadors, història i molt més.")
print("Escriu 'adeu' en qualsevol moment per acabar la conversa.\n")

# Demanem el nom de l'usuari
nom = input("Com et dius? ")
print("Encantat de conèixer-te, " + nom + "! 😄")
print("Comencem amb algunes preguntes sobre el Barça!\n")

# Guardem algunes respostes per fer el xat més personal
jugador_favorit = ""
visita_camp_nou = False

# Llista de preguntes
preguntes = [
    "T'agrada el FC Barcelona?",
    "Tens algun jugador del Barça favorit?",
    "Has estat mai al Camp Nou o al Spotify Camp Nou?",
    "Segueixes els partits habitualment?",
    "T'interessen les noves joventuts de La Masia?",
    "Recordes algun partit històric del Barça?",
    "Què creus que és el millor del Barça?"
]

# Guardarem les preguntes realitzades
preguntes_respostes = []

# Bucle principal
for pregunta in preguntes:
    print(f"BarçaBot: {pregunta}")
    resposta = input(f"{nom}: ").lower()

    if resposta == "adeu":
        print("BarçaBot: D'acord " + nom + ", ha estat un plaer parlar amb tu! Visca el Barça! 👋🔵🔴")
        break

    preguntes_respostes.append((pregunta, resposta))

    # FC Barcelona
    if "agrada el fc barcelona" in pregunta.lower():
        if "no" in resposta:
            print("BarçaBot: Oh... 😢 Bé, sempre tens temps per enamorar-te del millor club del món!")
        elif "si" in resposta or "sí" in resposta:
            print("BarçaBot: Així m'agrada! 🔵🔴 El Barça és més que un club.")
        else:
            print("BarçaBot: Pots respondre amb 'sí' o 'no'?")

    # JUGADOR FAVORIT
    elif "jugador" in pregunta.lower():
        jugador_favorit = resposta.capitalize()
        print(f"BarçaBot: Bona elecció! {jugador_favorit} és un gran jugador. 🔥")

    # CAMP NOU
    elif "camp nou" in pregunta.lower():
        if "si" in resposta or "sí" in resposta:
            visita_camp_nou = True
            print("BarçaBot: Brutal! És increïble viure l'ambient en directe, oi?")
        elif "no" in resposta:
            print("BarçaBot: T'hi recomano anar algun dia! És una experiència espectacular. 🏟️")
        else:
            print("BarçaBot: Pots respondre amb 'sí' o 'no'?")

    # PARTITS
    elif "partits" in pregunta.lower():
        if "si" in resposta or "sí" in resposta:
            print("BarçaBot: Perfecte! Aquests últims anys estan sent molt emocionants.")
        elif "no" in resposta:
            print("BarçaBot: Cap problema! Pots començar quan vulguis 😉")
        else:
            print("BarçaBot: Pots respondre amb 'sí' o 'no'?")

    # MASIA
    elif "masia" in pregunta.lower():
        if "si" in resposta or "sí" in resposta:
            print("BarçaBot: La Masia no falla mai! Sempre formant talent de primer nivell.")
        elif "no" in resposta:
            print("BarçaBot: Doncs t'agradarà descobrir nous talents com Lamine Yamal o Cubarsí!")
        else:
            print("BarçaBot: Pots respondre amb 'sí' o 'no'?")

    # PARTIT HISTÒRIC
    elif "partit històric" in pregunta.lower():
        if "no" in resposta:
            print("BarçaBot: Pots buscar el 2-6 al Bernabéu o el 6-1 contra el PSG. Partits legendàris!")
        else:
            print("BarçaBot: Quin partidàs! El Barça té moments inoblidables. 🔥")

    # MILLOR DEL BARÇA
    elif "millor del barça" in pregunta.lower():
        print("BarçaBot: Totalment d'acord! El Barça és especial per moltes raons. 🔵🔴")

    print()

# MENÚ FINAL BLAUGRANA

print("BarçaBot: Abans d'acabar, vols fer alguna d'aquestes opcions?")
print("1️⃣ Generar una alineació aleatòria del Barça")
print("2️⃣ Fer-me qualsevol pregunta sobre el Barça")
print("3️⃣ Repetir una de les preguntes anteriors")
print("4️⃣ Sortir")

# Llista d'un XI possible del Barça
jugadors_barca = [
    "Ter Stegen", "Koundé", "Araujo", "Cubarsí", "Balde",
    "De Jong", "Gündogan", "Pedri",
    "Lamine Yamal", "Lewandowski", "Ferran Torres"
]

while True:
    opcio = input("Tria una opció (1, 2, 3 o 4): ")

    # OPCIÓ 1 — GENERAR ALINEACIÓ
    if opcio == "1":
        print("🔵🔴 Aquí tens una alineació aleatòria del Barça:")
        random.shuffle(jugadors_barca)
        
        print("\n— 🧤 Porter:")
        print("   •", jugadors_barca[0])

        print("\n— 🛡️ Defensa:")
        for j in jugadors_barca[1:5]:
            print("   •", j)

        print("\n— ⚙️ Mig del camp:")
        for j in jugadors_barca[5:8]:
            print("   •", j)

        print("\n— ⚡ Davantera:")
        for j in jugadors_barca[8:11]:
            print("   •", j)

        print()

    # OPCIÓ 2 — Pregunta lliure
    elif opcio == "2":
        pregunta_usuari = input("Pregunta'm el que vulguis del Barça: ")
        respostes_generiques = [
            "Gran pregunta! El Barça té una història molt rica.",
            "Interessant! El Barça sempre té alguna cosa emocionant al voltant.",
            "Molt bona pregunta, " + nom + "! El Barça és un club ple de curiositats."
        ]
        print("BarçaBot:", random.choice(respostes_generiques))
        print()

    # OPCIÓ 3 — Repetir una pregunta
    elif opcio == "3":
        if not preguntes_respostes:
            print("BarçaBot: Encara no has respost cap pregunta anterior.")
        else:
            print("BarçaBot: Aquí tens les preguntes que hem fet abans:")
            for i, (preg, _) in enumerate(preguntes_respostes, 1):
                print(f"{i}. {preg}")

            idx = input("Quina pregunta vols repetir? (escriu el número): ")

            if idx.isdigit() and 1 <= int(idx) <= len(preguntes_respostes):
                pregunta = preguntes_respostes[int(idx) - 1][0]
                print(f"BarçaBot: {pregunta}")
                resposta = input(f"{nom}: ").lower()
                print("BarçaBot: Gràcies per la teva nova resposta!")
            else:
                print("BarçaBot: No és una opció vàlida.")
        print()

    # OPCIÓ 4 — Sortir
    elif opcio == "4" or opcio == "adeu":
        print("🔵🔴 --- Resum de la conversa --- 🔵🔴")
        print("Gràcies per parlar amb mi, " + nom + "!")

        if jugador_favorit:
            print("El teu jugador favorit és " + jugador_favorit + ". Gran elecció!")

        if visita_camp_nou:
            print("També hem parlat de la teva visita al Camp Nou. Experiència increïble!")

        print("Segueix gaudint del Barça! 🔵🔴 Visca el Barça i visca Catalunya!\n")
        print("Fins aviat, " + nom + "! 👋")
        break

    # OPCIÓ INVÀLIDA
    else:
        print("BarçaBot: No he entès l'opció. Tria 1, 2, 3 o 4.")
        print()
