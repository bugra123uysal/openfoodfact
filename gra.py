import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt





exc=pd.read_excel(r"C:\Users\buğra\Desktop\openfoodfacts\food.xlsx")



"""  
exc['Ad']=exc['Ad'].fillna("bilinmiyor")
exc['Marka']=exc['Marka'].fillna("billinmiyor")
exc['katagori']=exc['katagori'].astype(str).str.strip()
exc['katagori']=exc['katagori'].replace(["","nan","None"], "bilinmiyor")
exc['katagori']=exc['katagori'].fillna("billinmiyor")
exc['Miktar']=exc['Miktar'].fillna(0)
print(exc['katagori'].unique()[:20])
print(exc['katagori'].isnull().sum())
print(exc.isnull().sum())
"""

print(exc.columns)

#filtreleme
marka=exc[exc['Marka']== 'Coca-Cola' ].head(10)
ger=exc[exc['ülke']=='Germany'][['Ürün', 'Miktar', 'ülke']].head(10)
a=exc[exc['Besin-puanı']=='a'][['Ürün','Marka','Besin-puanı']].head(10)
b=exc[exc['Besin-puanı']=='b'][['Ürün','Marka','Besin-puanı']].head(10)
c=exc[exc['Besin-puanı']=='c'][['Ürün','Marka','Besin-puanı']].head(10)
d=exc[exc['Besin-puanı']=='d'][['Ürün','Marka','Besin-puanı']].head(10)
e=exc[exc['Besin-puanı']=='e'][['Ürün','Marka','Besin-puanı']].head(10)
mık=exc[exc['Marka']== 'Danone'].head(10)

  
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

sıra=exc.sort_values(by='Miktar', ascending=True).head(50)
sns.barplot(y='Ad', x='Miktar' , data=sıra)
plt.xticks(rotation=90)
plt.grid(True)
plt.title("gram")
plt.show()

sır=exc.sort_values(by='Miktar', ascending=False).head(50)
sns.barplot(x="Miktar", y="Ad"  , data=sır)
plt.title("miktar küçükden büyüğe")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

