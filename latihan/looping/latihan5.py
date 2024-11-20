#program membuat persegi dengan simbol bintang,dengan input dari input
# contoh persegi
# *****
# *****
# *****
# *****
# *****
# misal 
sisi =int (input("masukan panjang sisi :"))
#membuat persegi dengan simbol bintang
for i in range (sisi):
    bintang =""
    for j in range(sisi):
        bintang += "*"
    print(bintang)