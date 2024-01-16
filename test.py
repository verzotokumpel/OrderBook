# Przykładowa klasa reprezentująca strukturę danych
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.price = cena

# Przykładowa tablica z obiektami Produkt
produkty = [
    Produkt("Laptop", 1200),
    Produkt("Smartphone", 800),
    Produkt("Tablet", 500),
    Produkt("Kamera", 600),
]

# Posortuj tablicę obiektów według klucza 'price'
posortowane_produkty = sorted(produkty, key=lambda x: x.price)

# Wydrukuj posortowane obiekty
for produkt in posortowane_produkty:
    print(f"Nazwa: {produkt.nazwa}, Cena: {produkt.price}")
