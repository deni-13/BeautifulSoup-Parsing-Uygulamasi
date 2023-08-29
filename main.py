import requests

from bs4 import BeautifulSoup


for sayfa in range(1,25):
    url="https://www.kitapsec.com/Products/Kirtasiye/Boyalar-ve-Boya-kalemleri/"+str(sayfa)+"-6-0a0-0-0-0-0-0.xhtml"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"lxml")


    
    #urunsatir bir urun 
    #urunler !
    
    urunler=soup.find_all("div",attrs={"class":"Ks_UrunSatir"})
    #urunler icin text ler
    #print(urunler) #ilk syf40urun
    # for j in urunler:
    #     print(j.text)
    
    #ornek eleman
    #<a href="https://www.kitapsec.com/Products/Notyaz-Yapiskanli-Not-Kagidi-Seti-142149.html" class="text" title="Notyaz Yapışkanlı Not Kağıdı Seti" itemprop="url"> <span itemprop="name">Notyaz Yapışkanlı Not Kağıdı Seti</span></a>
    for urun in urunler:
        isim=urun.find("a",attrs={"class":"text"}).get("title") 
        #print(urun) a icindeki textleri aldik
        print(isim)
        #-----------------------------
        #fiyatlar
        fiyat=urun.find("span",attrs={"class":"fiyat"})
        #print(fiyat)    
        a_urun=urun.find("font",attrs={"class":"piyasa"}).text
        b_urun=urun.find("font",attrs={"class":"satis"}).text #indirimli
        # print(a_urun)
        # print(b_urun)
        
        if a_urun and b_urun:
            print("piyasa:",a_urun ,"satis:",b_urun)
        else:
            print("satis" ,  b_urun)
            
        adet=urun.find("div",attrs={"class":"adet"})
        #bazilarinda urun kalmiyor
        
        if adet:
            print("kalan adet",adet.text)
        else:
            print("adet bilgisi yok")
            
            
    
        
        