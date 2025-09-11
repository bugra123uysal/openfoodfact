# OpenFoodFact

Bu proje, OpenFoodFacts verilerini kullanarak ürünlerin **besin puanı, kategori, marka, ülke ve miktar** açısından analizini içerir.  

## 🚀 İçerik

## proje hakkında bilgiler 
- url=https://world.openfoodfacts.org/
- Sütünlar: 'Ürün', 'Marka', 'Ad', 'Miktar', 'ülke', 'katagori', 'Besin-puanı'


### 1. fod.py (Veri Hazırlama)
- `food.xlsx` dosyasını okur.
- Eksik değerleri doldurur.
- Tekrar eden ürünleri siler.
- `Miktar` kolonunu standart hale getirir (tüm birimler grama çevrilir).
- Yeni kolonlar ekler:
  - `Miktar_temiz`
  - `first_katagori`
  - `ilk_ülke`

### 2. gra.py (Veri Görselleştirme)
- Besin puanı dağılımı (barplot)
- Ülkelere göre ürün sayısı (barplot)
- Kategorilere göre ürün sayısı (barplot)
- Markalara göre ürün sayısı (barplot)
- Miktar dağılımları (barplot)
- Heatmap: Besin puanı × kategori
- Histogram: Miktar dağılımı

## 📊 Kullanılan Kütüphaneler
- pandas
- numpy
- matplotlib
- seaborn

  


  
