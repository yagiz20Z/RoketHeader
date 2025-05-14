import os
import re

target_dir = os.getcwd()  # Çalışma dizini

# Header'ı silen fonksiyon
def remove_old_header(content):
    # Header'ı silmek için regex kullanıyoruz
    pattern = re.compile(r"/\*.*?YILDIZ ROKET TAKIMI.*?\*/\n*", re.DOTALL)
    return re.sub(pattern, '', content, count=1)

# Dosyaları tara ve eski header'ı sil
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(('.c', '.h')):  # .c ve .h dosyalarını hedef al
            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Eğer eski header varsa sil
            if "YILDIZ ROKET TAKIMI" in content:
                content = remove_old_header(content)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"🧹 Eski header silindi: {file}")
            else:
                print(f"✅ Header zaten yok: {file}")

print("🎉 Eski header'lar başarıyla silindi.")
