import sys
import json
import urllib
import time
import argparse

GEO_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

def findNearbyPlaces(enteredLoc, filename, radius, apiKey):
    url = PLACES_API_URL + "location=" + enteredLoc +"&radius=" + radius + "&key=" + apiKey
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    hasNextPage = True

    fwrite = open(filename + ".csv", 'w+')
    while data["status"] == "OK" and hasNextPage:
        if "next_page_token" in data:
            print "Next page exists"
            nextPage = data["next_page_token"]
        else:
            print "No more pages"
            hasNextPage = False

        for result in data["results"]:
            try:
                fwrite.write(str(result["name"].encode('utf-8')).replace(",","") + "," + 
                      str(result["vicinity"].encode('utf-8')).replace(",","") + "," + str(result["rating"]).replace(",","") + '\n')
            except KeyError as e:
                continue
    
        time.sleep(2)
    if hasNextPage:        
        url = PLACES_API_URL + "location=" + enteredLoc +"&radius=5000" + "&key=" + apiKey + "&pagetoken=" + str(nextPage.encode('utf-8'))
        print url
        response = urllib.urlopen(url)
        data = json.loads(response.read())

    print data["status"]
    fwrite.close()


def findLatLong(enteredLoc, apiKey):
    url = GEO_API_URL + "address=" + enteredLoc + "&key=" + apiKey
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    
    latitude = data["results"][0]["geometry"]["location"]["lat"]
    longitude = data["results"][0]["geometry"]["location"]["lng"]

    latLong = str(latitude) + "," + str(longitude)

    print latLong

    return latLong

def main():
    parser = argparse.ArgumentParser(description='Google Business Finder')
    parser.add_argument("--api-key", required=True, type=str, help="The API key to use")

    args = parser.parse_args()

    print "Please make a selection!"
    print "1. Search by Suburb/City/Town name (uses Geo API + Places API)"
    print "2. Input Lat/Long (uses Places API)"
    print "0. Exit"
    selection = input()

    latLong = ""

    if(selection == 1):
        print "Enter a suburb/city/location followed by a state!"
        enteredLoc = raw_input()
        print "You entered " + enteredLoc + "!"
        latLong = findLatLong(enteredLoc, args.api_key)
        filename = enteredLoc
    elif(selection == 2):
        print "Enter Latitude:"
        enteredLat = raw_input()
        print "Enter Longitude:"
        enteredLong = raw_input()
        latLong = enteredLat +","+enteredLong
        print "You entered " + latLong
        filename = latLong
    else:
        print "Exiting..."
        sys.exit()

    print "Enter a radius (metres)"
    radius = raw_input()

    findNearbyPlaces(latLong, filename, radius, args.api_key)

if __name__ == "__main__":
    main()
