# Hayvan sınıfı, temel hayvan özelliklerini ve davranışlarını tanımlar.
class Hayvan:
    def __init__(self, sesi, yemegi, yeri):
        # Hayvanın adını tanımlamak için bir özellik (değişken) adı atanmamıştır.
        # Bunun yerine alt sınıflar bu özelliği kendileri tanımlayacak.
        self.ad = None
        self.yemegi = yemegi
        self.sesi = sesi 
        self.yeri = yeri 

    def NeDer(self):
        return self.sesi

    def NeredeYaşayan(self):
        return self.yeri

    def NeYer(self):
        return self.yemegi

# Kedi sınıfı, Hayvan sınıfından türetilmiştir.
class kedi(Hayvan):
    def __init__(self, sesi, yemegi, yeri):
        # Kedinin adı kedi olarak atanmıştır.
        self.ad = "kedi"
        self.yemegi = yemegi
        self.sesi = sesi 
        self.yeri = yeri 

# Köpek sınıfı, Hayvan sınıfından türetilmiştir.
class köpek(Hayvan):
    def __init__(self, sesi, yemegi, yeri):
        # Köpeğin adı köpek olarak atanmıştır.
        self.ad = "köpek"
        self.yemegi = yemegi
        self.sesi = sesi 
        self.yeri = yeri 

# Kuş sınıfı, Hayvan sınıfından türetilmiştir.
class kuş(Hayvan):
    def __init__(self, sesi, yemegi, yeri):
        # Kuşun adı kuş olarak atanmıştır.
        self.ad  = "kuş"
        self.yemegi = yemegi
        self.sesi = sesi 
        self.yeri = yeri

# İnek sınıfı, Hayvan sınıfından türetilmiştir.
class inek(Hayvan):
    def __init__(self, sesi, yemegi, yeri):
        # İneğin adı inek olarak atanmıştır.
        self.ad = "inek"
        self.yemegi = yemegi
        self.sesi = sesi 
        self.yeri = yeri 

# anlat fonksiyonu, bir Hayvan örneğini parametre olarak alır ve özelliklerini ekrana yazdırır.
def anlat(h):
    print(h.ad,"= ", h.NeDer()," diyen", h.NeYer(),"yiyen  ",h.NeredeYaşayan() ,"yaşayan hayvanım var")

# Hayvan alt sınıflarından örnekler oluşturulur.
kedi = Hayvan("miyav","mama","evde")
köpek = Hayvan("hav","kemik","kulübede")
kuş = Hayvan("cik","yem","ağaç")
inek = Hayvan("mö","saman","ahır")

# Oluşturulan örnekler anlat fonksiyonuna gönderilir ve bilgiler ekrana yazdırılır.
anlat(kedi)
anlat(köpek)
anlat(kuş)
anlat(inek)