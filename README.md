# OpenFoodFact

Bu proje, OpenFoodFacts verilerini kullanarak ürünlerin **besin puanı, kategori, marka, ülke ve miktar** açısından analizini içerir.  


## 🚀 İçerik

## proje hakkında bilgiler 
- url=https://world.openfoodfacts.org/
- Sütünlar:'Ürün', 'Marka', 'Ad', 'Miktar', 'ülke', 'katagori', 'Besin-puanı',
       'birim', 'sayı', 'Miktar_temiz', 'first_katagori', 'ilk_ülke'
    


### 1. fod.py (Veri Hazırlama)
- `food.xlsx` dosyasını okur.
- Eksik değerleri doldurur.
- Tekrar eden ürünleri siler.
- `Miktar` kolonunu standart hale getirir (tüm birimler grama çevrilir).
- Yeni kolonlar ekler:
  - `Miktar_temiz`
  - `first_katagori`
  - `ilk_ülke`
 

## Veri Keşfi

### print(exc.info())
#   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Ürün            684 non-null    object
 1   Marka           684 non-null    object
 2   Ad              684 non-null    object
 3   Miktar          684 non-null    object
 4   ülke            684 non-null    object
 5   katagori        684 non-null    object
 6   Besin-puanı     684 non-null    object
 7   birim           684 non-null    object
 8   sayı            684 non-null    object
 9   Miktar_temiz    684 non-null    float64
 10  first_katagori  684 non-null    object
 11  ilk_ülke        684 non-null    object
print(exc.dtypes)
## print(exc.shape) 
(684, 12)
### print(exc.index)
Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
       ...
       677, 678, 679, 680, 681, 682, 683, 684, 685, 686],
      dtype='int64', length=684)

### print(exc.describe())
      Miktar_temiz
count    684.000000
mean     334.463692
std      445.129919
min        0.000000
25%        0.000000
50%      225.000000
75%      450.000000
max     5000.000000


### print(exc.memory_usage())
Index             5472
Ürün              5472
Marka             5472
Ad                5472
Miktar            5472
ülke              5472
katagori          5472
Besin-puanı       5472
birim             5472
sayı              5472
Miktar_temiz      5472
first_katagori    5472
ilk_ülke          5472


### print(exc.nunique())   
Ürün               70
Marka             450
Ad                593
Miktar            267
ülke              255
katagori          534
Besin-puanı         7
birim              33
sayı              134
Miktar_temiz      122
first_katagori    117
ilk_ülke          107

### print(exc.isnull().sum())
Ürün              0
Marka             0
Ad                0
Miktar            0
ülke              0
katagori          0
Besin-puanı       0
birim             0
sayı              0
Miktar_temiz      0
first_katagori    0
ilk_ülke          0

### 2. gra.py (Veri Görselleştirme)
- Besin puanı dağılımı (barplot)
- Ülkelere göre ürün sayısı (barplot)
- Kategorilere göre ürün sayısı (barplot)
- Markalara göre ürün sayısı (barplot)
- Miktar dağılımları (barplot)
- Histogram: Miktar dağılımı

## 📊 Kullanılan Kütüphaneler
- pandas
- numpy
- matplotlib
- seaborn

## Analiz 
En çok hangi markanın ürünü var: Tesco
En çok hangi kategori var: Plant-based foods and beverages
En fazla hangi ülke var: France
En çok hangi besin puanı var: A 


## Grafikler 

<img width="1751" height="854" alt="Ekran görüntüsü 2025-10-02 212941" src="https://github.com/user-attachments/assets/a60908fe-bebf-40c6-aa01-728f77086351" />
  
<img width="1391" height="832" alt="Ekran görüntüsü 2025-10-02 212341" src="https://github.com/user-attachments/assets/03346b0c-072c-4429-95ef-d504c4daf6da" />

<img width="1784" height="891" alt="Ekran görüntüsü 2025-10-02 212211" src="https://github.com/user-attachments/assets/bf4f93c6-d7bb-4c7a-8a96-bf94e793b053" />

<img width="1615" height="920" alt="Ekran görüntüsü 2025-10-02 211950" src="https://github.com/user-attachments/assets/0006e51a-4cd3-46ce-8792-5623f9456e31" />

<img width="1716" height="855" alt="Ekran görüntüsü 2025-10-02 212748" src="https://github.com/user-attachments/assets/c3e4f174-1916-4526-b657-05fe4e189d5e" />




