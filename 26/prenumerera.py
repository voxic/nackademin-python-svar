import paho.mqtt.subscribe as subscribe


def visa(client, userdata, message):
    print(message.payload.decode())


print("Lyssnar. Avbryt med Ctrl+C.")
subscribe.callback(
    visa,
    "nackademin/larare/hello",
    hostname="mqtt.progress42.com",
    port=1883,
)
