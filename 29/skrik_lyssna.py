import paho.mqtt.subscribe as subscribe


def visa(client, userdata, message):
    print(message.payload.decode())


print("Shout-bussen är öppen.")
subscribe.callback(
    visa,
    "nackademin/shout",
    hostname="mqtt.progress42.com",
    port=1883,
)
