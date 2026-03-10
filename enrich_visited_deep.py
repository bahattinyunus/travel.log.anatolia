import os

VISITED_DEEP_DETAILS = {
    "Istanbul": {
        "hikmet": "İstanbul bir şehirdir ki, yedi tepe üzerinde yedi veli bekler.",
        "quote": "\"İki denizin birleştiği yer... Hem Doğu'nun kalbini hem Batı'nın aklını cem eden yüce dergah.\"",
        "description": "Dünyanın gözbebeği, payitaht. Hem zahiri ihtişamı hem batıni derinliğiyle seyyahların sığınağı. Toprağında yatan sayısız sahabi, evliya ve dervişin duasıyla ayakta duran bu kadim şehir, her sokağında ayrı bir sır fısıldar. Süleymaniye'nin kubbesinden süzülen ışıkta Sinan'ın zikrini, Eyüp Sultan'ın avlusunda sadakat ve teslimiyetin yankısını duyarsınız. Boğaz'ın suları, adeta ilahi aşkın coşkunluğunu yansıtan bir ayna gibidir. Gündüzü ticaret ve dünya telaşıyla geçerken, gecesi dervişlerin huşusuyla sabaha erer.",
        "sufi_notes": "İstanbul'u layıkıyla gezmek, sadece taşını toprağını değil, üzerine sinmiş feyzi hissetmektir. Galata'da bir ney sesi duyduğunda dönmeye başlayan semazenlerin ruh haletine bürünmek, Üsküdar'da Aziz Mahmud Hüdayi hazretlerinin duasını hissedip yola o tevekkülle revan olmaktır.",
        "landmarks": ["Eyüp Sultan Camii", "Aziz Mahmud Hüdayi Türbesi", "Galata Mevlevihanesi", "Süleymaniye Camii"]
    },
    "Konya": {
        "hikmet": "Gel, ne olursan ol yine gel... Ama buraya aşkla gel.",
        "quote": "\"Ateş olmayan yerde duman tütmez. Benim gönlümde aşk ateşi yanmasaydı, şiirlerim böyle cihana yayılır mıydı?\" - Hz. Mevlana",
        "description": "Aşkın merkezi, Mevlana'nın yurdu. Hamdım, piştim, yandım diyenlerin durak noktası. Selçuklu'nun başkenti olan bu kadim şehir, sadece tarihi eserleriyle değil, göğe yükselen minarelerinden yayılan maneviyatıyla da kalpleri celbeder. Çöllerin ortasında bir vaha gibi, manevi kuraklığı çeken asi gönülleri serinleten sularla doludur. Şems'in yaktığı ateş, Mevlana'nın gönlünde harmanlanmış, asırlardır bu şehrin sokaklarına aşk ve vecd olarak yayılmıştır.",
        "sufi_notes": "Konya'da atılan her adım, 'Hamdım, piştim, yandım' sırrına ulaşma gayesini taşır. Sadreddin Konevi'nin felsefi derinliğiyle, Şems-i Tebrizi'nin ilahi cezbesi bu şehirde bir bütün olmuştur. Türbe ziyaretleri, sadece bir mekanı görmek değil, halden hale geçmenin bir talimidir.",
        "landmarks": ["Mevlana Müzesi", "Şems-i Tebrizi Türbesi", "Sadreddin Konevi Camii", "İnce Minareli Medrese"]
    },
    "Bursa": {
        "hikmet": "Bursa'da zaman, bir eski cami avlusunda sükutla geçer.",
        "quote": "\"Burası Osmanlı'nın doğduğu topraktır, her çınarında bir dua, her taşında bir himmet vardır.\"",
        "description": "Evliyalar şehri, Osmanlı'nın ilk payitahtı. Ulu bir çınar gibi kökleri tarihin derinliklerinde. Uludağ'ın eteklerine bir inci gerdanlık gibi dizilmiş olan bu şehir, yeşilin her tonunu barındırdığı gibi, kalbin de her türlü dinginliğine ev sahipliği yapar. Ulu Cami'nin o haşmetli direkleri arasında hissedilen tevazu, Somuncu Baba'nın fırınından yayılan bereketli kokularla birleşir. Bursa, ruhun dünyevi olan her türlü kirden arınıp, ilahi bir sükunete büründüğü yerdir.",
        "sufi_notes": "Emir Sultan'ın huzurunda boyun eğmek, Osman ve Orhan Gazi'nin türbelerinde cihan devleti kuran o ince iradeyi tefekkür etmektir. Su sesleriyle uyanıp, dua sesleriyle uykuya dalar bu şehrin dervişleri.",
        "landmarks": ["Ulu Cami", "Emir Sultan Külliyesi", "Yeşil Türbe", "Somuncu Baba Fırını", "Muradiye Külliyesi"]
    },
    "Ankara": {
        "hikmet": "Dışarısını imar ederken içerisini haraap etme.",
        "quote": "\"Nâgehân ol şâra vardım, Ol şârı ben yapılır gördüm. Ben dahi bile yapıldım, Taş ü toprak âresinde.\" - Hacı Bayram-ı Veli",
        "description": "Anadolu'nun kalbi, Hacı Bayram-ı Veli'nin manevi muhafızlığında bir şehir. Ankara sadece Cumhuriyet'in değil, asırlardır süregelen manevi bir dirilişin de merkezidir. Kalenin eteklerinden süzülen o eski zaman kokusu, Ahi şefkatiyle yoğrulmuş esnafın dualarına karışır. Augustus Tapınağı ile yan yana duran Hacı Bayram Camii, bu topraklardaki çok kültürlü ama tek hakikate yönelen irfanın en somut yüzüdür.",
        "sufi_notes": "Hacı Bayram-ı Veli hazretleri yoksulların ve yetimlerin sığınağı olmuş, dergahında hem gönülleri imar etmiş hem de tarlada alın teri dökmeyi öğretmiştir. Şehre bakan her seyyah, O'nun \"Ben de bile yapıldım\" düsturunu kalbine fısıldamalıdır.",
        "landmarks": ["Hacı Bayram-ı Veli Türbesi", "Taceddin Dergahı", "Ankara Kalesi", "Ahi Şerafeddin Camii"]
    },
    "Amasya": {
        "hikmet": "Dağları delmek zordur ama gönülleri delmek (feth etmek) daha zordur.",
        "quote": "\"Şehzadelerin talimgahı, suyun sükutla aktığı, dağların huşu ile durduğu kutlu diyar.\"",
        "description": "Şehzadeler şehri, Ferhat ile Şirin'in diyarı. Yeşilırmak'ın aynasında tarihini izleyen kent. Amasya vadinin içine gizlenmiş, sırlarını sadece ona gönül verenlere açan mütevazı bir şehirdir. Akşamları kayalara oyulmuş mezarlara vuran ışıklarla aydınlanan şehir, faniliğin ve bekanın muazzam bir tezatını sunar. Su dolaplarının yüzyıllardır söylediği ninni, dervişlerin zikrine eşlik eder.",
        "sufi_notes": "Amasya'da Ferhat'ın Şirin'e duyduğu mecazi aşkın nasıl ilahi aşka dönüştüğünü tefekkür etmek gerekir. Şeyh Hamdullah'ın yazdığı mushaflardaki her bir harfin zarafeti, Amasya insanının kalbine yansımıştır.",
        "landmarks": ["Kral Kaya Mezarları", "Şeyh Hamdullah Türbesi", "II. Bayezid Külliyesi", "Yalıboyu Evleri"]
    },
    "Corum": {
        "hikmet": "Geçmişin izleri üzerindeki bugünün bereketini gör.",
        "quote": "\"Toprağın bereketlendiği, kadim medeniyetlerin fısıltılarının rüzgara karıştığı il.\"",
        "description": "Hititlerin kadim diyarı, leblebi kokulu Anadolu şehri. Çorum, gösterişten uzak, bağrında binlerce yıllık bir sırrı saklayan mütavazı bir ev sahibidir. Hattuşaş'ın yıkıntıları arasında yürürken insan, bir zamanlar cihanı titreten krallıkların şimdi rüzgarda savrulan topraktan ibaret olduğunu görür ve kibirden arınır. Ulu Cami'deki sükunet, şehrin candan insanlarıyla bütünleşir.",
        "sufi_notes": "Bu şehir bize her saltanatın bir gün biteceğini, sadece Allah'ın vekilliğinin ve ilahi muhabbetin baki kalacağını haykırır. Çorum'un bereketli toprakları, kalbine merhamet ekenin merhamet biçeceğinin en büyük delilidir.",
        "landmarks": ["Hattuşaş Antik Kenti", "Alacahöyük", "Murad-ı Râbi Ulu Cami", "İncesu Kanyonu"]
    },
    "Samsun": {
        "hikmet": "Her büyük yürüyüş ilk bir adımla başlar.",
        "quote": "\"Umut, güneşin denizden doğuşuyla bir olup kara bulutları dağıttığı yerdedir.\"",
        "description": "Milli Mücadele'nin meşale şehri. Karadeniz'in giriş kapısı. Hırçın dalgaların umuda dönüştüğü, zulme ve karanlığa karşı ilk adımın atıldığı kutlu rıhtım. Samsun, sadece yakın tarihin değil, Amazonların efsanelerinden, ilk çağ yerleşimlerine kadar uzanan bir direniş ve azim diyarıdır. Göğü ve denizi ayıran o derin mavi çizgi, seyyaha sonsuzluğun kapılarını aralar.",
        "sufi_notes": "Nasıl ki bağımsızlık için atılan ilk adım bu şehirden başladıysa, insanın nefsine karşı açacağı o büyük cihad (cihad-ı ekber) da niyet denizine atılan ilk adamı gerektirir. Burada denizin dalgası, dervişin kalbindeki coşkunlukla bir atar.",
        "landmarks": ["Onur Anıtı", "Bandırma Vapuru", "Amisos Tepesi", "Göğceli (Ahşap) Camii"]
    },
    "Sinop": {
        "hikmet": "Gölge etme başka ihsan istemem.",
        "quote": "\"Mutluluğun sırrı çok şeye sahip olmakta değil, az şeye ihtiyaç duymaktadır.\"",
        "description": "Mutluluğun ve sükunetin şehri. Karadeniz'in en kuzey ucu. Dalgaların dövdüğü kaleleri ve tarih boyunca hüznü barındıran cezaeviyle zıtlıkların uyumunu sergileyen Sinop, inzivaya çekilmek isteyen ruhlar için bir barınaktır. Denizin kokusu ve ormanın fısıltısı, dünya telaşını ardında bırakanlara teselli verir.",
        "sufi_notes": "Diyojen'in dünya malından vazgeçişini anımsatan bu şehir, mutasavvıfların 'Terk, terk etmeyi de terk et' anlayışına ne kadar yakındır. Eski hapishanede yaşanan acıları tefekkür ederken, insanın esas zindanının kendi bedeni ve nefsi olduğunu anlar insan.",
        "landmarks": ["Tarihi Sinop Cezaevi", "Sinop Kalesi", "Hamsilos Koyu", "Erfelek Şelaleleri"]
    },
    "Giresun": {
        "hikmet": "Denizin cömertliği insanın tevazusuyla birleşir.",
        "quote": "\"Yeşille mavinin sırrına erdiği, bereketin dallardan sarktığı Karadeniz yurdu.\"",
        "description": "Fındığın ve kirazın ana vatanı. Mavi ile yeşilin kucaklaştığı yer. Şehrin sokaklarında dolaşırken dağlardan gelen yayla havası ve denizden esen iyot kokusu birbirine karışır. Giresun Adası'ndaki söylenceler, zeytinlik semtindeki tarihi evlerin zerafetiyle bir bütün olur. Burada zaman ağır işler, insanlar denizin ve yağmurun ritmine göre yaşar.",
        "sufi_notes": "Fındık ağacının ağır yükü altında nasıl eğildiğini görmek, kamil bir insanın ilim ve irfanla doldukça nasıl tevazuyu kuşandığının bir ispatıdır. Giresun'da tabiat, hal diliyle Allah'ı tesbih eder.",
        "landmarks": ["Giresun Kalesi", "Zeytinlik Semti", "Giresun Adası", "Kuzalan Şelalesi"]
    },
    "Ordu": {
        "hikmet": "Yükseklere çıkmadan ufku göremezsin.",
        "quote": "\"Dereleri yukarı akan, bulutların yoldaş olduğu yüksek dağların hırçın çocuğu.\"",
        "description": "Deresi yukarı akan, fındığın diyarı, Karadeniz'in nazlı şehri. Ordu'nun dağları denize öyle ani kavuşur ki, insan Boztepe'den aşağı bakarken faniliğini hisseder. Karadeniz'in o coşkulu doğası burada en asil halini almıştır. Vadilerin içindeki ince yollar, sarp yamaçlara tutunan köyler, burada yaşamanın bir mücadele ve aynı zamanda bir şükür vesilesi olduğunu hatırlatır.",
        "sufi_notes": "Boztepe'den uçsuz bucaksız Karadeniz ufkuna bakmak, vahdetin (birliğin) denizinde kaybolmaya benzer. Tıpkı Kurul Kalesi'nde kazı yapan arkeologun geçmişin sırrını aradığı gibi, ormanda yalnız başına yürüyen bir derviş de kalbinin derinliklerindeki defineyi kazar.",
        "landmarks": ["Boztepe", "Yason Burnu", "Kurul Kalesi", "Perşembe Yaylası"]
    },
    "Kocaeli": {
        "hikmet": "Emek, en büyük hazinedir.",
        "quote": "\"Taşın terlediği, demirin su verildiği, rızkını arayanların büyük yurdu.\"",
        "description": "Sanayinin ve tarihin iç içe geçtiği, Marmara'nın kilit noktası. Kocaeli, bir yanı fabrikaların dumanıyla tüterken, diğer yanı Kartepe'nin beyaz karlarıyla ve Maşukiye'nin şırıl şırıl akan dereleriyle serinleyen bir şehirdir. Geçmişin İzmit'i, bugün emeğin ve alın terinin başkentidir. Roma'dan Osmanlı'ya süzülen tarih, yerini modern çağın telaşına bırakmış olsa da, şehrin ruhundaki o asil duruş hiç kaybolmamıştır.",
        "sufi_notes": "Makine çarkları arasında atılan ter, helalinden rızık aramanın en büyük ibadet sayıldığı İslam ahlakının bir tezahürüdür. Burada fabrikalarda vardiyadan çıkan işçinin yüzündeki yorgunluk, rıza makamında bir dervişin tebessümüne denktir.",
        "landmarks": ["İzmit Saat Kulesi", "Osman Hamdi Bey Evi", "Kartepe", "Sekapark"]
    },
    "Antalya": {
        "hikmet": "Güneşin her gün yeniden doğuşu, umudun bitmeyeceğinin delilidir.",
        "quote": "\"Dağların heybetiyle denizin şefkatinin buluştuğu kadim medeniyetler ocağı.\"",
        "description": "Akdeniz'in incisi, kadim uygarlıkların limanı. Olympos'un sönmeyen ateşi, Kaleiçi'nin dar ve sarmal sokaklarına düşen dar sokakların sarmaşıkları, Antalya'yı sadece bir cennet değil, aynı zamanda manevi bir arınma havzası yapar. Roma krallarının, Selçuklu sultanlarının adımladığı taşlarda yürümek, zamanın göreceliliğini hissetmektir. Ilık rüzgarı bedeni sararken, denizin mavisi kalpte sonsuz bir sükunet bırakır.",
        "sufi_notes": "Hadrian Kapısı'ndan geçerken asırların ne kadar çabuk geçtiği, geriye sadece yapılan amellerin kalacağı idrak edilir. Akdeniz'in dalgaları, Allah'ın 'Hayy' (Diri) isminin sürekli tecellisini yansıtır.",
        "landmarks": ["Kaleiçi", "Hadrian Kapısı", "Yivli Minare Camii", "Olympos Antik Kenti", "Kaputaş Plajı"]
    },
    "Denizli": {
        "hikmet": "Su gibi aziz ol, aktığın yeri güzelleştir.",
        "quote": "\"Beyaz kayaların içinden sızan şifa, toprağın taştan bile nur çıkardığının kanıtıdır.\"",
        "description": "Pamuktan kalelerin, Hierapolis'in şifalı sularının şehri. Denizli, Ege'nin iç kesimlerinde tarih ve jeolojinin mucizevi birleşimidir. Travertenlerin o saf beyazlığı, inanan bir kalbin günahlardan arınmış halini sembolize eder adeta. Antik Laodikeia ve Hierapolis'in kalıntıları arasında dolaşırken, eski inançların yerini hakikatin nasıl aldığını gözlemlersiniz. Dokumacılığın kalbi olan bu şehir, insanın ince ince işlediği kader bağlarını andırır.",
        "sufi_notes": "Sıcak suların yerin derinliklerinden çıkıp taşları beyaza boyaması gibi, zikrullah (Allah'ın anılması) da insanın kapkara olmuş kalbinden fışkırıp onu pamuk gibi bembeyaz ve yumuşak kılar. Denizli, insanın içine akan şifanın yeryüzündeki yansımasıdır.",
        "landmarks": ["Pamukkale Travertenleri", "Hierapolis Antik Kenti", "Laodikeia", "Karahayıt Şifalı Suları"]
    }
}

REGIONS_MAP = {
    "01_Marmara": ["Istanbul", "Kocaeli", "Bursa"],
    "02_Ege": ["Denizli"],
    "03_Akdeniz": ["Antalya"],
    "04_IcAnadolu": ["Ankara", "Konya"],
    "05_Karadeniz": ["Amasya", "Corum", "Samsun", "Sinop", "Giresun", "Ordu"]
}

def enrich_visited():
    for region, cities in REGIONS_MAP.items():
        if not os.path.exists(region):
            continue
        
        # Match exact folder names in the directory
        actual_folders = os.listdir(region)
        
        for folder in actual_folders:
            clean_city = folder.strip()
            # If standard ascii matching
            lookup_key = clean_city
            if clean_city == "İstanbul": lookup_key = "Istanbul"
            if clean_city == "Çorum": lookup_key = "Corum"
            
            if lookup_key in VISITED_DEEP_DETAILS:
                
                details = VISITED_DEEP_DETAILS[lookup_key]
                file_path = os.path.join(region, folder, "README.md")
                
                content = f"# 📍 {clean_city} - Seyahat ve Tefekkür Notları\n\n"
                content += f"## 📜 Şehir Manifestosu\n> \"{details['hikmet']}\"\n"
                content += f"> {details['quote']}\n\n"
                content += f"### 🌍 Şehrin Ruhu ve Hakikati\n{details['description']}\n\n"
                content += f"### 🕊️ Batıni Tefekkür (Sufi Perspektifi)\n{details['sufi_notes']}\n\n"
                content += "### ✨ Zâhiri ve Bâtıni Duraklar\nSeyyahın adımlaması ve ibret alması tavsiye edilen mukaddes ve tarihi mekanlar:\n"
                
                for loc in details['landmarks']:
                    content += f"- [ ] **{loc}**\n"
                    
                content += "\n---\n*Bu il bizzat seyyah tarafından ziyaret edilmiş, idrak edilmiş ve kayıt altına alınmıştır.* ✅\n"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Deeply enriched: {file_path}")

if __name__ == "__main__":
    enrich_visited()
