import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

exc=pd.read_excel(r"C:\Users\buğra\Desktop\openfoodfacts\food.xlsx")
print(exc["katagori"].unique()[:20])
print(exc["katagori"].isnull().sum())
print(exc.columns)
print(exc[['Miktar_temiz', 'Miktar']].head(20))
#filtreleme
marka=exc[exc['Marka']== 'Coca-Cola' ].head(10)
ger=exc[exc['ülke']=='Germany'][['Ürün', 'Miktar', 'ülke']].head(10)

ktgr=exc['first_katagori'].value_counts().head(10)


mık=exc[exc['Marka']== 'Danone'].head(10)
mra=exc['Marka'].value_counts().head(10) 
arm=exc['Marka'].value_counts().tail(10)
cuty=exc['ilk_ülke'].value_counts().head(10)
cou=exc['ülke'].value_counts().tail(10)

for kat in ['Dairies','Snacks','Seafood']:
    k=exc[exc['first_katagori']==kat].value_counts('Marka').head(10)
    kk=exc[exc['first_katagori']==kat].value_counts('Marka').tail(10)

for puan in ['a', 'b', 'c', 'd', 'e']:
   #miktar
   haa=exc[exc['Besin-puanı']==puan].value_counts('Miktar_temiz').head(10)
   taa=exc[exc['Besin-puanı']==puan].value_counts('Miktar_temiz').tail(10)
  
   ha=exc[exc['Besin-puanı']==puan][['Ürün','Marka','Besin-puanı']].head(10)
   ta=exc[exc['Besin-puanı']==puan][['Ürün','Marka','Besin-puanı']].tail(10)

   #marka
   hallmark=exc[exc['Besin-puanı']==puan].value_counts('Marka').head(10)
   tallmark=exc[exc['Besin-puanı']==puan].value_counts('Marka').tail(10)

   #kategori
   hkb=exc[exc['Besin-puanı']== puan].value_counts('first_katagori').head(10)
   tkb=exc[exc['Besin-puanı']== puan].value_counts('first_katagori').head(10)


"""
exc['Marka'].value_counts().head(10).plot(kind='pie',autopct='%1.1f%%')
plt.title("marka dağılımı")
plt.show()

exc['first_katagori'].value_counts().head(10).plot(kind='pie', autopct='%.1f%%')
plt.title("kategoriler")
plt.show()

exc['ülke'].value_counts().head(10).plot(kind='pie', autopct='%.1f%%')
plt.title('Ülkeler')
plt.show()


plt.hist(exc["Miktar_temiz"].dropna(), bins=50)
plt.grid(True)
plt.title("miktar dağılımı (gram)")
plt.show()


plt.hist(exc['Besin-puanı'].dropna(), bins=50)
plt.title("besin puanı dağılımı")
plt.grid(True)
plt.show()




plt.hist(exc['ilk_ülke'].dropna().head(10), bins=50)
plt.title("ülke dağılımı")
plt.grid(True)
plt.show()


sns.boxplot(exc['Miktar_temiz'])
plt.show()


bes=exc["Besin-puanı"].value_counts().reset_index().head(50)
bes.columns=["adet" ,"Besin-puanı"]
sns.barplot(y="Besin-puanı", x="adet" ,data=bes)
plt.title("Besin puanı adetleri")
plt.grid(True)
plt.show()


ülk=exc['ülke'].value_counts().reset_index().head(50)
ülk.columns=["ülke", "adet"]
sns.barplot( x="ülke",y="adet" , data=ülk)
plt.title("ülke sayıları ")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

kat=exc['katagori'].value_counts().reset_index().head(10)
kat.columns=["katagori", "adet"]
sns.barplot(x="katagori", y="adet" , data=kat)
plt.title("kategori adeti")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()


mar=exc['Marka'].value_counts().reset_index().head(50)
mar.columns=["marka", "adet"]
sns.barplot(x="marka", y="adet", data=mar)
plt.title("marka adeti")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()



sır=exc.sort_values(by='Miktar_temiz', ascending=False).head(50)
sns.barplot(x="Miktar_temiz", y="Ad"  , data=sır)
plt.title("miktar küçükden büyüğe")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()
 """  