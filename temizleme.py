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
*        
*       
*/
"""
    return header

# Header'ı silen fonksiyon
def remove_old_header(content):
    # Header'ı silmek için regex kullanıyoruz
    pattern = re.compile(r"/\*.*?YILDIZ ROKET TAKIMI.*?\*/\n*", re.DOTALL)
    return re.sub(pattern, '', content, count=1)


print("Header silindi.")