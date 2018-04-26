# Wildlife-Detector-Internet-Of-Things
### Use of IOT in Wildlife Research.

## Objective: 
   The aim of the project is to collect wildlife animal data using IOT devices and use it for research to monitor migration pattern of various wildlife species and their habitat etc.

## Hardware Requirements:
  1. Raspberry pi 3
	1. Motion Sensor
	1. Camera Sensor
	1. Temperature Sensor
	1. LCD Display

## Software Technologies:
	1. HTML5 and CSS
	1. MYSQL DB
	1. Python 3, Django

## Description:
	* Basically, Wildlife animals can be detected by using motion sensor attached to Raspberry pi. Once motion is detected camera attached to raspberry pi will take picture of the animal and send this picture to image recognition API. 
	* Image recognition API will analyze this image and give output in the form of JSON data from which animal information can be extracted. Also, it will note date, time and weather conditions when animal is detected.
	* All this data will be stored in MYSQL database for the analysis and research. Application will have front end using HTML5, CSS which will show history of all animals captured using camera.

## References:
* Image Recognition:  https://visual-recognition-demo.mybluemix.net/



