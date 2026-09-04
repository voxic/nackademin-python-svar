try:
    tal = int(input("Heltal: "))
except ValueError:
    print("Kunde inte läsa talet.")
else:
    print(tal * 10)
