import csv
import os.path
from Location import *

class StationNode:
    def __init__(self, id, name: str, location: Location):
        self.id = int(id)
        self.name = str(name)
        self.location = location

    def ID(self):
        return self.ID

    def lon(self):
        return self.location.longitude()

    def lat(self):
        return self.location.latitude()

    def __str__(self):
        return str(self.id) + ', ' + str(self.name) + ', ' + str(self.location)

#   function to load StationNodes from a KNMI dataset
#   it has similar structure to the load functions
#   of the other node types
def loadStationNodes(fileName: str) -> list:
    reader = csv.reader(open(fileName))

    nodes = []

    #   save important attributes to a StationNode object and add it to the list
    #   row[0] = id
    #   row[1] = latitude
    #   row[2] = longitude
    #   row[3] = altitude (not important)
    #   row[4] = station name
    for row in reader:
        nodes.append(StationNode(row[0], row[4], Location(row[1], row[2])))

    return nodes

#   function to save a list of WeatherNode objects to csv
#   for a further explanation see the saveTrafficNodes function
def saveStationNodes(nodes: list):
    header = ['id', 'name', 'latitude', 'longitude']
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\stationNodes.csv', 'w')

    file.write(', '.join(header))

    for node in nodes:
        file.write("\n" + str(node))

    file.close()
