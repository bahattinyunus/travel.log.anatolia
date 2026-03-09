import os

# Map regions correctly
regions_map = {
    '01_Marmara': 'Marmara',
    '02_Ege': 'Ege',
    '03_Akdeniz': 'Akdeniz',
    '04_IcAnadolu': 'İç Anadolu',
    '05_Karadeniz': 'Karadeniz',
    '06_DoguAnadolu': 'Doğu Anadolu',
    '07_GuneydoguAnadolu': 'Güneydoğu Anadolu'
}

provinces = {
    '01_Marmara': ['Balikesir', 'Bilecik', 'Bursa', 'Canakkale', 'Edirne', 'Istanbul', 'Kirklareli', 'Kocaeli', 'Sakarya', 'Tekirdag', 'Yalova'],
    '02_Ege': ['Afyonkarahisar', 'Aydin', 'Denizli', 'Izmir', 'Kutahya', 'Manisa', 'Mugla', 'Usak'],
    '03_Akdeniz': ['Adana', 'Antalya', 'Burdur', 'Hatay', 'Isparta', 'Kahramanmaras', 'Mersin', 'Osmaniye'],
    '04_IcAnadolu': ['Aksaray', 'Ankara', 'Cankiri', 'Eskisehir', 'Karaman', 'Kayseri', 'Kirikkale', 'Kirsehir', 'Konya', 'Nevsehir', 'Nigde', 'Sivas', 'Yozgat'],
    '05_Karadeniz': ['Amasya', 'Artvin', 'Bartin', 'Bayburt', 'Bolu', 'Corum', 'Duzce', 'Giresun', 'Gumushane', 'Karabuk', 'Kastamonu', 'Ordu', 'Rize', 'Samsun', 'Sinop', 'Tokat', 'Trabzon', 'Zonguldak'],
    '06_DoguAnadolu': ['Agri', 'Ardahan', 'Bingol', 'Bitlis', 'Elazig', 'Erzincan', 'Erzurum', 'Hakkari', 'Igdir', 'Kars', 'Malatya', 'Mus', 'Tunceli', 'Van'],
    '07_GuneydoguAnadolu': ['Adiyaman', 'Batman', 'Diyarbakir', 'Gaziantep', 'Kilis', 'Mardin', 'Siirt', 'Sanliurfa', 'Sirnak']
}

# Proper turkish names
tr_names = {
    'Adana': 'Adana', 'Adiyaman': 'Adıyaman', 'Afyonkarahisar': 'Afyonkarahisar', 'Agri': 'Ağrı',
    'Aksaray': 'Aksaray', 'Amasya': 'Amasya', 'Ankara': 'Ankara', 'Antalya': 'Antalya', 'Ardahan': 'Ardahan',
    'Artvin': 'Artvin', 'Aydin': 'Aydın', 'Balikesir': 'Balıkesir', 'Bartin': 'Bartın', 'Batman': 'Batman',
    'Bayburt': 'Bayburt', 'Bilecik': 'Bilecik', 'Bingol': 'Bingöl', 'Bitlis': 'Bitlis', 'Bolu': 'Bolu',
    'Burdur': 'Burdur', 'Bursa': 'Bursa', 'Canakkale': 'Çanakkale', 'Cankiri': 'Çankırı', 'Corum': 'Çorum',
    'Denizli': 'Denizli', 'Diyarbakir': 'Diyarbakır', 'Duzce': 'Düzce', 'Edirne': 'Edirne', 'Elazig': 'Elazığ',
    'Erzincan': 'Erzincan', 'Erzurum': 'Erzurum', 'Eskisehir': 'Eskişehir', 'Gaziantep': 'Gaziantep',
    'Giresun': 'Giresun', 'Gumushane': 'Gümüşhane', 'Hakkari': 'Hakkari', 'Hatay': 'Hatay', 'Igdir': 'Iğdır',
    'Isparta': 'Isparta', 'Istanbul': 'İstanbul', 'Izmir': 'İzmir', 'Kahramanmaras': 'Kahramanmaraş', 'Karabuk': 'Karabük',
    'Karaman': 'Karaman', 'Kars': 'Kars', 'Kastamonu': 'Kastamonu', 'Kayseri': 'Kayseri', 'Kilis': 'Kilis',
    'Kirikkale': 'Kırıkkale', 'Kirklareli': 'Kırklareli', 'Kirsehir': 'Kırşehir', 'Kocaeli': 'Kocaeli', 'Konya': 'Konya',
    'Kutahya': 'Kütahya', 'Malatya': 'Malatya', 'Manisa': 'Manisa', 'Mardin': 'Mardin', 'Mersin': 'Mersin',
    'Mugla': 'Muğla', 'Mus': 'Muş', 'Nevsehir': 'Nevşehir', 'Nigde': 'Niğde', 'Ordu': 'Ordu', 'Osmaniye': 'Osmaniye',
    'Rize': 'Rize', 'Sakarya': 'Sakarya', 'Samsun': 'Samsun', 'Sanliurfa': 'Şanlıurfa', 'Siirt': 'Siirt',
    'Sinop': 'Sinop', 'Sirnak': 'Şırnak', 'Sivas': 'Sivas', 'Tekirdag': 'Tekirdağ', 'Tokat': 'Tokat',
    'Trabzon': 'Trabzon', 'Tunceli': 'Tunceli', 'Usak': 'Uşak', 'Van': 'Van', 'Yalova': 'Yalova', 'Yozgat': 'Yozgat',
    'Zonguldak': 'Zonguldak'
}

def generate_template(province_dir, tr_name, region_name):
    return f"""# {tr_name}

## 📍 Konum Bilgisi
* **Bölge:** {region_name}
* **İl:** {tr_name}

## 📝 Gezi Notları
*Bu şehre ait bilgiler veya gezi notları daha sonra eklenecektir.*

Türkiye'nin {region_name} bölgesinde yer alan {tr_name}, keşfedilmeyi bekleyen birçok tarihi ve doğal güzelliğe ev sahipliği yapmaktadır.

### 🏛️ Gezilecek Yerler
* [Gezilecek Yerler eklenecek]

### 🍽️ Yeme - İçme
* [Yöresel lezzetler eklenecek]

## 📸 Fotoğraf Galerisi
<!-- Buraya assets klasöründeki fotoğrafları ekleyin -->

## 💡 İpuçları & Tavsiyeler
* [Tavsiye Ekle]
"""

for region, cities in provinces.items():
    region_tr = regions_map[region]
    for city in cities:
        city_dir = os.path.join(region, city)
        os.makedirs(city_dir, exist_ok=True)
        
        readme_path = os.path.join(city_dir, 'README.md')
        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(generate_template(city_dir, tr_names[city], region_tr))
            print(f"Created {readme_path}")
        else:
            # check if it just has default 'Unknown' text maybe? Or maybe it already has content.
            # Let's read first 100 chars
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read(150)
            if "Unknown" in content or len(content.strip()) < 10:
                print(f"Overwriting minimal {readme_path}")
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(generate_template(city_dir, tr_names[city], region_tr))
            else:
                print(f"Skipped {readme_path} (already exists with content)")

print("Done generating province folders.")
