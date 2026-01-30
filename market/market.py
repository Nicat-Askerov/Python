# bir market tesevvur edek

print("Nicat markete xos geldiz")
  
# Ana menyu
print('hal hazirda bu secimler movcuddur')

print(
"1 = Ət mehsullari\n"
"2=Meyvə tərəvəz bitkilər\n"
"3=Spirtli içkilər\n"
"4=spirtsiz ickiler\n"
 )
  

secimetvetendas =int(input("zehmet olmasa birini secin"))

if secimetvetendas==1:
   print('et mehsullari asagidaki kateqoriyalara bolunur')
   print(
     '11 =Qırmızı ətlər'
     '12 = Dana eti'
     '13= Quzu eti'
    )
          
   meatsecim=int(input('Hansini isteyirsiniz secin zehmet olmasa'))
   if meatsecim==11:
     print('Qirmizi etlerin qiymeti bunlardir')
     print(
      "TAC MAL FARŞI DONMUŞ KQ-14 azn\n"
      "Dana Əti Sümüksüz 1 kq-16 azn\n"
      "Ət Dana Sümüksüz 1 kg-21 azn\n"

     )
   elif meatsecim==12:
     print('Dana əti 9 məhsul')
     print(
    "Dana Əti Sümüksüz 1 kq-25 azn\n"
    "Ət Dana Antrikot 1 kq-18 azn\n"
    "Ət Dana Sümüksüz 1 kq-21 azn\n"
     )
   elif meatsecim==13:
     print('Quzu əti 2 məhsul')
     print(
    "Quzu quyruqu-21azn\n"
    "Ət Quzu Komplekt-14azn\n"
    
     )
   else:
     print('bu secim movcud deyil')

elif secimetvetendas==2:
  print('Meyvə tərəvəz bitkilər asagidaki kateqoriyalara bolunur')
  print(
    "21 = Tərəvəz"
    "22 = Meyvə"
    '23 = Meyvəli tərəvəz'
  )
  meyvesecim=int(input('bunlardan birini secin'))
  if meyvesecim==21:
    print(
      "sogan setka 1 kg 0.79 azn\n"
      "Bibər Şirin 1kq 4.50 azn\n"
      "Kartof Kababliq 1.5kq\n"
      "Pomidor Muço 1kq 3.19\n"
    )
  elif meyvesecim==22:
    print(
      "Fındıq 1kq-11.09 azn\n"
      "Qoz 1 kg 8 azn\n"
      "Alma Qala Super kq 1.59 azn\n"
      "Banan kq 3.19 azn\n"
      "Qarpız kq 0.35 azn\n"
      "Yemiş 1 kq 5.49 azn\n"
      " Kivi 1 kq 4 azn\n"
      "Alma Fuji Super 1 kq 2.69 azn\n"
      "Armud Konfrans 1 kq 3.99 azn\n"

    )
  elif meyvesecim==23:
    print(
      "Lobya Yerli kq\n"
      "Balqabaq kq\n"
      "Pomidor Zirə Ekonom kq\n"
      "Bibər Dolmalıq 1 kq\n"
      "Xiyar Melit 1kq\n"
    )
  else:
    print('Teesufki bu secim yoxdur')




        
    
















