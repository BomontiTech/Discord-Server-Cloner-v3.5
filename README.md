# 🔮 DISCORD SERVER CLONER OPEN-SOURCE v3.5

Rengarenk mor-pembe arayüze sahip, hızlı, stabil ve tamamen Discord API kurallarına uygun resmi sunucu kopyalama ve şablon taşıma otomasyonu!

A fast, stable, and official Discord server cloner automation with a colorful purple-pink interface, fully compliant with Discord API guidelines!

---

## 👑 Geliştirici / Developer
Developed with 💜 by **Bomonti Automation**

---

## ✨ Özellikler / Features

- 📶 **v3.5 Kararlı Sürüm:** En güncel `discord.py` altyapısı ve resmi ağ geçitleri (Gateway) üzerinden maksimum kararlılıkla çalışır.
- 👑 **Rol Klonlama:** Hedef sunucudaki tüm rolleri, özel renklerini ve gelişmiş yetki ayarlarını (Yönetici, susturma vb.) birebir sıfırdan inşa eder.
- 📂 **Hiyerarşik Tasarım:** Tüm kategori başlıklarını, metin odalarını ve ses kanallarını orijinal sıralamasıyla boş sunucunuza aktarır.
- 🎨 **Şık Konsol Arayüzü:** `fade` kütüphanesi sayesinde göz alıcı mor-pembe geçiş efektli bir terminal ekranı sunar.

---

## 🛠️ Kurulum ve Çalıştırma / Installation & Usage

### 1. Kütüphaneleri Yükleyin / Install Dependencies
Klasörünüzde CMD açın ve gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

### 2. Bot Token Girişi / Configuration
`main.py` dosyasının en altındaki `TOKEN` alanına Discord Developer Portal'dan aldığınız resmi bot tokenınızı yapıştırın.

### 3. Çalıştırın / Run
Hazırladığımız `baslat.bat` dosyasına çift tıklayarak botu saniyeler içinde yayına alın:
```bash
py main.py
```

---

## 📢 Kullanım Talimatı / Usage Instructions

1. Botu hem **kopyalamak istediğiniz (hedef) sunucuya** hem de kendi **boş sunucunuza** yönetici yetkisiyle davet edin.
2. Kendi boş sunucunuzun metin kanalına geçerek şu komutu ateşleyin:
```text
!kopyala [HEDEF_SUNUCU_ID]
```
3. Bot saniyeler içinde eski odaları temizleyecek ve yeni sunucu tasarımınızı gözünün önünde inşa edecektir!

---

## ⚖️ Yasal Uyarı / Legal Notice
Bu proje tamamen eğitim, sunucu yedekleme ve açık kaynak geliştirme amaçlı üretilmiştir. Discord API politikalarına ve Hizmet Şartları'na (ToS) %100 uyumludur. Hesap riski barındırmaz.
