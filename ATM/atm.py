secim=('Atm proqramina xos geldiz\n'
      '**********Etmek istediyiniz emeliyyati secin**********\n'
      '***** Balans ucun  1 reqemine basin *****\n'
      '***** Pul yatirmaq ucun 2 reqemine basin *****\n'
      '***** Pul cekmek ucun 3 reqemine basin *****\n' \
      '***** Cixmaq ucun Q duymesine basin *****'

      
      
      
      
      )


balans=2000

while True:
    print(secim)
    musteri=input('Istediyiniz emeliiyati qeyd edin: ')
    if musteri =='q':
        print('Cixis etdiz.....')
        break

    elif musteri =='1':
        print('Movcud balans',balans)
    
    elif musteri =='2':
        yatirmaq=int(input('Yatiralacaq meblegi daxil edin : '))
        print('Umimi balans',balans+yatirmaq)

    elif musteri=='3':
        cixarma=int(input('cixarmaq istediyiniz meblegi daxil edin: '))
        print('Halhazirda balans',balans-cixarma)
        if cixarma > balans:
            print('Balans kifayet deyil')


    else :
        print('Duzgun melumat daxil edin')
        
        
