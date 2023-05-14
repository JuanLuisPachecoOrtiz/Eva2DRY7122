import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Santiago"
dest = "Ovalle"
key = "dFJtW3YnqMj31kJm2S5oXbsqiykyGQwr"

while True:
   orig = input("Origen: ")
   if orig == "quit" or orig == "q":
        break
   
   dest = input("Destino: ")
   if dest == "quit" or dest == "q":
      break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]

   if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("Directions from " + (orig) + " to " + (dest))
       print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
       print("Kilometers:      " + str((json_data["route"]["distance"])*1.61))
       for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
       print("=============================================")


    






