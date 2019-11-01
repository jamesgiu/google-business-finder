# google-business-finder
Hacked together Python 2.7 CLI script made eons ago to help a door-to-door salesperson generate a list of businesses to visit.

It takes in a radius and generates a .csv file containing the business's name, address and rating.

Enter a central location either by Latitude/Longitude or by Suburb/Town etc.

Uses Google's Geocode API and Places API.

# Usage
## Google Cloud
* Requires Google Cloud Console API Key (https://console.cloud.google.com/apis/)
* Pass in your api key in the command line as an argument `--api-key`

The maximum amount of businesses returned with a non-business license request is 60.
Keep your radiuses small.

Source: https://developers.google.com/places/web-service/search

## Execution
* Install Python 2.7
* (Linux/Unix-based systems) Run `python2 location.py --api-key=<your_api_key>`
* (Windows) Launch by executing `windows/run.bat <your_api_key>`
