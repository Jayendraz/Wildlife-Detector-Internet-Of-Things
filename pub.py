import paho.mqtt.client as mqtt

def on_public(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client()
client.connect("172.27.246.86")
f=open("/home/pi/Downloads/tiger.jpg", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish("image",byteArr,0)
client.publish("imagename","test.jpg",0)

#client.loop(5)
client.loop_forever()
