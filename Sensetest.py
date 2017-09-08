import RPi.GPIO as GPIO
import time
import json
import pprint
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from picamera import PiCamera
from os.path import join, dirname
from ParseJson import *
from WildlifeDBHelper import *
import paho.mqtt.client as mqtt
 
class Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)
 
    def getState(self):
        return GPIO.input(self.pin)
 
    def waitFor(self, event):
        GPIO.wait_for_edge(self.pin, event)

    def on_public(mosq, userdata, mid):
        mosq.disconnect()
 
def main():
    print("Hello")
    count = 0
    sensor = Sensor(22)
    camera = PiCamera()
    camera.start_preview()
    while count < 1:
        sensor.waitFor(GPIO.RISING);
        state = sensor.getState()
        if state == 1:
            print "Sensor is %d" % (sensor.getState())
            time.sleep(3)
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filepath = "/home/pi/Downloads/Project/Images/"
            filename = "image_" + timestamp + ".jpg"
            camera.capture(filepath + filename)
            count +=1
    camera.stop_preview()

    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='81d3e76ab27c6e270571c1ee50cbdcb2448efa2f')
    with open(join(dirname(__file__), filepath + filename), 'rb') as image_file:
        results = visual_recognition.classify(images_file=image_file)
    data = json.dumps(results, indent=2)
    parsejson = ParseJson(data, filename)
    animaldata = parsejson.methodParse()
    print(animaldata.AnimalName)
    objwildlifedbhelper = WildlifeDBHelper(animaldata)
    objwildlifedbhelper.insert_animal()
    client = mqtt.Client()
    client.connect("172.27.246.86")
    f=open("/home/pi/Downloads/Project/Images/" + filename, "rb")
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    client.publish("image",byteArr,0)
    client.loop_forever()
         
if __name__ == "__main__":
    main()
