##################### Boolean #####################

# Boolean veri türleri True veya False değeri alırlar
x, y = True, False

x  # True
y  # False

# and, or ve not mantıksal operatörlerinin sonuçlarıda True veya False değer alır
x and y # False
x or y # True

not x # False
not y # True

not x and y # False
x and not y # True

not x or y # False
x or not y # True

# <,>,<=,>=,== gibi karşılaştırma operatörlerinin sonuçlarıda True veya False değer alır

1 < 2 # True
4 > 6 # False

7 >= 7 # True
9 <= 7 # False

3 == 5 # False


##################### Integer, Float #####################

# Integer, tam sayı değerleri temsil eder.
# Float, ondalıklı sayıları ifade eder.

a, b = 5, 7

a # 5 int
b # 7 int

a + b # 12 int
a - b # -2 int
a * b # 35 int
a / b # 0.714 float
a // b # 0 int
a % b # 5 int
abs(a) # 5 int
int(2.8) # 2 int
float(5) # 5.0 float
a ** b # 78125 int

##################### String #####################

# Python String'leri karakter dizileridir

s1 = 'Merhaba'
s2 = "DÜNYA"
s3 = """Çok satırlı
string veri tanımlamak için 
bu yöntem kullanılır"""

s1  # Merhaba
s2  # Dünya 
s3  # Çok satırlı\n\nstring veri tanımlamak için \n\nbu yöntem kullanılır

# Strinlerin bir dizi olduğunu ifade etmiştik

s1[1] # e
s2[1:5] # ünya
s3[-3:-1] # lı

# Bazı string Methodlarını inceleyelim

s3.split() # ['Çok', 'satırlı', 'string', 'veri', 'tanımlamak', 'için', 'bu', 'yöntem', 'kullanılır']

s1.upper()  # MERHABA

s2.lower()  # dünya

s3.startswith("veri")  # False
s3.startswith("Çok")  # True

s2.endswith("ya") # False

s3.find("veri") # 20 - indis değeri

s1.replace("e","a") # Marhaba

s1.join(["*", "*", "*"])  # '*Merhaba*Merhaba*'

len(s3) #63

s1 in s3 # False
"satırlı" in s3 # True

print("Deneme")