import json
# def info():
#     with open('info.json','r',)as file:
#         a=json.load(file)
#         for i,y in a.items():
#             print(i ,'-', y)
        

# info()

# def login():
#     while True:
#         username=input('zehmet olmasa adinizi daxil edin:')
#         surname=input('zehmet olmasa soyadinizi daxil edin:')
#         password=int(input('Sifrenizi daxil edin:'))
#         if username =='Qafur'and surname=='Memmedov'and password==21:
#             print('sisteme ugurlu giris oldu')
#             break
#         else:
#             print('Yalnis melumat daxil etdiniz')


# login()


# def secim_1():
#     print('Balans artirilmasi ekranina xos geldiz zehmet olmasa biraz gozleyin')
#     import time 
#     for i in range(3,0,-1):
#         print(i)
#         time.sleep(1)

#     print('Gozlediyiniz ucun tesekkurler')
#     print()


#     while True:
#         k=input('Zehmet olmasa kart nomrenizi daxil edin:')
#         if k=="":
#             print('bos qoya bilmersiz')
#             continue
#         elif len(k) !=16:
#             print('kartin  nomresi 16 reqem olmalidi:')
#             continue
#         elif not k.isdigit():
#             print('reqem olmalidir')

#         elif len(k)==16:
#             print('kart ugurla daxil edildi:')
#             print()
#             print(k)
#             break


#     while True:
#         m=input('Zehmet olmasa mebleg daxil edin:')
#         if m =="":
#             print('Bos qoya bilmersiz')

#         elif not m.isdigit():
#             print('Yalniz reqem daxil edin')

#         elif m.isdigit():
#             print(m)
#             print('Odesiniz ugurla heyata kecirildi')
#             break
        
# ------------------

def secim_2():
    print("Paketler haqqinda ekranina xos geldiz zehmet olmasa gozleyin")
    import time 
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    print('Gozlediyiniz ucun tesekkur edirik' )
    print()
    print('Halhazirda bu secimler vardir')
    with open('paketler.json','r',encoding='utf-8')as dosya:
        txt=json.load(dosya)
        
       
    while True:
        for a,b in txt.items():
            print('\n'+a)
            for c,d  in b.items():
                print('', c ,"-",d)

        print()
    
      
        secim2=input('Zehmet olmasa secim edin\n0 - Esas menuya qayit\nSecim:').strip()
        if secim2 =="1":
            
            for ad,qiymet in txt['1- Limitsiz'].items():
                print(ad ,"-",qiymet)
            print()
            secim3=input('birini secin')------secim ekrani paketin
        
           

       
       
       
        elif secim2=="0":
            input('Enter basin')
            


secim_2()
    










    
# def secim_ekrani():
#     with open('secimifno.json','r',encoding='utf-8')as file:      
#         info=json.load(file)
        

#         while True:
#             for i,y in info.items():
#                 print(i,'-',y)

#             secim=input('zehmet olmasa reqemle seciminizi edin:')
#             if secim=='1':
#                 secim_1()

         
           



# secim_ekrani()



    



   