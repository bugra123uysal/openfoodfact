import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


exc=pd.read_excel("C:\\Users\\buğra\\Desktop\\openfoodfacts\\food.xlsx")
print(exc.columns)
print(exc.isnull().sum())

say=exc["Besin-puanı"].value_counts().reset_index().head(10)
say.columns=["adet" ,"Besin-puanı"]
sns.barplot(y="Besin-puanı", x="adet" ,data=say)
plt.title("Besin puanı")
plt.show()