import json
import random


def ny_matning():
    return {
        "temp": random.randint(18, 23),
        "fukt": random.randint(35, 50),
    }


matningar = [ny_matning() for _ in range(5)]

with open("sensor.json", "w", encoding="utf-8") as f:
    json.dump(matningar, f)

hogsta = max(m["temp"] for m in matningar)
print("Sparade", len(matningar), "mätningar.")
print("Högsta temperatur:", hogsta)
