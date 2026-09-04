import paho.mqtt.publish as publish

publish.single(
    "nackademin/larare/hello",
    payload="Hej från läraren",
    hostname="mqtt.progress42.com",
    port=1883,
)
print("Skickat.")
