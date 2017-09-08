import json, requests
from WildLifeModel import *
from I2C_device import *

class Board:
    def __init__(self, addr=0x48, port=1):
        self.device = I2C_device(addr, port)
 
    def temperature(self):
        self.device.write_cmd(0x42)
        self.device.read()
        return self.device.read()

class ParseJson:
        def __init__(self, data_file, imgfilename):
                self.data_file = data_file
                self.imgfilename = imgfilename

        def methodParse(self):
                data = json.loads(self.data_file)

                classifiers = data["images"][0]["classifiers"]
                data = classifiers[0]["classes"]
                classLength = len(classifiers[0]["classes"])

                board = Board()

                AnimalName = ""
                AirTemperature = str(board.temperature()) + "F degree"
                Color = ""
                OtherFeatures = self.imgfilename
                DateTimeOfImageCapture = ""
                
                url = "http://ipinfo.io/json" #to capture camera location
                response = requests.get(url)
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    print("HTTP Error:", e.message)

                w = json.loads(response.text)
                
                LocationOfAnimal = w["region"] + "|" + w["city"] + "|" + w["country"]
 
                count = 0
                while (count < classLength):                
                        
                        if 'type_hierarchy' in data[count]:
                           #print("Classification of Animal: " + data[count]["type_hierarchy"])
                           AnimalName += data[count]["type_hierarchy"]

                        if 'color' in data[count]:
                           #print("Color of Animal: " + data[count]["class"])
                           Color = "/" + data[count]["class"]

                        count = count + 1
                #print(AnimalName)
                #print(Color)
                #print(AirTemperature)
                #print(LocationOfAnimal)
                #print(OtherFeatures)
                animaldata = make_wildlife(AnimalName , AirTemperature, Color, OtherFeatures, LocationOfAnimal)
                return animaldata
