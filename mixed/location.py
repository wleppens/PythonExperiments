from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="http://biasc.be")
city_country = "Brussels, Belgium"
location = geolocator.geocode(city_country)
print(location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print((devnet_lat, devnet_lon))
