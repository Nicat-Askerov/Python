def xos():
    print('Deyerli istifadeci xos geldiz')

xos()

def toplama():
    print('Netice',a+b)

def cixma():
    print('Netice',a-b)

def vurma():
    print('Netice',a*b)


def bolme():
    print('Netice',a/b)






try:
    while True:
        a=int(input('zehmet olmasa reqem daxil edin:'))
        b=int(input('zehmet olmasa reqem daxil edin:'))
        c=input('zehmet olmasa isaret secin (+ - / *  , cixis ucun -1 q):')
        if c =="+":
            toplama()
            input(' Qayitmaq ucun Enter basin')
        elif c =="-":
            cixma()
            input(' Qayitmaq ucun Enter basin')
        elif c=="*":
            vurma()
            input(' Qayitmaq ucun Enter basin')

        elif c=='/':
            bolme()
            input(' Qayitmaq ucun Enter basin')

        elif c=="q":
            print('Cixis edildi')
            break

        else :
            print('Bele bir secim yoxdur')


except Exception as e:
    print('xeta var' , e)

finally:
    print('Bizi secdiyiniz ucun tesekkur edirik')
