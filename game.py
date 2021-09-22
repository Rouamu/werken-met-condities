Dribbel = input("Welkom je gaat nu beginnen met het spel, je staat in het midden van de veld. Dribbel je de bal of pass je de bal? (dribbel/pass) ")


if Dribbel == "dribbel":
    zelf = input("je staat voor de basket, wil je zelf proberen om te schieten of te passen? (schiet/pass) ")
    if zelf == "schiet":
        print('Je hebt gescoord, gefeliciteerd je hebt de game gewonnen.')
    else:
        print('De bal werdt verdedigd en de tijd is om! Helaas je hebt de game verloren.')
else:
    jezelf = input('je hebt de bal aan je teamgenoot gepasst, wil je de teamgenoot zijn of jezelf zijn? (jezelf/teamgenoot) ')
    if jezelf == "jezelf":
        verdedigen = input("wil je je teamgenoot verdedigen of je blijft staan? (verdedigen/staan) ")
        if verdedigen =="verdedigen":
            print("je teamgenoot heeft gescoord, gefeliciteerd je hebt de game gewonnen")
        else:
            print("omdat je bleef staan is de bal afgepakt, helaas je hebt verloren.")
    else:
        teamgenoot = input('Je bent nu de teamgenoot, pass je de bal of schiet je? (pass/schiet) ')
        if teamgenoot == "schiet":
            print('je hebt gescoord, gefeliciteerd je hebt de game gewonnen.')
        else:
            print('de bal werdt verdedigd, helaas je hebt de game verloren.')
