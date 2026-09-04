"""Hjälp vid demo: publicerar temp 21 och 29 till telemetry."""
import json

import paho.mqtt.publish as publish

for temp in (21, 29):
    payload = json.dumps({"temp": temp, "fukt": 40})
    publish.single(
        "nackademin/larare/telemetry",
        payload=payload,
        hostname="mqtt.progress42.com",
        port=1883,
    )
    print("Skickat", payload)
