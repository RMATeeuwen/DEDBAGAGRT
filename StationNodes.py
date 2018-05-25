import csv
import os.path
from Location import *

class StationNode:
    def __init__(self, id, name: str, location: Location):
        self.id = int(id)
        self.name = str(name)
        self.location = location

    def __str__(self):
        return str(self.id) + ', ' + str(self.name) + ', ' + str(self.location)


def loadStationNodes(fileName: str) -> list:
    reader = csv.reader(open(fileName))

    nodes = []

    for row in reader:
        nodes.append(StationNode(row[0], row[4], Location(row[1], row[2])))

    return nodes


def saveStationNodes(nodes: list):
    header = ['id', 'name', 'latitude', 'longitude']
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\stationNodes.csv', 'w')

    file.write(', '.join(header))

    for node in nodes:
        file.write("\n" + str(node))

    file.close()
