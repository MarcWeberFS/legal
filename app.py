import re

legalArticles = {
    "Art. 7 USG": (
        "Einwirkungen sind Luftverunreinigungen, Lärm, Erschütterungen, Strahlen, Gewässerverunreinigungen oder "
        "andere Eingriffe in Gewässer, Bodenbelastungen, Veränderungen des Erbmaterials von Organismen oder der "
        "biologischen Vielfalt, die durch den Bau und Betrieb von Anlagen, durch den Umgang mit Stoffen, Organismen "
        "oder Abfällen oder durch die Bewirtschaftung des Bodens erzeugt werden.\n"
        "Luftverunreinigungen, Lärm, Erschütterungen und Strahlen werden beim Austritt aus Anlagen als Emissionen, "
        "am Ort ihres Einwirkens als Immissionen bezeichnet.\n"
        "Luftverunreinigungen sind Veränderungen des natürlichen Zustandes der Luft, namentlich durch Rauch, Russ, "
        "Staub, Gase, Aerosole, Dämpfe, Geruch oder Abwärme.\n"
        "Dem Lärm sind Infra- und Ultraschall gleichgestellt."
    ),
    "Art. 11 USG": (
        "Luftverunreinigungen, Lärm, Erschütterungen und Strahlen werden durch Maßnahmen bei der Quelle begrenzt "
        "(Emissionsbegrenzungen)."
    ),
    "Art. 12 USG": (
        "Emissionen werden eingeschränkt durch den Erlass von:\n"
        "a. Emissionsgrenzwerten;\n"
        "b. Bau- und Ausrüstungsvorschriften;\n"
        "c. Verkehrs- oder Betriebsvorschriften;\n"
        "d. Vorschriften über die Wärmeisolation von Gebäuden;\n"
        "e. Vorschriften über Brenn- und Treibstoffe.\n"
        "Begrenzungen werden durch Verordnungen oder, soweit diese nichts vorsehen, durch unmittelbar auf dieses "
        "Gesetz abgestützte Verfügungen vorgeschrieben."
    ),
    "Art. 13 USG": (
        "Für die Beurteilung der schädlichen oder lästigen Einwirkungen legt der Bundesrat durch Verordnung "
        "Immissionsgrenzwerte fest.\n"
        "Er berücksichtigt dabei auch die Wirkungen der Immissionen auf Personengruppen mit erhöhter "
        "Empfindlichkeit, wie Kinder, Kranke, Betagte und Schwangere."
    ),
    "Art. 15 LSV": (
        "Die Immissionsgrenzwerte für Lärm und Erschütterungen sind so festzulegen, dass nach dem Stand der "
        "Wissenschaft oder der Erfahrung Immissionen unterhalb dieser Werte die Bevölkerung in ihrem Wohlbefinden "
        "nicht erheblich stören."
    ),
    "Art. 19 LSV": (
        "Dieser Artikel behandelt den baulichen Lärmschutz, der Maßnahmen zur Verringerung der Lärmemissionen von "
        "Gebäuden umfasst."
    ),
    "Art. 22 LSV": (
        "Dieser Artikel beschreibt spezifische Maßnahmen zur Verringerung von Lärmimmissionen in Wohngebieten und "
        "anderen schützenswerten Bereichen."
    ),
    "APV Zürich - Lärm": (
        "Der Lärm- und Immissionsschutz ist vollständig in die APV integriert und nicht mehr in einer separaten "
        "Lärmschutzverordnung geregelt. Eine Unterscheidung zwischen verschiedenen Lärmarten wie beispielsweise "
        "Arbeits-, Haushalts-, Gartenarbeiten- und Freizeitlärm wird nicht mehr gemacht.\n"
        "Die Nachtruhe dauert von 22.00–7.00 Uhr, während der Sommerzeit freitags und samstags beginnt die "
        "Nachtruhe erst um 23.00 Uhr. Während der Nachtruhe ist störendes Verhalten verboten.\n"
        "Mittags von 12.00–13.00 Uhr, abends ab 20.00 Uhr und sonntags ist dem Erholungsbedürfnis der Bevölkerung "
        "besonders Rechnung zu tragen, indem lärmintensives Verhalten zu unterlassen ist. Hier ist die "
        "Toleranzgrenze höher angesetzt als bei der eigentlichen Nachtruhe."
    ),
    "APV Zürich - Ruhezeiten": (
        "Bauarbeiten, die störenden Lärm verursachen, sind grundsätzlich von 12.00–13.00 Uhr und von 19.00–7.00 Uhr "
        "ebenfalls verboten. Die Benutzung von Wertstoffsammelstellen ist werktags von 20.00–7.00 Uhr und sonntags "
        "untersagt."
    ),
    "APV Zürich - Lautsprecheranlagen": (
        "Lautsprecher im Freien, in Fahrnisbauten und in Zelten dürfen nur mit Polizeibewilligung betrieben werden."
    ),
    "APV Zürich - Weitere Immissionen": (
        "Das Verbrennen von Grünabfällen in Wohngebieten und das Verwenden von Skybeamern sind nicht zugelassen. "
        "Das Abbrennen von Feuerwerk ist am 1. August und in der Nacht auf den 2. August sowie in der Nacht vom 31. "
        "Dezember auf den 1. Januar gestattet."
    )
}

decibelFines = {
    "70-79": 50,
    "80-89": 100,
    "90-99": 200,
    "100+": 400
}

timeMultipliers = {
    "day": 1.0,
    "night": 1.5
}


def calculateFine():
    print("\nBerechne Lärmbelästigungsgeld in der Stadt Zürich")
    print("=================================================")
    
    try:
        decibels = int(input("Gebe den Lärmpegel in Decibels (dB) ein: "))
        if decibels < 70:
            print("Lärmpegel zu tief für eine Geldstrafe.")
            return
    except ValueError:
        print("Ungültiger Wert für Lärmpegel. Bitte gebe eine Nummer ein.")
        return

    if 70 <= decibels < 80:
        baseFine = decibelFines["70-79"]
    elif 80 <= decibels < 90:
        baseFine = decibelFines["80-89"]
    elif 90 <= decibels < 100:
        baseFine = decibelFines["90-99"]
    elif decibels >= 100:
        baseFine = decibelFines["100+"]
    else:
        print("Ungültiger Wert für Dezibel, bitte eine Nummer eingeben.")
        return

    try:
        duration = float(input("Dauer der Lärmbelästigung in Stunden: "))
    except ValueError:
        print("Ungültiger Wert für die Dauer. Bitte gebe eine Nummer ein.")
        return

    timeOfDay = input("Gebe die Tageszeit an (day/night): ").strip().lower()
    if timeOfDay in timeMultipliers:
        multiplier = timeMultipliers[timeOfDay]
    else:
        print("Unbekannte Tageszeit. Bitte gebe 'day' oder 'night' ein.")
        return

    try:
        priorConvictions = int(input("Anzahl der vorherigen Verstösse: "))
        if priorConvictions < 0:
            raise ValueError("Anzahl der vorherigen Verstösse kann nicht negativ sein.")
    except ValueError as e:
        print(f"Ungültiger Wert: {e}")
        return

    calculatedFine = baseFine

    if duration > 1:
        calculatedFine += baseFine * 0.5 * (duration - 1)

    calculatedFine *= multiplier
    calculatedFine += priorConvictions * 50

    if calculatedFine > 500:
        calculatedFine = 500

    print(f"Deine kalkulierte Busse beträgt CHF {calculatedFine:.2f}.")

def findLegalArticles():
    print("\nGeseztesartikel suchen")
    print("===============================")
    keyword = input("Schreibe ein Keyword für die Suche eines Gesetzesartikels: ").strip()
    pattern = re.compile(rf"\b{keyword}\b", re.IGNORECASE)
    
    matches = []
    for article, text in legalArticles.items():
        if pattern.search(text):
            matches.append((article, text))
    
    if matches:
        print("\nFolgende Artikel wurden gefunden:")
        for article, text in matches:
            print(f"{article}: {text}")
    else:
        print("Keine Gesetzesartikel gefunden.")

def main():
    while True:
        print("\nSchweizer Lärmbelästigungsgeld Rechner")
        print("=========")
        print("1. Lärmbelästigungsgeld berechnen")
        print("2. Gesetzesartikel suchen")
        print("3. Beenden")
        
        choice = input("Wähle deine Auswahl (1/2/3): ").strip()
        
        if choice == "1":
            calculateFine()
        elif choice == "2":
            findLegalArticles()
        elif choice == "3":
            print("Beenden des Programms, uf widerluege!")
            break
        else:
            print("Unbekannte Angabe. Bitte 1, 2, oder 3 eingeben.")

if __name__ == "__main__":
    main()
