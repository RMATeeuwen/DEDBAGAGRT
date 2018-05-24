#   Code for loading traffic data CSV into designated data-structure

import csv
import os.path
import Location
import Interval


#   class to store all the important attributes associated to a TrafficNode
class TrafficNode:
    def __init__(self, id, type, interval, location, locName):
        self.id = id
        self.type = type
        self.interval = interval
        self.location = location
        self.locName = locName

    def __str__(self):
        return str(self.id) + ', ' + str(self.type) + ', ' + str(self.interval.startDate) + ', ' + \
               str(self.interval.startTime) + ', ' + str(self.interval.endDate) + ', ' + \
               str(self.interval.endTime) + ', ' + str(self.location.lat) + ', ' + \
               str(self.location.lon) + ', ' + str(self.locName)


#   function to extract TrafficNodes from a .csv file and store them in a list
def loadTrafficNodes(fileName):
    reader = csv.reader(open(fileName))

    trafficNodes = []

    for row in reader:
        if (row[0] == "ongeval" or row[0] == 'blokkade') and row[14] == "TRUE":
            #   Important indexes:
            #   situationRecordType         1
            #   situationId                 6
            #   validityOverallStartTime    11
            #   validityOverallEndTime      13
            #   lat lon                     40
            #   alertCLocationName          41

            #   Insert above values into TrafficNode Object

            #   Split the latitude and longitude into two separate variables
            loc = row[40].split(',')[0].split(' ')

            #   Split date and time into two separate variables
            start = row[11].split(' ')
            end = row[13].split(' ')

            #   Add a TrafficNode to the list of trafficNodes
            trafficNodes.append(
                TrafficNode(row[6], row[1], Interval(start[0], start[1], end[0], end[1]), Location(loc[0], loc[1]),
                            row[41]))

    return trafficNodes


def saveTrafficNodes(nodes):
    header = ['id', 'type', 'start date', 'start time', 'end date', 'end time', 'latitude', 'longitude',
              'location name']
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\trafficNodes.csv', 'w')

    file.write(', '.join(header))

    for node in nodes:
        file.write('\n' + str(node))

    file.close()
