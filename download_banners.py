import os
import json
import urllib.request
import urllib.parse
from urllib.error import URLError

REGIONS_MAP = {
    "01_Marmara": ["Istanbul", "Kocaeli", "Bursa"],
    "02_Ege": ["Denizli"],
    "03_Akdeniz": ["Antalya"],
    "04_IcAnadolu": ["Ankara", "Konya"],
    "05_Karadeniz": ["Amasya", "Corum", "Samsun", "Sinop", "Giresun", "Ordu"]
}

def get_city_image_url(city_name):
    query_city = city_name
    # Handle Turkish character specifics for Wikipedia querying
    if city_name == "Corum": query_city = "Çorum"
    if city_name == "Istanbul": query_city = "İstanbul"
    
    encoded_city = urllib.parse.quote(query_city)
    url = f"https://tr.wikipedia.org/w/api.php?action=query&titles={encoded_city}&prop=pageimages&format=json&pithumbsize=1200"
    
    req = urllib.request.Request(url, headers={'User-Agent': 'TravelLogScript/1.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data.get('query', {}).get('pages', {})
            for page_id, page_data in pages.items():
                if 'thumbnail' in page_data:
                    return page_data['thumbnail']['source']
    except Exception as e:
        print(f"Error fetching URL for {city_name}: {e}")
    return None

def download_image(url, save_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'TravelLogScript/1.0'})
    try:
        with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def main():
    for region, cities in REGIONS_MAP.items():
        if not os.path.exists(region):
            print(f"Directory {region} not found, skipping.")
            continue
            
        actual_folders = os.listdir(region)
        for folder in actual_folders:
            clean_city = folder.strip()
            lookup_key = clean_city
            if clean_city == "İstanbul": lookup_key = "Istanbul"
            if clean_city == "Çorum": lookup_key = "Corum"
            
            # Verify if this is one of our target cities mapped
            all_cities = [c for lst in REGIONS_MAP.values() for c in lst]
            if lookup_key in all_cities:
                print(f"Processing {clean_city}...")
                img_url = get_city_image_url(lookup_key)
                
                if img_url:
                    target_path = os.path.join(region, folder, "banner.jpg")
                    print(f"  -> Found image: {img_url}")
                    success = download_image(img_url, target_path)
                    print(f"  -> Saved to {target_path}: {success}")
                else:
                    print(f"  -> No Wikipedia page image found for {clean_city}.")

if __name__ == "__main__":
    main()
