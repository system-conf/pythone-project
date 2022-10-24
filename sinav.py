from pickle import UNICODE


a="selam"
print("\a sad")


# Kaçış Dizileri
# Kaçış dizileri, Python’da özel anlam taşıyan işaret veya karakterleri, sahip oldukları bu özel
# anlam dışında bir amaçla kullanmamızı sağlayan birtakım araçlardır.

# \' - Karakter dizisi içinde tek tırnak işaritini kullanabilmemizi sağlar.. 
# \" - Karakter dizisi içinde tırnak işaritini kullanabilmemizi sağlar.. 
# \\ - Karakter dizisi içinde \ işaritini kullanabilmemizi sağlar..
# \n - Yeni bir satıra geçmemizi sağlar önemli !!..
# \t - Karakterler arasında boşluk bırakmak için kullanılır..
# \u - UNICODE kod konumlarını gösterebilmenizi sağlar..
# \U - UNICODE kod konumlarını gösterebilmenizi sağlar..
# \N - Karakterleri UNICODE adlarına göre kullanabilmemizi sağlar..
# \x - Onaltılık sistemdeki bir sayının karakter karşılığını gösterebilmemizi sağlar..
# \a - Destekleyen sistemlerde, kasa hoparlöründen bir "bip" sesi verilmesini sağlar..
# \r - Aynı satırın başına dönülmesini sağlar..
# \v - Destekleyen cihazlarda düşey sekme oluşmasını sağlar..
# \b - İmlecin sola doğra kaydırılmasını sağlar.. 
# \f - yeni bir sayfaya geçilmesini sağlar..
# r - Karakter dizisi içinde kaçış dizileri kullanabilmemizi sağlar... 


#*************************************************************************************************

# x**y - x sayısının y üssünün alınması..
# pow(x,y) - x sayısının y üssünün alınması..

# abs(x) - x sayısının mutlak değeri...
# divmod(x,y) - x sayısının y sayısına bölümünden elde edilen tam kısım ve kalanın ikili demet olarak elde edilmesi..
# pow(x,y,z) - pow(x,y)%z değeri..
# round(x,n) - x sayısının n basamağa yuvarlanması..
# bin(i) - On tabanında ki i sayısının binary yani iki tabanındaki hali (Bu değer string olarak geri döner)..
# hex(i) - On tabanında ki i sayısının hexadecimal yani onaltılık tabandaki hali (Bu değer string olarak geri döner)...
# int(x) - x nesnesinin tamsayıya çevrilmiş hali (yuvarlama yapmaz)..
# int(s,taban)  - String biçimdeki s değerini tamsayıya çevirir. Taban değeri 2ile 26 arasında belirtilmelidir aksi halde hata verir.
# oct(i) - On tabanında ki i sayısının octal yani sekizlik tabana çevirir (Bu değer string olarak geri döner)..
# str(i) - Sayının string hale dönüşmesini sağlar..


# Boolean İfadeler:

# Mantıksal değerler olarak da karşınıza çıkar. 2 değer alır bunlar True ve False’dir. True doğru
# değer ifade eder ve geri 1 değeri döndürür. False ise yanlış değer ifade eder ve geri 0 değeri
# döndürür. Bool ifadeler mantıksal değerlendirmeler yapılırken kullanılır.

# Karakter Dizileri:

# String veri tipidir. Bir veya daha fazla karakterden oluşurlar. Gösterilirken tırnak içinde
# kullanılırlar. Bir dizi gibi düşünülebilirler. Fakat dizilerde istenildiğinde s[i]=’k’ şeklinde s
# dizisinin i. elemanını k yap şeklinde değiştirilebilirler. Python buna izin vermez. Çünkü string
# ifadeler değiştirilemez yapılardır. String ifadeler Unicode karakterler içerebilir. Onları
# dilimleyebilir veya birleştirebiliriz, fakat bu dizilerin elemanlarını değiştiremezsiniz. Karakter
# dizilerinde toplama veya çarpma gibi aritmetik işlemler yapabilirsiniz. Örneğin

# s=”abc”
# k=”123”
# l=s+k => “abc123”
# m=s*3 => “abcabcabc” elde edilir.


# Listeler:
# Listeler farklı tür elemanları saklayan birimlerdir. Listeler köşeli parantezler arasında aralarına
# virgül konarak oluşturulurlar.
# liste = [] Boş liste
# liste = [1,2,3]
# Listeler değiştirilebilir özellikledir. Stringler gibi değildir. Farklı tip elemanlar aynı liste
# içerisinde saklanabilir.
# liste =[1,”fatih”,(“abc”,5)]


# Demetler:
# Demetlerde stringler gibi elemanları değiştirilemez yapılardır. Genellikle parantez içinde
# yazılırlar. İndisleri sıfırdan başlar. Elemanları dilimlenebilir, iç içe yazılabilir fakat kesinlikle
# değiştirilemez. Elemanları birbirinden virgül ile ayrılır. Farklı tip verileri saklayabilir.
# demet=(123,”a”,[“x”,”y”],(1,2,3),4) şeklinde tanımlanabilir.
# demet[0]=321 hata verecektir. Çünkü doğrudan değiştirilemezler. Ekleme yapılabilir.
# demet1=demet2 + demet3[0]
# işlemi demet1’e demet2 ye demet3’ün 0 indisli elemanını ekler ve atamayı yapar. 


# url = "w"*3 
# print( url +"."+ "safirvadi.com")


yas = int(input("Yaşınız: "))

print("Adın" , int(yas + yas) , "yaşındasın vayy")
type(yas)


