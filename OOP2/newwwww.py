class Muellimler():
    def calismaq(self):
        print('butun muellimler ders calisir')
        return self

    def iclas(self):
        print('butun muellimler iclasda istirak edir')
        return self

    def imtahan(self):
        print('Muellimler imtahan zamani qaydalara riayyet edir')
        return self





class tarixm(Muellimler):
    def enter(self):
        print('tarix muellimi sinife daxil olur olur')
        return self

    def login(self):
        print('tarix muellimi elektron jurnali acir')
        return self

    def active(self):
        print('tarix muellimi Osmanli tarixine aid  imtahan tertib edir')
        return self





class riyazm(Muellimler):
    def lab(self):
        print('Kimya muellimesi lab dersi kecir')
        return self

    def lab1(self):
        print('Muellime labda reaksiyalar haqqinda melumat verir')
        return self

    def lab2(self):
        print('Kimya muellimesi labin istifade qaydalarini basa salir')

        return self
    def both(self):
        print('Riyaziyyat ve Ingilis dili muellimleri iclasda istirak etdiler')
        return self


class ingilism(riyazm):
    def teach(self):
        print('Ingilis dili  muellimi ders kecir')
    


tm1=tarixm()
rm1=riyazm()
ingm=ingilism()

tm1.enter()\
    .login()\
    .active()\
    .calismaq()\
    .iclas()\
    .imtahan()

rm1.lab().lab1().lab2()

ingm.iclas()



# # # -----------------------


class mebel():
    material='taxta'

    def __init__(self,dest_novu,olcu,reng):
        self.dest=dest_novu
        self.olcu=olcu
        self.reng=reng

    def istehsal(self):
        print(f'{self.dest} {self.material}dan hazirlanir')

    def nov(self):
        print(f'{self.dest}nin rengi {self.reng}dir')

    def cm(self):
        print(f'{self.dest}nin olcusu {self.olcu}dur')


yataqdesti=mebel('yataqdesti','120x90','qehveyi')
yataqdesti2=mebel('metbexdesti','90x190','ag')

# change just one
yataqdesti.material='Polad'
yataqdesti.istehsal()

# change all
mebel.material='Palid'