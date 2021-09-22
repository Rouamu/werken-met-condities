dierendressuur = int(input("Hoeveel jaar ervaring heeft u met dieren-dressuur?"))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren?"))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?"))
school =input("heeft u school afgrond?")
diploma = (input("heeft u mbo 4 Diploma?"))
rijbewijs= input("bent u bezit van rijbewijs c(vrachtwagen)?") 
geslacht= input("bent u een vrouw of een man?")
hoed= input("heeft u een hoge hoed?")
lengte= 150
gewicht= 90
snor2 = 0
snor ='ja'
roodhaar = "ja"

if geslacht=="man":
    lengte =int(input("hoe lang bent u?"))
    if lengte >=150:
        snor= input("heeft u een snor?")
    if snor =="ja":
        snor2 =int(input("hoe breed is uw snor?"))
    else:
        snor2 = 0

if geslacht=="vrouw":
    lengte = int(input("hoe lang bent u?"))
    if lengte>=150:
        roodhaar = input('heeft u roodkrullig har?')
    if roodhaar =='ja':
        haarlengte =int(input('hoelang is uw haar? '))
else:
    haarlengte = 0



if (dierendressuur >= 4 or jongleren >= 5 or acrobatiek >= 3) and (diploma =="ja" and rijbewijs =="ja" and hoed =="ja" and lengte >= 150 and gewicht >= 90 and (geslacht=="man" and snor and snor2 >=10)or (geslacht== "vrouw" and haarlengte>=20)):
    print("je bent aangenomen")

else:
    print("helaas, u voldoet niet aan de eisen")


        







