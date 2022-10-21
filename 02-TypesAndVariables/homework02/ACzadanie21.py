import random
liczba = random.randint(1, 6)
liczba_gracza = int(input("Zgadnij jaka liczba wypadła na kostce."))
print(liczba == liczba_gracza)