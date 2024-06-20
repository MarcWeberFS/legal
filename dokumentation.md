# Dokumentation

## 1. Was macht das Programm?
Das Programm ist ein einfacher Lärmbelästigungsgeldrechner, der es dem Benutzer ermöglicht, eine Geldstrafe für eine Lärmbelästigung in der Stadt Zürich zu berechnen. Der Benutzer kann auch nach bestimmten Gesetzesartikeln suchen, die sich auf Lärmbelästigung beziehen. Das Programm ist dabei eine Commandline basierende Applikation.

## 2. Wie wird das Programm bedient?

![picture of the menu](/img/menu.png)

Das Programm bietet dem Benutzer ein einfaches Menü mit vier Optionen:
1. **Lärmbelästigungsgeld berechnen**: 
![picture of the noise complaint calculator](/img/calculator.png)
Der Benutzer wird aufgefordert, den Lärmpegel in Dezibel, die Dauer der Lärmbelästigung in Stunden, die Tageszeit (Tag oder Nacht) und die Anzahl der vorherigen Verstösse gegen die Lärmbelästigungsgesetze einzugeben. Das Programm berechnet dann die Geldstrafe basierend auf diesen Eingaben und zeigt das Ergebnis an. Die Geldstrafe bezieht sich auf die Stadt Zürich und wird anhand von festgelegten Regeln und approximativen Werten berechnet. Die Strafe kann nicht über 500 CHF betragen in Zürich. Dementsprechend kann es zu Fehlern in der Berechnung kommen, da das Gesetz nicht genau die Bussen festlegt, nur einen Rahmen in dem das Programm sich aufenthält.
2. **Gesetzesartikel suchen**: 
![picture of the article search](/img/search.png)
Der Benutzer kann ein Schlüsselwort eingeben, nach dem im Text der Gesetzesartikel gesucht werden soll. Das Programm zeigt dann alle Gesetzesartikel an, die das Schlüsselwort enthalten. Das Schlüsselwort wird mittels einer Regex Suche durchgeführt, um auch nach Teilwörtern zu suchen. Dabei werden alle Artikel, die für das Schlüsselwort relevant sind und über Lärmberechtigungen informieren, angezeigt.
3. **Beenden**: 
![picture of closing the programm](/img/end.png)
Beendet das Programm.

## 3. Python
Das Programm ist in Python geschrieben und verwendet einfache Konzepte wie Schleifen, Bedingungen, Benutzereingaben, Funktionen, Dictionaries und reguläre Ausdrücke. Es zeigt auch die Verwendung von Funktionen und Dictionaries in Python. Das Programm ist in verschiedene Funktionen aufgeteilt, um die Lesbarkeit und Wartbarkeit zu verbessern. Die Funktionen sind:

- **`calculateFine()`**: 
![picture of the method calculateFine()](/img/calculateFine.png)
Diese Funktion berechnet die Geldstrafe für eine Lärmbelästigung basierend auf den Benutzereingaben. Sie berücksichtigt den Lärmpegel, die Dauer der Lärmbelästigung, die Tageszeit (Tag oder Nacht) und die Anzahl der vorherigen Verstösse.
- **`findLegalArticles()`**: 
![picture of the method findLegalArticles()](/img/findLegalArticles.png)
Diese Funktion sucht nach Gesetzesartikeln, die ein bestimmtes Schlüsselwort enthalten. Sie verwendet reguläre Ausdrücke, um nach Teilwörtern zu suchen und relevante Gesetzesartikel zu finden.

Das Programm verwendet auch ein Dictionary, um die Gesetzesartikel und ihre Definitionen zu speichern. Die Verwendung von regulären Ausdrücken ermöglicht es dem Benutzer, nach Teilwörtern zu suchen, um relevante Gesetzesartikel zu finden.

## 4. Verbesserungsvorschläge
- Das Programm könnte um weitere Funktionen erweitert werden, z.B. um die Anzeige aller verfügbaren Gesetzesartikel oder um die Anzeige von Informationen zu den verschiedenen Arten von Lärm.
- Die Berechnung der Geldstrafe könnte genauer gemacht werden, indem vorherige Fälle analysiert und in die Berechnung implementiert werden.
- Die Benutzeroberfläche könnte verbessert werden, sodass das Programm nicht über eine Commandline bedient wird, sondern über eine Webseite.

## 5. Fazit
Das Programm ist ein einfacher Lärmbelästigungsgeldrechner, der es dem Benutzer ermöglicht, eine Geldstrafe für eine Lärmbelästigung in der Stadt Zürich zu berechnen. Es zeigt die Verwendung von Funktionen, Dictionaries und regulären Ausdrücken in Python. Das Programm könnte weiter aufgebaut werden in eine richtige Webapp, ähnlich wie zuschnell.ch und auch monetarisiert werden. Das Programm erfüllt die Beurteilungskriterien.

## 6. Beurteilungskriterien und dessen Erfüllungsgrad
![picture of the programcriteria](/img/bewertungskriterien.png)
- **Das Programm verweist auf die Rechtsgrundlagen in einer Art und Weise, wie es von Studierenden der Rechtswissenschaft zu erwarten wäre**: Das Programm verweist auf die Rechtsgrundlagen, indem es die relevanten Gesetzesartikel für Lärmbelästigung in der Stadt Zürich auflistet und es dem Benutzer ermöglicht, nach Gesetzesartikeln zu suchen, die ein bestimmtes Schlüsselwort enthalten.
- **Das Programm nimmt die Komplexitäten des Rechts gebührend in Betracht**: Das Programm berücksichtigt die Komplexität des Rechts, indem es die Geldstrafe für Lärmbelästigung basierend auf verschiedenen Faktoren berechnet, wie z.B. den Lärmpegel, die Dauer der Lärmbelästigung, die Tageszeit und die Anzahl der vorherigen Verstösse. Es ermöglicht auch die Suche nach Gesetzesartikeln, die sich auf Lärmbelästigung beziehen.
- **Das Programm funktioniert ohne Fehlermeldungen**: Das Programm ist kompilierbar und keine der Funktionen weisen Fehler auf.
- **Die schriftliche Dokumentation ist nachvollziehbar und setzt sich kritisch mit dem Gelernten auseinander**: Eine Regex-Expression ist vorhanden und das Programm basiert auf Python, welches wir während des Unterrichts angeschaut und einen Crashkurs dazu gehabt haben. Das Programm bezieht sich auf den LegalTech Kontext, indem es ein Programm ist, welches sich mit rechtlichen Grundlagen im Lärmbelästigungssegment auseinandersetzt und diese in einem Programm umsetzt. Die Dokumentation ist in einem Markdown Format geschrieben und zeigt diverse Bilder vom Programm.
