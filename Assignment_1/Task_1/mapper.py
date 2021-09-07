#!/usr/bin/env python
import sys
import json
from datetime import datetime

def isNotNan(data):
    if data["Description"] == "NaN" or data["Severity"].isNaN or data["Sunrise_Sunset"].isNaN or data["Visibility(mi)"].isNaN or data["Precipitation(in)"].isNaN or data["Weather_Condition"].isNaN:
        return False
    return True

def filterBasedOnConstraints(data):
    #{"ID": "A-1655975", "Severity": 3, "Start_Time": "2017-02-07 13:32:33", "End_Time": "2017-02-07 14:17:05", "Start_Lat": 42.385605, "Start_Lng": -83.15898100000001, "End_Lat": NaN, "End_Lng": NaN, "Distance(mi)": 0.01, "Description": "Left and left center lane blocked and left hand shoulder blocked due to accident on I-96 Eastbound at Exits 186A 186B Wyoming St.", "Number": NaN, "Street": "Wyoming St", "Side": "R", "Country": "US", "Timezone": "US/Eastern", "Airport_Code": "KDET", "Weather_Timestamp": "2017-02-07 13:38:00", "Temperature(F)": 36.0, "Wind_Chill(F)": 29.6, "Humidity(%)": 100.0, "Pressure(in)": 29.37, "Visibility(mi)": 3.0, "Wind_Direction": "ESE", "Wind_Speed(mph)": 8.1, "Precipitation(in)": 0.06, "Weather_Condition": "Light Rain", "Amenity": false, "Bump": false, "Crossing": false, "Give_Way": false, "Junction": false, "No_Exit": false, "Railway": false, "Roundabout": false, "Station": false, "Stop": false, "Traffic_Calming": false, "Traffic_Signal": false, "Turning_Loop": false, "Sunrise_Sunset": "Day", "Civil_Twilight": "Day", "Nautical_Twilight": "Day", "Astronomical_Twilight": "Day"}
    if "lane blocked" in data["Description"] or "shoulder blocked" in data["Description"] or "overturned vehicle" in data["Description"]:
        if data["Severity"] >=2:
            if data["Sunrise_Sunset"] == "Night":
                if data["Visibility(mi)"]<=10.0:
                    if data["Precipitation(in)"]>=0.2:
                        if data["Weather_Condition"] == "Heavy Snow" or  data["Weather_Condition"] == "Thunderstorm" or data["Weather_Condition"] ==  "Heavy Rain" or data["Weather_Condition"] ==  "Heavy Rain Showers" or data["Weather_Condition"] == "Blowing Dust":
                            return True
                else:
                    print(type(data["Visibility(mi)"]))
    return False

for line in sys.stdin:
    line=line.strip()
    data = json.loads(line)
    if(isNotNan(data)):
        if(filterBasedOnConstraints(data)):
            #2017-02-07 13:32:33.354
            hour=str(data["Start_Time"])[11:13]
            """try:
                dateTimeObject=datetime.strptime(str(data["Start_Time"]).strip(),"%Y-%m-%d %H:%M:%S.%f")
            except ValueError:
                print(data["Start_Time"])
                dateTimeObject=datetime.strptime(str(data["Start_Time"]).strip(),"%Y-%m-%d %H:%M:%S")
            
            #hour=datetime.strftime(dateTimeObject,"%H")
            hour=time.strftime(dateTimeObject,"%H")
            #hour=data["Start_Time"].hour"""
            #print(hour,"\t1")