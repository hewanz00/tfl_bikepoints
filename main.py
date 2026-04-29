#libraries
import requests
import json
from datetime import datetime


#variables
url = 'https://api.tfl.gov.uk/BikePoint/BikePoints_888'
response = requests.get(url) #reading from web; imports as string(?)
data = response.json() #transforms to json

#the below is for if statement
status_code = data.get("httpStatusCode") #finds value based on key (httpstatuscode)
error_message = data.get("message", "no message given")
file_name = "BikePoints_all_"
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 

#the below is for the loop
num_docks = len(data)


#hint 1 
#print(response.status_code)

#hint 2
#error_message = data.get("message", "no message given")

if response.status_code == 200: 
    print(f"File {file_name} {timestamp} was done!")
    with open("BikePoint_888.json", "w") as file:
        json.dump(data, file)
    

else:
      print(f"Error creating  {file_name} {timestamp}: {status_code} {error_message} " )




