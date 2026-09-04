def medel(temperaturer):
    return sum(temperaturer) / len(temperaturer)


temps = []
for _ in range(3):
    temps.append(int(input("Temperatur: ")))

m = medel(temps)
print(m)
if m < 18:
    print("För kallt")
elif m > 24:
    print("För varmt")
else:
    print("Lagom")
