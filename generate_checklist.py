import os
import re

PROVINCES = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
    "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
    "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
    "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir",
    "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir",
    "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat",
    "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman",
    "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]

def normalize(name):
    # Mapping for Turkish characters
    tr_to_en = {
        'ı': 'i', 'I': 'I', 'İ': 'I', 'i': 'i',
        'ğ': 'g', 'Ğ': 'G',
        'ü': 'u', 'Ü': 'U',
        'ş': 's', 'Ş': 'S',
        'ö': 'o', 'Ö': 'O',
        'ç': 'c', 'Ç': 'C'
    }
    name = name.translate(str.maketrans(tr_to_en))
    name = name.lower()
    name = re.sub(r'[^a-z0-9]', '', name)
    return name

def get_visited_cities():
    regions = [
        "01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu",
        "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"
    ]
    visited = set()
    for r in regions:
        if os.path.exists(r):
            for c in os.listdir(r):
                if os.path.isdir(os.path.join(r, c)):
                    visited.add(normalize(c))
    return visited

def generate_checklist(visited_normalized):
    # Sort provinces alphabetically
    sorted_provinces = sorted(PROVINCES)
    
    # We will format it as a markdown table or simply a list or multiple columns.
    # Let's use a markdown unordered list with sub-lists (or just 3 columns in a markdown table)
    # Actually, a simple bulleted checklist with [ ] and [x] is standard.
    # To save vertical space, let's group them by regions, or just display a multi-column list?
    # Github markdown doesn't support generic multi-columns easily without tables.
    # Let's do a table with 3 columns.
    
    lines = ["", "## ✅ 81 İl Keşif Durumu (Provinces Checklist)", ""]
    lines.append("| İl | İl | İl |")
    lines.append("|---|---|---|")
    
    row = []
    for i, p in enumerate(sorted_provinces):
        norm_p = normalize(p)
        checked = "[x]" if norm_p in visited_normalized else "[ ]"
        item = f"- {checked} {p}"
        row.append(item)
        
        if len(row) == 3:
            lines.append(f"| {row[0]} | {row[1]} | {row[2]} |")
            row = []
            
    if row:
        while len(row) < 3:
            row.append("")
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} |")
        
    lines.append("")
    # Calculate progress
    visited_count = len([p for p in sorted_provinces if normalize(p) in visited_normalized])
    total = len(PROVINCES)
    percent = (visited_count / total) * 100
    
    # Progress bar with badges
    lines.insert(2, f"**Toplam Ziyaret Edilen İl:** {visited_count}/{total} (%{percent:.1f})")
    lines.insert(3, "")
    
    return "\n".join(lines)

def update_readme():
    visited = get_visited_cities()
    checklist = generate_checklist(visited)
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        
    # We want to insert this right after "## 📍 Mevcut Kapsam (Current Coverage)" table
    # Let's find "## 🧬 Sistem Mimarisi" and insert right before it
    
    if "## ✅ 81 İl Keşif Durumu" in content:
        print("Checklist already exists! Please update manually or remove first.")
        # But maybe we can replace the entire section. Let's just do an regex replace if it exists
        content = re.sub(r"## ✅ 81 İl Keşif Durumu.*?(?=## 🧬 Sistem Mimarisi)", checklist + "\n", content, flags=re.DOTALL)
    else:
        # Insert before "## 🧬 Sistem Mimarisi"
        content = content.replace("## 🧬 Sistem Mimarisi", checklist + "\n## 🧬 Sistem Mimarisi")
        
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated README with checklist. Visited: {len(visited)} provinces.")

if __name__ == "__main__":
    update_readme()
