geelkaas = input("is de kaas geel?")

if geelkaas == 'ja':
    gaten = input('zitten er gaten in? ')
    if gaten == 'ja':
        duur = input('is de kaas belachelijk duur? ')
        if duur == 'ja':
            print('de kaas die jij wilt is Emmenthaller!!! ')
        else:
            print('de kaas die jij wilt is Leerdameer!!! ')
    else:
        hard = input('is de kaas hard als steen? ')
        if hard == 'ja':
            print('de kaas die jij wilt is Parmigiano Reggiano')
        else:
            print('de kaas die jij wilt is Goude kaas!!!')
else:
    schimmel = input('Heeft de kaas blauwe schimmels? ')
    if schimmel == 'ja':
        korst = input('heeft de kaas kortst? ')
        if korst == 'ja':
           print('de kaas die jij wilt is Blue De Rochbaron!!! ')
        else: 
            print('de kaas die jij wilt is Founme dambert!!')
    else: 
        korst2 = input('heeft de kaas korst??')
        if korst2 == 'ja':
            print('de kaas die jij wilt is Chamembert!!!!')
        else:
            print('de kaas die jij wilt is mozzarella!!!')



