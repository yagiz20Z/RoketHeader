import os
import datetime
import re

target_dir = os.getcwd()  # Çalışma dizini

# Yeni header'ı oluştur
def create_new_header(file_path):
    try:
        created_ts = os.path.getctime(file_path)
        created_date = datetime.datetime.fromtimestamp(created_ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        created_date = "Tarih alınamadı"

    # Yeni header (ASCII art + tarih)
    header = rf"""/*
*
*        ^
*       /^\\
*      /___\\         YILDIZ ROKET TAKIMI
*     |=   =|        
*     |     |        File Created: {created_date}
*     |     |        
*     |     |
*    /|##!##|\\
*   / |##!##| \\
*  /  |##!##|  \\
* |  / ^ | ^ \  |
* | /  ( | )  \ |
* |/   ( | )   \|
*     ((   ))
*    ((  :  ))
*    ((  :  ))
*     ((   ))
*      (( ))
*       ( )
*        .
*        .
*        .
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
        if file.endswith(('.c', '.h')):  # .c ve .h dosyalarını hedef al
            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Eğer eski header varsa sil
            if "YILDIZ ROKET TAKIMI" in content:
                content = remove_old_header(content)
                print(f"🧹 Eski header silindi: {file}")

            # Yeni header'ı ekle
            new_header = create_new_header(file_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_header + '\n' + content)
            print(f"✅ Yeni header eklendi: {file}")

print("🎉 Tüm işlem tamamlandı.")
