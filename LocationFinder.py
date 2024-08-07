# Interacting with Google Maps API to find driving time and distance between cities
# User to dynamically input start and end destination

# pip install googlemaps
import googlemaps

# Read API key from external file, without disclosing in Python script
API = open("Google Maps Platform API Key.txt", "r")
APIKey = API.read()

# Pass through API key/ client ID
Maps = googlemaps.Client(key = APIKey)

# User inputs for start and end drive destination
StartDestination = input("Where will you begin your drive?\n")
EndDestination = input("Where will you end your drive?\n")

# Calculate distance through API
Distance = Maps.directions(StartDestination, EndDestination)

# Format API output into relevant variables
KMDistance = (Distance[0]['legs'][0]['distance']['text'])
HrsMinsDuration = (Distance[0]['legs'][0]['duration']['text'])

# Pass results into an easy to read text string
print("Your drive will cover a total distance of " + KMDistance + ", taking a total time of " + HrsMinsDuration + ".")
