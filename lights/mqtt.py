import paho.mqtt.client as mqtt
from . import utils


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        mqtt_client.subscribe("lights")
    else:
        print("Bad connection. Code:", rc)


def on_message(mqtt_client, userdata, msg):
    print(f"Received message on topic: {msg.topic} with payload: {msg.payload}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
broker = utils.read_json("broker.json")
user = broker["user"]
password = broker["password"]
server = broker["server"]
port = broker["port"]
keepAlive = broker["keepAlive"] or 0
client.username_pw_set(user, password)
client.connect(
    host=server, port=port, keepalive=keepAlive
)
