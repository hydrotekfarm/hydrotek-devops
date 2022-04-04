import sys
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ota-fertigation-system")
    client.subscribe("version_result")
    client.publish("ota-fertigation-system", sys.argv[1])
    client.publish("version_request", "1")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(transport="websockets")
client.on_connect = on_connect
client.on_message = on_message

client.connect("35.202.108.111", 8000, 60)

client.loop_forever()


