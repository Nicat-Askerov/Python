class olkeler:
    def __init__(self,ad,paytaxt,Ehali,miliyyet):
        self.ad1=ad
        self.paytaxt=paytaxt
        self.ehali=Ehali
        self.miliyyet=miliyyet

    def mekan(self):
        print(f'{self.ad1} paytaxti {self.paytaxt}')

    def population(self):
        print(f'{self.ehali} sayi bu qederdir')


    def nationality(self):
        print(f'olkenin miliyyeti {self.miliyyet}dur')        



class Azerb(olkeler):
    def __init__(self, ad, paytaxt, Ehali, miliyyet,cografiya):
        super().__init__(ad, paytaxt, Ehali, miliyyet,)

        self.cog=cografiya

    def mix(self):
        return self.cog,self.ad1


class Georgia(olkeler):
    def __init__(self, ad, paytaxt, Ehali, miliyyet,yemek):
        super().__init__(ad, paytaxt, Ehali, miliyyet)

        self.yemek=yemek

    def meals(self):
        print(f'{self.ad}in en mehsur yemeyi {self.yemek}dir')







    
Azerbaycan=Azerb('AZ','Baku','10 million','turk','qafqaz')
Gurcustan=Georgia('Gurcustan','Tflis','3 milyon','gurcu','xacapuri')

print(Azerbaycan.mix())

Gurcustan.mekan()

#  ------------------------
from abc import ABC,abstractmethod




class elektronika(ABC):
     def __init__(self,nov,marka,yadddas):
          self.nov=nov
          self.marka=marka
    
          self.yaddas=yadddas
     @abstractmethod
     def info1(self):
         print(f'elektronikanin novu {self.nov}dur')

    
    



class phone(elektronika):
    def __init__(self, nov, marka, yadddas):
        super().__init__(nov, marka, yadddas)
 

    def myinfo(self):
        pass
    def info1(self):
         print(f'elektronikanin novu {self.nov}dur')

    def phone1(self):
        print(f'{self.nov}nun markasi {self.marka}dir')

    def phone2(self):
        print(f'Cihazin rami {self.yaddas}dir')





class tablet(phone):
    def __init__(self, nov, marka, yadddas):
        super().__init__(nov, marka, yadddas)

   



telefon=phone('telefon','samsung','128')
planset=tablet('tablet','iphone','256')


telefon.info1()

planset.info1(
)




----------


class fennler():

    ad=None


def example(fenn,deyer):
    fenn.ad=deyer
    





azdili=fennler()

example(azdili,'azerbaycandili')


print(azdili.ad)




# ------------

class heyvanlar:
    def all(self):
        pass


class dog:
    def qacmaq(self):
        print('It qacir')

    def oynamaq(self):
        print('it oyanyir')


class cat:
    def yatmaq(self):
        print('Pisik yatir')
        

    def yemek(self,info):
        print('Pisik oyanyir')
        info.qacmaq()
        


it=dog()
pisik=cat()

pisik.yemek(it)


--------------------



