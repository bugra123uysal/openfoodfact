import requests
import pandas as pd


urun=[ # Dairy & Eggs
    "Milk", "Skim Milk", "Almond Milk", "Soy Milk", "Eggs", "Butter", "Cheese", "Cheddar Cheese", "Mozzarella",
    "Yogurt", 


    # Bread & Bakery
    "White Bread", "Whole Wheat Bread", "Multigrain Bread", "Bagels", "Croissants"

    # Meat & Poultry
    "Chicken Breast", "Chicken Wings", "Chicken Legs", "Ground Beef", "Beef Steak"

    # Seafood
    "Salmon", "Tuna", "Shrimp", "Crab", "Lobster"

    # Fruits
    "Apples", "Bananas", "Oranges", "Mandarins", "Grapes",

    # Vegetables
    "Potatoes", "Sweet Potatoes", "Onions", "Garlic", "Carrots", "Broccoli", 

    # Grains & Pasta
    "Rice", "Basmati Rice", "Brown Rice", "Quinoa", "Oats", 

    # Baking & Cooking
    "Flour", "Whole Wheat Flour", "Cornmeal", "Sugar", "Brown Sugar"

    # Oils & Condiments
    "Olive Oil", "Vegetable Oil", "Canola Oil", "Sunflower Oil", "Coconut Oil", "Vinegar",

    # Canned & Packaged Foods
    "Tomato Sauce", "Tomato Paste", "Canned Tomatoes", "Canned Beans", "Canned Tuna"
    # Frozen Foods
    "Frozen Vegetables", "Frozen Fruit", "Frozen Pizza", "Frozen Fries", "Frozen Chicken Nuggets", 
   
    # Beverages
    "Bottled Water", "Sparkling Water", "Mineral Water", "Soft Drinks", "Cola"

    # Breakfast & Snacks
    "Breakfast Cereal", "Cornflakes", "Granola", "Oatmeal", "Peanut Butter"

    # Household & Cleaning
    "Toilet Paper", "Paper Towels", "Napkins", "Facial Tissues", "Dish Soap"

    # Personal Care
    "Shampoo", "Conditioner", "Body Wash", "Bar Soap", "Toothpaste"

    # Baby & Kids
    "Baby Formula", "Baby Food", "Diapers", "Baby Wipes",

    # Pet Supplies
    "Dog Food", "Cat Food", "Pet Treats"   
   
      ]
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

       bos.append({"Ürün": allurun,"Marka": brand , "Ad": name ,"Miktar":quantity,"ülke":country, "katagori": categories , "Besin-puanı": nutriscore})

       """ 
       print(f"{name} - {brand}")
       """


      

exc=pd.DataFrame(bos)

exc["Ad"]=exc["Ad"].fillna("bilinmiyor")
exc["Marka"]=exc["Marka"].fillna("bilinmiyor")
exc["katagori"]=exc["katagori"].fillna("bilinmiyor")
exc["Miktar"]=exc["Miktar"].fillna(0)

exc['birim']=exc['Miktar'].astype(str).str.extract(r'([a-zA-Z]+)$')
exc['sayı']=exc['Miktar'].astype(str).str.extract(r'(\d+\.?\d*)')
exc=exc.drop_duplicates()  # tekrar eden ürünleri siler
print(len(exc))
print(exc['birim'].unique())
def mka(sayı , birim):
    if pd.isnull(sayı) or pd.isnull(birim):
        return None
    
    sayı=float(sayı)
    birim=birim.lower()

    if birim in ['g','gr','gram']:
        return sayı
    
    elif birim in ['kg']:
      return sayı * 1000 
    elif birim in ['ml']:
        return sayı
    elif birim in ['l','lt','litre']:
        return sayı * 1000
    elif birim in ['cl']:
        return sayı * 10
    elif birim in ['oz']:
        return sayı * 28.35
    else:
        return None # bilinmeyen 
    


exc['sayı']=exc['sayı'].fillna(0)
exc['birim']=exc['birim'].fillna('')
exc['Miktar_temiz']=exc.apply(lambda x: mka(x['sayı'], x['birim']), axis=1)
exc["Miktar_temiz"]=exc["Miktar_temiz"].fillna(0)
#kategorı
# kategorilerden ilkini alır
exc['first_katagori']=exc['katagori'].str.split(",").str[0]
# ülkede ilk ülkeyi alır
exc['ilk_ülke']=exc['ülke'].str.split(",").str[0]

print(exc[['Miktar_temiz', 'Miktar']].head(20))
exc.to_excel("C:\\Users\\buğra\\Desktop\\openfoodfacts\\food.xlsx", index=True)

print(exc.info())
print(exc.dtypes)
print(exc.shape)
print(exc.index)
print(exc.head())
print(exc.tail())
print(exc.describe())
print(exc.memory_usage())


print(exc.columns)

print(exc.nunique()) # her satırda kaç farklı değer var 
print(exc.isnull().sum())