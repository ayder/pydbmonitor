##Dagitik Veritabani Monitoru ##

### dbcount_cron.py ###
- Istenilen sürelerde çalışarak dbconfig.ini icinde belirtilmis sunucularda tüm veritabanlarından tablo durumlarını alır ve lokal veritabanına kaydeder


###Web Arayüzü tornado_server.py##
- [Sayfasının](http://dbmonitor.host:8888/)  kullanıcı odaklı son rapor
bilgilerini goruntuler olmasını sağlanır. 
- Angularjs ile veri kaynağında olan değişiklik sayfanızdaki görünüme, görünümde olan değişiklik de,herhangi bir atama işlemleri olmadan veriye uygulanır.
- Artık **controller** içerisinde arayüz nesnelerini kullanmadan işlerimizi gerçekleştirabiliyoruz.Ayrıca html içerisindeki elementleri hiyerarşik controller yapısıyla yönetebiliyorsunuz. Hangi elementlerin görünür, hangi elementlerin hangi koşullarda render edilecek olmasını, hangilerinin belirttiğiniz case lerde var olmasını küçücük attiribute ler ile ayarlayabiliyorsunuz.. (ng-app="gemStore" , ng-controller="StoreController")
- Html taglarıyla yazılmış ve veritabanından alınmış bilgileri sayfadaki alan türlerinine göre sıralayabiliyorsunuz.
- Projedeki verileri **db.py** veritanından alıyorsunuz.
- Veritabanına bağlantı bilgileri ise **dbconfig.ini** dosyasından kolayca ulaşabiliyorsunuz.
    
 
örnek dbmonitor.ini dosyası:

```config
[server]  

; Kayitlarin saklanacagi lokal veritabani sunucusu
[server]
host=localhost
db=dbmon
user=dbmonuser
passwd=dbmonpaswd

; Databases to monitor
; format:
; name=host,user,pass 
[monitor]
cbgone=10.10.10.55,dbmonuser,dbpasswd
cbtwo=10.10.10.56,dbmonuser,dbpasswd
foydb=10.10.10.231,dbmonuser,dbpasswd
pdfajans=10.10.10.54,dbmonuser,dbpasswd
ht-db=10.10.10.193,dbmonuser,dbpasswd
```

 
### Python2.7 ve Gereksinimler###
> - Jinja2==2.7.3  
> - MySQL-python==1.2.5  
> - tornado==3.2.2

###Bunun dışında hakkını yememek lazım##
> Angularjs 
> Tornado  
> Json  
> python  
> html5/bootstrapt  
> MySql  




