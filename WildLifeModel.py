import datetime

class WildlifeModel(object):
    AnimalName = ""
    AirTemperature = ""
    Color = ""
    OtherFeatures = ""
    DateTimeOfImageCapture = ""
    LocationOfAnimal = ""
 
def make_wildlife(AnimalName , AirTemperature, Color, OtherFeatures, LocationOfAnimal):
    animal = WildlifeModel()
    animal.AnimalName = AnimalName
    animal.AirTemperature = AirTemperature
    animal.Color = Color
    animal.OtherFeatures = OtherFeatures
    animal.DateTimeOfImageCapture = datetime.datetime.now().strftime('%m/%d/%Y %H:%M')
    animal.LocationOfAnimal = LocationOfAnimal
    return animal
