import sys
import paho.mqtt.client as mqtt
import json
import time

# The callback for when the client receives a CONNACK response from the server.
payld = {'version':sys.argv[1],'endpoint':sys.argv[2]}
payld = json.dumps(payld)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ota_done/fertigation")
    client.subscribe("version_result/fertigation")
    client.publish("ota_update/fertigation",payld )
    client.publish("version_request/fertigation", "1")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
count=0
client = mqtt.Client(transport="websockets")
client.on_connect = on_connect
client.on_message = on_message

client.connect("35.202.108.111", 8000, 60)

client.loop_start()
time.sleep(30)
client.loop_stop()


