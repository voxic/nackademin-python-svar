import json
import random

import paho.mqtt.publish as publish


def ny_matning():
    return {
        "temp": random.randint(18, 28),
        "fukt": random.randint(30, 60),
    }


for _ in range(3):
    data = ny_matning()
    payload = json.dumps(data)
    publish.single(
        "nackademin/larare/telemetry",
        payload=payload,
        hostname="mqtt.progress42.com",
        port=1883,
    )
    print(payload)
