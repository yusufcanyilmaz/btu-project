# BTU BLM101_Project
Öğrenci Bilgileri: Yusufcan Yılmaz 25360859310

Proje Konusu: Veri Depolama ve Sayısal Sistemler

YouTube Linki: https://www.youtube.com/watch?v=fRl7dNoooyc

Proje Açıklaması: 
### Kodun ne yaptığı
Bu Python programı, kullanıcıdan alınan onluk tabandaki tam sayıları bilgisayar mimarisine uygun şekilde 16-bitlik ikilik (binary) ve onaltılık (hexadecimal) sistemlere dönüştürerek verinin donanım seviyesindeki temsilini simüle eder.
### Nasıl çalıştırılacağı (kurulum gerekip gerekmediği)
Kodu herhangi bir metin düzenleyiciye yapıştırıp .py uzantısıyla kaydettikten sonra, terminal veya komut satırı üzerinden ilgili dizinde python dosya_adi.py komutunu çalıştırmanız programı başlatmak için yeterlidir.
### Kodun Çalışma Mantığı
Kodun çalışma algoritması, temel aritmetik operatörler ve mantıksal döngüler aracılığıyla veriyi katmanlı bir şekilde işlemektedir; öncelikle girilen sayı pozitifse klasik **"ikiye bölme ve kalanları sıralama"** döngüsüyle saf ikilik karşılığı elde edilirken, negatif sayılarda donanım düzeyindeki **İkiye Tümleyen (Two's Complement)** mantığını simüle etmek adına önce sayının mutlak değeri 16-bite tamamlanmakta, ardından tüm bitler mantıksal olarak terslenip (**NOT işlemi**) elde edilen sonuca ikilik tabanda matematiksel olarak **1 eklenerek** işaretli sayı temsili oluşturulmaktadır. Sürecin devamında elde edilen 16 karakterlik ikilik dizi, her biri bir **"nibble"ı (4-bit)** temsil eden dört gruba ayrılarak bir sözlük yapısı üzerinden **onaltılık (hexadecimal)** karşılıklarına haritalanmakta ve son aşamada bu veri, sekizer bitlik iki ayrı **"Byte" hücresi** olarak gruplandırılıp ASCII karakterleriyle şematize edilerek verinin bellekteki fiziksel hücre dizilimi ve saklanma mantığı kullanıcıya görsel bir çıktı olarak sunulmaktadır.
