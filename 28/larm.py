import json

import paho.mqtt.subscribe as subscribe


def hantera(client, userdata, message):
    text = message.payload.decode()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        print("Kunde inte läsa JSON.")
        return
    temp = data["temp"]
    print(temp)
    if temp > 24:
        print("LARM")


subscribe.callback(
    hantera,
    "nackademin/larare/telemetry",
    hostname="mqtt.progress42.com",
    port=1883,
)
