import requests
import pandas as pd

urun=["coke","milk","bread","water","meat","chocolate","hazelnut","pasta","almond"] 
bos=[]
for allurun in urun:

   url=f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={allurun}&json=1"
   respon=requests.get(url)
   bb=respon.json()
   
   for uru in bb.get("products", [])[:10]:
       name=uru.get("product_name", "bilinmiyor")
       brand=uru.get("brands", "bilinmiyor")
       country=uru.get("countries", "bilinmiyor")  
       categories=uru.get("categories","bilinmiyor")
       quantity=uru.get("quantity", "bilinmiyor")
       nutriscore=uru.get("nutriscore_grade","bilinmiyor")
       """ 
       print(f"{name} - {brand}")
        """
       bos.append({"Ürün": allurun,"Marka": brand , "Ad": name  ,"katagori": categories,"Miktar":quantity,"ülke":country , "Besin-puanı": nutriscore})

exc=pd.DataFrame(bos)
exc.to_excel("C:\\Users\\buğra\\Desktop\\openfoodfacts\\food.xlsx", index=True)
print(exc.columns)
print(exc.isnull().sum())
