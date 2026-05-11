import os
import random
import re
import uuid

# --- AYARLAR ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SANATCI_ADI = "Ferzan Özpetek"
KLASOR_ADI = os.path.join(BASE_DIR, "ferzan_seo_army")
RESIM_KLASORU = "img"

KEYWORDS = [
    "Ferzan Özpetek", "Ferzan Özpetek", "Ferzan Özpetek", "Ferzan Özpetek", "Ferzan Özpetek",
    "Ferzan Ozpetek", "Ferzan Ozpetek", "Ferzan Ozpetek", "Ferzan Ozpetek", "Ferzan Ozpetek",
    "Ferzan Özpetek son hali", "Ferzan Özpetek official", "Ferzan Özpetek kimdir",
    "Ferzan Özpetek biyografi", "Ferzan Özpetek movies", "Ferzan Özpetek news",
    "Ferzan Özpetek interview", "Ferzan Özpetek photo", "Ferzan Özpetek 2025",
    "Ferzan Özpetek İstanbul", "Ferzan Özpetek Roma", "Ferzan Özpetek Director",
    "Italian Turkish Director", "Ferzan Özpetek sineması", "Ferzan Özpetek yeni film",
    "Ferzan Özpetek kitapları", "Ferzan Özpetek röportaj", "Ferzan Özpetek ödülleri",
    "Ferzan Özpetek 2026", "Ferzan Ozpetek 2026","Ferzan Ozpetek Diamante", "Ferzan Ozpetek Diamante 2026",
    "Ferzan Ozpetek biography","Ferzan Ozpetek filmography","Ferzan Ozpetek latest news","Ferzan Ozpetek interview 2026",
    "Ferzan Ozpetek awards","Ferzan Ozpetek new movie Diamanti","Ferzan Ozpetek libri","Ferzan Ozpetek official website",
    "Ferzan Ozpetek cinematographic style","Ferzan Ozpetek biografia","Ferzan Ozpetek filmografia completa",
    "Ferzan Ozpetek ultime notizie","Ferzan Ozpetek intervista 2026","Ferzan Ozpetek libri e romanzi",
    "Ferzan Ozpetek nuovo film Diamanti","Ferzan Ozpetek Roma e Istanbul","Ferzan Ozpetek premi e riconoscimenti",
    "Ferzan Ozpetek teatro e regia",
    ]

def slugify(text):
    text = text.replace('I', 'i').replace('İ', 'i').replace('ı', 'i')
    text = text.lower()
    char_map = {'ş': 's', 'ç': 'c', 'ğ': 'g', 'ö': 'o', 'ü': 'u', ' ': '-'}
    for search, replace in char_map.items():
        text = text.replace(search, replace)
    text = re.sub(r'[^a-z0-9\-]', '', text)
    return text

def html_olustur(dosya_no, keyword, resim_dosya_adi):
    resim_yolu = f"{RESIM_KLASORU}/{resim_dosya_adi}"
    title = f"{SANATCI_ADI} - {keyword} - Resmi Görsel {dosya_no}"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <meta name="description" content="{SANATCI_ADI} {keyword} güncel görsel arşivi.">
        <style>
            body {{ font-family: sans-serif; text-align: center; padding: 20px; background-color: #f9f9f9; }}
            h1 {{ color: #333; }}
            img {{ max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin-top: 20px; }}
            .back-link {{ display: block; margin-top: 30px; font-weight: bold; text-decoration: none; color: #007bff; }}
        </style>
    </head>
    <body>
        <h1>{SANATCI_ADI} - {keyword}</h1>
        <img src="{resim_yolu}" alt="{SANATCI_ADI} {keyword}">
        <a href="index.html" class="back-link">⬅ Ana Galeriye Dön</a>
    </body>
    </html>
    """
    return html_content

def index_olustur(dosya_listesi):
    """Tüm sayfaları listeleyen ANA GİRİŞ SAYFASI (index.html) oluşturur."""
    linkler_html = ""
    for dosya in dosya_listesi:
        linkler_html += f'<li><a href="{dosya}">{dosya} - Görüntüle</a></li>\n'

    html_content = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{SANATCI_ADI} - Resmi Görsel Arşivi 2025</title>
        <style>
            body {{ font-family: sans-serif; padding: 40px; background-color: #fff; max-width: 800px; margin: 0 auto; }}
            h1 {{ border-bottom: 2px solid #333; padding-bottom: 10px; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin: 10px 0; border-bottom: 1px solid #eee; padding: 5px; }}
            a {{ text-decoration: none; color: #007bff; font-weight: bold; }}
            a:hover {{ color: #0056b3; }}
        </style>
    </head>
    <body>
        <h1>{SANATCI_ADI} - Dijital Arşiv (2025)</h1>
        <p>Aşağıdaki bağlantılar Google Görsel optimizasyonu için oluşturulmuş güncel kayıtlardır:</p>
        <ul>
            {linkler_html}
        </ul>
    </body>
    </html>
    """
    return html_content

def saldiri_baslat():
    if not os.path.exists(KLASOR_ADI):
        os.makedirs(KLASOR_ADI)
        
    tam_resim_yolu = os.path.join(KLASOR_ADI, RESIM_KLASORU)
    
    # Hata Kontrolü
    if not os.path.exists(tam_resim_yolu):
        print(f"HATA: '{KLASOR_ADI}' içinde '{RESIM_KLASORU}' klasörü yok!")
        return
    
    resim_listesi = [f for f in os.listdir(tam_resim_yolu) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not resim_listesi:
        print("HATA: img klasörü boş!")
        return

    print(f"--- OPERASYON BAŞLIYOR ---")
    
    # 1. Alt Sayfaları Oluştur
    for i in range(1, 51):
        secilen_keyword = random.choice(KEYWORDS)
        secilen_resim = random.choice(resim_listesi)
        
        benzersiz_id = str(uuid.uuid4().hex)[:6]
        temiz_keyword = slugify(secilen_keyword)
        dosya_adi_kisa = f"ferzan-ozpetek-{temiz_keyword}-{benzersiz_id}.html"
        dosya_adi_tam = os.path.join(KLASOR_ADI, dosya_adi_kisa)
        
        icerik = html_olustur(i, secilen_keyword, secilen_resim)
        with open(dosya_adi_tam, "w", encoding="utf-8") as f:
            f.write(icerik)
        
        print(f"[OK] {dosya_adi_kisa} oluşturuldu")

    # 2. ANA SAYFAYI (index.html) OLUŞTUR - TÜM DOSYALARI DAHİL ET
    tum_dosyalar = [f for f in os.listdir(KLASOR_ADI) if f.endswith('.html') and f != 'index.html']
    tum_dosyalar.sort(reverse=True) # İsteğe bağlı sıralama
    
    index_icerik = index_olustur(tum_dosyalar)
    with open(os.path.join(KLASOR_ADI, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_icerik)
    
    print(f"\n--- İŞLEM BAŞARILI: index.html oluşturuldu ---")
    print("Klasörü tekrar Netlify'a yükleyebilirsiniz.")

if __name__ == "__main__":
    saldiri_baslat()