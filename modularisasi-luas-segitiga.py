"""
Menghitung Segitiga Dengan Fungsi
Dengan Rumus alas * tinggi / 2
"""

print("Menghitung luas segitiga cara sederhana 1")
alas = 10
tinggi = 6
luas = alas * tinggi / 2

print(f'Menghitung luas segitiga dengan alas = {alas} dan tinggi = {tinggi} dengan hasil luasnya yaitu {luas}')

print("\nMenghitung luas segitiga cara sederhana 2")
alas = 20
tinggi = 6
luas = alas * tinggi / 2

print(f'Menghitung luas segitiga dengan alas = {alas} dan tinggi = {tinggi} dengan hasil luasnya yaitu {luas}')

print("\nMenghitung Luas Segitiga dengan perintah fungsi")
def luas_segitiga(alas, tinggi):
    rumus = alas * tinggi / 2
    return rumus

print(f'Hasil dari luas segitiga adalah = {luas_segitiga(10, 6)}')
print(f'Hasil dari luas segitiga adalah = {luas_segitiga(20, 6)}')

