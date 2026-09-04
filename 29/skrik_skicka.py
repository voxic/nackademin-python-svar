import paho.mqtt.publish as publish

namn = input("Namn: ")
while True:
    text = input("Meddelande: ")
    if text == "":
        break
    publish.single(
        "nackademin/shout",
        payload=f"{namn}: {text}",
        hostname="mqtt.progress42.com",
        port=1883,
    )
