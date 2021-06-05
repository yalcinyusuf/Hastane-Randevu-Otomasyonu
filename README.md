Hastane-Randevu-Otomasyonu
Bu hastanede 2 poliklinik ve 4 doktor vardır. Her poliklinikte 2 doktor şeklinde hasta tedavi etmektedir.

Projeyi yaparken MSSQL Server veri tabanı ile Python dili kullanıldı.Veri tabanının arayüzünü görselleştirmek için arayüz olarak PyQt5 kütüphanesi kullanıldı.Arayüzleri dizayn etmek için Qt Designer adlı programdan yararlanıldı.

Otomasyon kodu yazılırken hem Windows hem de MacOS işletim sisteminde çalışması sağlanmıştır.Veri tabanı bağlantısı için MacOS için pymssql kullanırken,Windows işletimli bilgisayar için pyodbc kütüphanesi kullanıldı.

Giriş Ekranı:
image

Ana Sayfa:
image

Yazdır:
SQL’den çekilen verileri FPDF kütüphanesini kullanarak, pdf dosyasına aktarır. Pdf dosyasında yeni randevu almış hastaların bilgileri bulunmaktadır.

image

Randevu Al:
Hasta TC numarasını ve poliklinik bilgisini girerek uygun doktorlardan randevu alacaktır. Randevu aralıkları 15 dk şeklindedir. Yani hasta 9:00 , 9:15, 9:30, 9:45 … şeklindeki slotlardan randevu alabilir. Bir hasta ilgili doktor için belirli bir saatte randevu aldıysa o doktorun o tarih ve saatteki durumu meşgul olduğundan başka bir hasta randevu alamayacaktır.TC kimlik 11 haneden küçük olamaz.İsim ve soyisim sadece harflerden oluşur.

image

Hasta randevu aldığında şu şekilde e-posta adresine mail gelecektir :

image

Randevu İptal Et:
Hasta TC numarası,randevu tarihi ve saatini girerek randevusunu iptal edebilecektir.

image

İstatistik Menüsü:
Her bir doktorun muayene ettiği hasta bilgileri, vb istatiksel bilgilere erişilmektedir.Bu verilere ulaşırken diğerlerinde olduğu gibi sql sorgularıyla sağlanmıştır.

image