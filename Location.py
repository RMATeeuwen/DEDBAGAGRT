#   class to store latitude and longitude values as floats

class Location:
    def __init__(self, lat, lon):
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return '(' + str(self.lat) + ', ' + str(self.lon) + ')'

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
