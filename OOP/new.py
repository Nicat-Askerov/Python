class kitabxana:
    def __init__(self,ad,nov,dil,sehife):
        self.ad=ad
        self.nov=nov
        self.dil=dil
        self.sehife=sehife

    def nameofbook(self):
         print(f'Kitabin adi{self.ad}dir ve novu {self.nov}')
     

    def dil2(self):
        print(f'{self.ad}in dili {self.dil}dir')

    def sehife2(self):
          print(f'{self.ad} {self.sehife} sehifedir ')
    

book1=kitabxana('Koroglu','Xalq dastani','Turkce','400')

book1.nameofbook()
book1.sehife2()
book1.dil2()

# --------------

class mekteb:
     def __init__(self,ad,nomre,seher,abituriyent_sayi):
          
          self.ad=ad
          self.nomre=nomre
          self.seher=seher
          self.abi=abituriyent_sayi
    
     def study(self):
          print(f'Abituriyentimizin adi {self.ad}dir ')

     def infostudy(self):
          print(f'{self.ad} hal hazirda {self.nomre}-li tam orda mektebde tehsil alir')
     def infostudy1(self):
          print(f'{self.nomre}-li mekteb {self.seher}de yerlesir')

     def infoscholl1(self):
          print(f'{self.nomre}-li mektebde hal hazirda {self.abi} nefer tehsil alir')


sagird1=mekteb('Malik','35','Baki','421'
    )


sagird1.study()
sagird1.infostudy()
sagird1.infostudy1()
sagird1.infoscholl1()

# ---------------

class ofis:
     def __init__(self,ad,soyad,comapny,sobe,maas):
          self.ad=ad
          self.soyad=soyad
          self.company=comapny
          self.sobe=sobe
          self.maas=maas

     def isci(self):
          print(f'{self.ad} {self.soyad} hal hazirda {self.company}-da calisir')

     def info0(self):
          print(f'{self.ad} hal hazirda {self.sobe}de calisir')

     def info(self):
          print(f'{self.ad}in emek haqqisi {self.maas}azn dir')


worker1=ofis('Mehemmed','Esedov','AZERISIQ','IT','750')
worker2=ofis('Qenber','Memmedov','Caspian telecom','HR','980')


# -----------



class laptoplar:
    def __init__(self,markasi,cpu,gpu,ram,ssd):
        self.markasi=markasi
        self.cpu=cpu
        self.gpu=gpu
        self.ram=ram
        self.ssd=ssd

    def info1(self):
        print(f'Komputerin markasi {self.markasi}')

    def info2(self):
        print(f'Komputerin Prosessoru(CPU) {self.cpu}')

    def info3(self):
        print(f'Komputerin ekran karti(GPU) {self.gpu}')

    def info4(self):
        print(f'Komputeri Ram-i (random access memory ) {self.ram}')

    def info5(self):
        print(f'Komputerin SSD(Solid state drive) yaddasi {self.ssd}')
              



laptop1=laptoplar('HP','Intel i5-12th400H','Nvdia 1650','32gbram ddr5','M2 NVME SSD 1 TB'
                  )

laptop1.info1()
laptop1.info2()
laptop1.info3()
laptop1.info4()
laptop1.info5()

# --------




