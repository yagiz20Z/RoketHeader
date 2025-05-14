import os
import datetime
import re

    ####################### ESKİSİNİ SİLER VE YENİSİNİ EKLER #######################
####################### SADECE MAİN.C VE FREERTOS DOSYASINA HEADER ATAR  #######################



# Çalışılan dizin
target_dir = os.getcwd()

# Header'ı oluştur
def create_header(file_path):
    try:
        created_ts = os.path.getctime(file_path)
        dateData = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        created_date = datetime.datetime.fromtimestamp(created_ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        created_date = "Tarih alınamadı"

    # ASCII Art içeren header (raw f-string: rf""")
    header = rf"""/*
*
*        ^
*       /^\\
*      /___\\         YILDIZ ROKET TAKIMI
*     |=   =|        
*     |     |        Olusturulma Tarihi: {created_date}
*     |     |        Tarih             : {dateData}
*     |     |
*    /|##!##|\\
*   / |##!##| \\
*  /  |##!##|  \\
* |  / ^ | ^ \  |                                       YILDIZDAN
* | /  ( | )  \ |
* |/   ( | )   \|                                                                YILDIZLARA
*     ((   ))                                                                       
*    ((  :  ))
*    ((  :  ))
*     ((   ))
*      (( ))                     
*       ( )
*        .
*      .. ..
*    .........
* ... ...... ....
* ************************************************************************************
*/
"""
    return header

# Header'ı silen fonksiyon
def remove_old_header(content):
    # Header'ı silmek için regex kullanıyoruz
    pattern = re.compile(r"/\*.*?YILDIZ ROKET TAKIMI.*?\*/\n*", re.DOTALL)
    return re.sub(pattern, '', content, count=1)

# Dosyaları tara ve eski header'ı silip yenisini ekle
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(('main.c', 'app_freertos.c')):  # .c ve .h dosyalarını hedef al
            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Eğer eski header varsa sil
            if "YILDIZ ROKET TAKIMI" in content:
                content = remove_old_header(content)
                print(f"🧹 Eski header silindi: {file}")

            # Yeni header'ı ekle
            new_header = create_header(file_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_header + '\n' + content)
            print(f"✅ Yeni header eklendi: {file}")

print("🎉 Tüm işlem tamamlandİ.")