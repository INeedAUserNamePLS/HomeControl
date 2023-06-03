import json
import paho.mqtt.client as mqtt
from . import utils


flag_connected = 0
client = mqtt.Client()
client._connect_timeout = 1.0


def on_connect(mqtt_client, userdata, flags, rc):
    global flag_connected
    if rc == 0:
        print("Connected successfully")
        flag_connected = 1
        client.subscribe("lights")
    else:
        print("Bad connection. Code:", rc)


def on_disconnect(mqtt_client, userdata, rc):
    disconnect()
    print("Disconnected")


def on_message(mqtt_client, userdata, msg):
    print(f"Received message on topic: {msg.topic} with payload: {msg.payload}")


def disconnect():
    global client
    global flag_connected
    flag_connected = 0
    client.loop_stop()
    client.disconnect()


def start():
    global client
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    broker = utils.read_json("broker.json")
    user = broker["user"]
    password = broker["password"]
    server = broker["server"]
    port = broker["port"]
    keepAlive = broker["keepAlive"] or 0
    client.username_pw_set(user, password)
    try:
        if server is not None:
            if port is None:
                client.connect(host=server, keepalive=keepAlive)
            else:
                client.connect(host=server, port=port, keepalive=keepAlive)
    except:
        print("connection failed")
        return None
    mqtt.Client.loop_start(client)
    return client


def send(data):
    global flag_connected
    global client
    if flag_connected == 1:
        mqtt.Client.publish(client, "lights", json.dumps(data))
