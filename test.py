import json

class List(list):
    def push(self, x):
        self.append(x)

caseStudyFileName = "pos_10492.png.json"

with open('sampleJson/'+caseStudyFileName, "r") as json_file:
    jsonPosDict = json.load(json_file)

isVehicle = False
isLicensePlate = False

VbboxValues = List()
LCbboxValues = List()

vehicleTags = {}
licensePlateTags = {}

if not isVehicle:
    vehicleJsonData = {
        "presence": 0,
        "bbox": []
    }

if not isLicensePlate:
    LicensePlateJsonData = {
        "vehicle": {
            "Type": None,
            "Pose": None, 
            "Model": None,
            "Make": None,
            "Color": None,
        },
        "license_plate": {
            "Difficulty Score": None,
            "Value": None,
            "Occlusion": None
        }
    }

if jsonPosDict["objects"] and jsonPosDict["objects"][0]["classTitle"] == "Vehicle":
    isVehicle = True

    for point in range (0, len(jsonPosDict["objects"][0]["points"]["exterior"])):
        for i in range(0,len(jsonPosDict["objects"][0]["points"]["exterior"][point])): 
            VbboxValues.push(jsonPosDict["objects"][0]["points"]["exterior"][point][i])
    vehicleJsonData = {
        "presence": 1,
        "bbox": VbboxValues
    }

if jsonPosDict["objects"] and jsonPosDict["objects"][1]["classTitle"] == "License Plate":
    isLicensePlate = True

    for point in range (0, len(jsonPosDict["objects"][1]["points"]["exterior"])):
        for i in range(0,len(jsonPosDict["objects"][1]["points"]["exterior"][point])): 
            LCbboxValues.push(jsonPosDict["objects"][1]["points"]["exterior"][point][i])
    LicensePlateJsonData = {
        "presence": 1,
        "bbox": LCbboxValues
    }

if isVehicle:
    for tag in range (0, len(jsonPosDict["objects"][0]["tags"])):
        vehicleTags[jsonPosDict["objects"][0]["tags"][tag]["name"]] = jsonPosDict["objects"][0]["tags"][tag]["value"]
if isLicensePlate:
    for tag in range (0, len(jsonPosDict["objects"][1]["tags"])):
        licensePlateTags[jsonPosDict["objects"][1]["tags"][tag]["name"]] = jsonPosDict["objects"][1]["tags"][tag]["value"]

formattedJsonPosDict = {
    "dataset_name": caseStudyFileName,
    "image_link": "",
    "annotation_type": "image",
    "annotation_objects": {
        "vehicle": vehicleJsonData, 
        "license_plate": LicensePlateJsonData
    },
    "annotation_attributes": {
        "vehicle": vehicleTags, 
        "license_plate": licensePlateTags
    },
}

print(formattedJsonPosDict)