import mysql.connector
import datetime

class WildlifeDBHelper:
    def __init__(self, animaldata):
        self.animaldata = animaldata
    
    def insert_animal(self):
        hostname = "172.23.134.94"
        try:
            query = "INSERT INTO WildLifeData(Animalname, Airtemperature, Color, Otherfeatures, DateTimeOfImageCapture, LocationOfAnimal) VALUES(%s,%s,%s,%s,%s,%s)"
            args = (self.animaldata.AnimalName, self.animaldata.AirTemperature, self.animaldata.Color, self.animaldata.OtherFeatures, self.animaldata.DateTimeOfImageCapture, self.animaldata.LocationOfAnimal)
            conn = mysql.connector.connect(user="root", password="admin123", host=hostname, database="WildlifeDB")
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except mysql.connector.Error as err:
            print "Error %s:" % err.args[0]
            sys.exit(1)
        finally:
            if conn:
                conn.close()
