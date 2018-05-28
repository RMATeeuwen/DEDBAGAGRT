#   Code for loading a weather data CSV into designated data-structure

import csv
import os.path
from Interval import *


class WeatherNode:

    def __init__(self, id, stationId, interval, windVelocity, maxVelocity, precipitation, sight, fog, rain, snow,
                 thunder, ice):
        self.id = int(id)
        self.stationId = int(stationId)
        self.interval = interval
        self.windVelocity = int(windVelocity)
        self.maxVelocity = int(maxVelocity)
        self.precipitation = int(precipitation)
        self.sight = int(sight)
        self.fog = int(fog)
        self.rain = int(rain)
        self.snow = int(snow)
        self.thunder = int(thunder)
        self.ice = int(ice)

    def interval(self):
        return self.interval

    def __str__(self):
        return str(self.id) + ', ' + str(self.stationId) + ', ' + str(self.interval) + ', ' + str(
            self.windVelocity) + ', ' + str(self.maxVelocity) + ', ' + str(self.precipitation) + ', ' + str(
            self.sight) + ', ' + str(self.fog) + ', ' + str(self.rain) + ', ' + str(self.snow) + ', ' + str(
            self.thunder) + ', ' + str(self.ice)

#   function to load WeatherNodes from the KNMI dataset
def loadWeatherNodes(fileName):
    reader = csv.reader(open(fileName))

    #   initialize a list to save the weatherNodes
    weatherNodes = []

    #   keep a counter to give every node a unique id
    id = 0;

    #   loop through every row in the file
    for row in reader:

        #   some of the weatherstations do not have any data on a specific topic (e.g. precipitation)
        #   the loop below makes sure to set all values of attributes of which there is no data to -1
        for i in range(3, 13):
            if row[i] == '     ':
                row[i] = -1

        #   add the node to the list of WeatherNodes
        #   for an explanation of the hourly function see Interval.py
        weatherNodes.append(
            WeatherNode(id, row[0], Interval.hourly(row[1], row[2]), row[3], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11],
                        row[12]))

        #   increment the id after a node has been added
        id += 1

    return (weatherNodes)

#   function to save a list of WeatherNode objects to csv
#   for a further explanation see the saveTrafficNodes function
def saveWeatherNodes(nodes):
    header = ['id', 'station id', 'start date', 'start time', 'end date', 'end time', 'wind velocity', 'max velocity',
              'precipitation in 0.1 ml', 'horizontal sight', 'fog', 'rain', 'snow', 'thunder', 'ice']
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\output\\weatherNodes.csv', 'w')

    file.write(', '.join(header))

    for node in nodes:
        file.write('\n' + str(node))

    file.close()
