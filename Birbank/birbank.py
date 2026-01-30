
try:
    print('tetbiq acilir sebrli olun zehmet olmasa')

    import time
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)
        
    print('salam eziz istifadeci xos gelmisiz')



    logininfolar=['l1','l2','l3']
    print()
    while True:
        logininfolar[0]=input('Zehmet olmasa kodunuzu yazin:')
        if logininfolar[0]!="":
            break
        print()
        print('Hal hazirda hansi emeliyyati isteyirsiz')
        
        print('Zehmet olmasa reqemle yazarsiz')
        
        print()

    secim=dict(
     e1= '1 = Kartdan karta pul atmaq',
     e2= '2 = Balansin artirilmasi',
     e3= '3 =  Kommunallar',
    e4= '4 =  Kredit ',
    e5= '5 = telefon balans artimi'
      )
    
    while True:
        for i in secim.values():
            print(i)
        

        s2=input('Zehmet olmasa daxil edin:').strip()
        if s2=='1':
            print('kartdan karta atmaq ekrani acilir zehmet olmasa gozleyin')
            import time
            for i in range(5,0,-1):
                print(i)
                time.sleep(1)
            
            print('Gozlediyiniz ucun tesekkur edirik')
        
            print()
            print('Medaxil daxil etmek')
            while True:
                k1=input('Kart nomresi daxil edin:')
                if k1 !="":
                    break
            
            while True:
                k2=input('kocurmek istediyiniz mebleg:')
                if k2!="":
                    break
        
            while True:
                k3=input('Emeliiyati tesdiq edirsizmi? Edirsizde Y Etmirsizse N yazin:')
                if k3=="Y":
                    break
                elif k3=='N':
                    break
                else:
                    print('ikisinden birini daxil edin')

            if k3=='Y':
                print('Emeliyyat ugurla heyata kecirildi')
                continue
            elif k3=='N':
                print('Emeliyyat legv edildi bizi secdiyiniz ucun tesekkurler')
                continue
            else: 
                print('Birbank size daha yaxin')


        elif s2=="2":
            print('Zehmet olmasa gozleyin')
            print()
            import time
            for i in range(5,0,-1):
                print(i)
                time.sleep(1)
            print('Balansin artirilmasi ekranina xos geldiz')
           
            operatorlar=dict(
            o1=' 1  = Bakcell ',
            o2=' 2  = Azercell',
            o3=' 3  = Nar'
            )
            for i in operatorlar.values():
                print(i)
        


            while True:
                n1=input('Zehmet olmasa operator secin:')
                if n1=="1":
                    break
                elif n1 =='2':
                    break
                elif n1=='3':
                    break
                else:
                    print('sehv operator secdiz')
                    
            if n1=="1":
                import time
                for i in range(5,0,-1):
                    print(i)
                    time.sleep(1)

                print('gozlediyiniz ucun tesekkur edirik')
                
                while True:
                    u1=input('zehmet olmasa nomreni daxil edin (+944/55/99)')
                    if u1!="":
                        break
                print(u1)

                while True:
                    y1=input('Odenisi tesdiqleyirsizmi? zehmet olmasa Y/N secin')
                    if y1=='Y':
                        break
                    elif y1=='N':
                        break
                    else:
                        print('Bele bir secim yoxdur')

                print()
                if y1=='Y':
                    print('Odenis ugurla tamamlandi')
                    continue
                
                elif y1=='N':
                    print('Odenis bas vermedi Bizi secdiyiniz ucun tesekkurler')
                    continue
                    
                else:
                    print('tesekkurler')


            elif n1=="2":
                print('zehmet olmasa gozleyin')
                import time
                for i in range(5,0,-1):
                    print(i)
                    time.sleep(1)

                print('gozlediyiniz ucun tesekkur edirik')
                while True:
                    u2=input('zehmet olmasa nomreni daxil edin (+944/51/50)')
                    if u2!="":
                        break
                    
                print(u2)

                while True:
                    i2=input('Odenisi tesdiqleyirsizmi  zehmet olmasa daxil edin Y/N')
                    if i2=="Y":
                        break
                    
                    elif i2=="N":
                        break
                    else:
                        print('bele bir secim yoxdur')
                        
                if i2=='Y':
                    print('Odenis ugurla gerceklesdi')
                    continue
                    
                elif i2=="N":  
                    print('Odenis tamamlanmadi')
                    continue
                   
                else:
                    print('birbank size daha yaxin')

            elif n1=="3":
                print('zehmet olmasa gozleyin')
                import time
                for i in range(5,0.-1):
                    print(i)
                    time.sleep(1)

                print('gozledyiniz ucun tesekkur edirik')

                while True:
                    u3=input('Zehmet olmasa nomrenizi daxil edin Y/N')
                    if u3=="Y" or u3=='N':
                        break
                    else:
                        print('bele bir secim yoxdur')

                if u3=='Y':
                    print('Odenis ugurla tamamlandi')
                    continue
                elif u3=='N':
                    print('Odenis heyeta kecirilmedi')
                    continue
                else:
                    print('Birbank heryerde')







































except Exception:
    print('xeta var')
finally:
    print('bizi secdiyiniz ucun tesekkurler')        




