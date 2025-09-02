import requests
import pandas as pd


urun=[ # Dairy & Eggs
    "Milk", "Skim Milk", "Almond Milk", "Soy Milk", "Eggs", "Butter", "Cheese", "Cheddar Cheese", "Mozzarella", 
    "Yogurt", "Greek Yogurt", "Cream", "Whipped Cream", "Cottage Cheese", "Sour Cream",
]
""" 
    # Bread & Bakery
    "White Bread", "Whole Wheat Bread", "Multigrain Bread", "Bagels", "Croissants", "Buns", "Pita Bread", 
    "Tortillas", "Muffins", "Donuts", "Pastries",

    # Meat & Poultry
    "Chicken Breast", "Chicken Wings", "Chicken Legs", "Ground Beef", "Beef Steak", "Pork Chops", "Bacon", 
    "Sausages", "Turkey Breast", "Ham", "Salami",

    # Seafood
    "Salmon", "Tuna", "Shrimp", "Crab", "Lobster", "Tilapia", "Sardines", "Cod", "Mussels",

    # Fruits
    "Apples", "Bananas", "Oranges", "Mandarins", "Grapes", "Strawberries", "Blueberries", "Raspberries", 
    "Watermelon", "Pineapple", "Kiwi", "Mango", "Papaya", "Peaches", "Pears", "Plums", "Cherries", "Avocados",

    # Vegetables
    "Potatoes", "Sweet Potatoes", "Onions", "Garlic", "Carrots", "Broccoli", "Cauliflower", "Spinach", 
    "Lettuce", "Kale", "Zucchini", "Cucumber", "Tomatoes", "Cherry Tomatoes", "Green Beans", "Peas", 
    "Eggplant", "Bell Peppers", "Hot Peppers", "Corn", "Asparagus", "Celery", "Mushrooms",

    # Grains & Pasta
    "Rice", "Basmati Rice", "Brown Rice", "Quinoa", "Oats", "Rolled Oats", "Pasta", "Spaghetti", "Macaroni", 
    "Lasagna Sheets", "Noodles", "Couscous", "Barley",

    # Baking & Cooking
    "Flour", "Whole Wheat Flour", "Cornmeal", "Sugar", "Brown Sugar", "Powdered Sugar", "Salt", "Sea Salt", 
    "Black Pepper", "Cinnamon", "Nutmeg", "Vanilla Extract", "Yeast", "Baking Powder", "Baking Soda",

    # Oils & Condiments
    "Olive Oil", "Vegetable Oil", "Canola Oil", "Sunflower Oil", "Coconut Oil", "Vinegar", "Apple Cider Vinegar", 
    "Soy Sauce", "Ketchup", "Mustard", "Mayonnaise", "Hot Sauce", "Barbecue Sauce", "Salad Dressing",

    # Canned & Packaged Foods
    "Tomato Sauce", "Tomato Paste", "Canned Tomatoes", "Canned Beans", "Canned Tuna", "Canned Corn", 
    "Canned Peas", "Canned Soup", "Instant Noodles", "Ready-to-Eat Meals",

    # Frozen Foods
    "Frozen Vegetables", "Frozen Fruit", "Frozen Pizza", "Frozen Fries", "Frozen Chicken Nuggets", 
    "Frozen Fish Fillets", "Frozen Dumplings", "Ice Cream", "Frozen Yogurt",

    # Beverages
    "Bottled Water", "Sparkling Water", "Mineral Water", "Soft Drinks", "Cola", "Orange Soda", "Lemonade", 
    "Energy Drinks", "Fruit Juice", "Apple Juice", "Orange Juice", "Cranberry Juice", "Iced Tea", 
    "Green Tea", "Coffee", "Ground Coffee", "Instant Coffee", "Tea Bags",

    # Breakfast & Snacks
    "Breakfast Cereal", "Cornflakes", "Granola", "Oatmeal", "Peanut Butter", "Almond Butter", "Jam", "Honey", 
    "Nutella", "Biscuits", "Cookies", "Crackers", "Chips", "Tortilla Chips", "Popcorn", "Pretzels", "Chocolate", 
    "Dark Chocolate", "Candy", "Gummies",

    # Household & Cleaning
    "Toilet Paper", "Paper Towels", "Napkins", "Facial Tissues", "Dish Soap", "Laundry Detergent", "Fabric Softener", 
    "Bleach", "All-Purpose Cleaner", "Glass Cleaner", "Sponges", "Trash Bags", "Aluminum Foil", "Plastic Wrap", 
    "Ziploc Bags",

    # Personal Care
    "Shampoo", "Conditioner", "Body Wash", "Bar Soap", "Toothpaste", "Toothbrush", "Mouthwash", "Deodorant", 
    "Shaving Cream", "Razors", "Hand Sanitizer", "Lotion",

    # Baby & Kids
    "Baby Formula", "Baby Food", "Diapers", "Baby Wipes",

    # Pet Supplies
    "Dog Food", "Cat Food", "Pet Treats" 
      """
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
print(exc.info())
print(exc.dtypes)
print(exc.shape())
print(exc.index)
print(exc.head())
print(exc.tail())
print(exc.describe())
print(exc.isnull().sum())

print(exc.memory_usage())

print(exc.nunique()) # her satırda kaç farklı değer var 