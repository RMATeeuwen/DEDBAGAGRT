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

    def __str__(self):
        return str(self.id) + ', ' + str(self.stationId) + ', ' + str(self.interval.startDate) + ', ' + str(
            self.interval.startTime) + ', ' + str(self.interval.endDate) + ', ' + str(
            self.interval.endTime) + ', ' + str(self.windVelocity) + ', ' + str(self.maxVelocity) + ', ' + str(
            self.precipitation) + ', ' + str(self.sight) + ', ' + str(self.fog) + ', ' + str(self.rain) + ', ' + str(
            self.snow) + ', ' + str(self.thunder) + ', ' + str(self.ice)


def loadWeatherNodes(fileName):
    reader = csv.reader(open(fileName))

    weatherNodes = []
    id = 0;

    for row in reader:

        for i in range(3, 13):
            if row[i] == '     ':
                row[i] = -1

        weatherNodes.append(
            WeatherNode(id, row[0], Interval.hourly(row[1], row[2]), row[3], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11],
                        row[12]))

        id += 1

    return (weatherNodes)

def saveWeatherNodes(nodes):
    header = ['id', 'station id', 'start date', 'start time', 'end date', 'end time', 'wind velocity', 'max velocity',
              'precipitation in 0.1 ml', 'horizontal sight', 'fog', 'rain', 'snow', 'thunder', 'ice']
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\weatherNodes.csv', 'w')

    file.write(', '.join(header))

    for node in nodes:
        file.write('\n' + str(node))

    file.close()
