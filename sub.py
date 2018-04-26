import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    print("Connect with result code " + str(rc))
    client.subscribe("image")
    client.subscribe("imagename")

def on_message(client, userdata, msg):
    f = open('/home/pi/Downloads/MQTT/TestName.jpg', 'w')
    f.write(msg.payload)
    f.close()
    #print(userdata)
    print(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("172.27.246.86")
client.loop_forever()
