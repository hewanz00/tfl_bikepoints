#libraries
import requests
import json
import os
from datetime import datetime



#variables
url = 'https://api.tfl.gov.uk/BikePoint'
response = requests.get(url) #reading from web; imports as json string
data = response.json() #transforms from json to pyth dic/list


if response.status_code == 200: 
    #creating folder
    if not os.path.exists('bikepoint_data'):
        os.makedirs('bikepoint_data')

    #loops for each bikepoint id
    for dock_id in data:
        id = dock_id.get("id")
        filename = f"bikepoint_data/{id}.json"
        no_docks = len(data)
        with open(filename, "w") as file: #writes (saves) file
            json.dump(dock_id, file) #transforms back to json
    
    print(f"Yay!! {no_docks} files are in the bikepoint_data folder! :)" )
    

else:
    status_code = data.get("httpStatusCode") #finds value based on key (httpstatuscode)
    error_message = data.get("message", "no message given")
    file_name = "BikePoints_all_"
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 
    print(f"Error creating {file_name} {timestamp}: {status_code} {error_message} :( )" )




