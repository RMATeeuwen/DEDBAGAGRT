from math import sin, cos, sqrt, atan2, radians

MAXDISTANCE = 5  # choose parameter


class WeatherIncidentEdge:
    def __init__(self, ID, weatherID, trafficID, location, interval):
        self.edgeID = ID
        self.weatherID = weatherID
        self.trafficID = trafficID
        self.location = location
        self.interval = interval

    def format(self) -> str:
        return str(self.edgeID) + ', ' + str(self.weatherID) + ', ' + str(self.trafficID) + \
               ', Edge Label, WeatherDuringIncident, location, ' \
               + str(self.location) + ', interval, ' + str(self.interval)


class ChainIncidentEdge:
    def __init__(self, ID, trafficID, othertrafficID, location, otherlocation, interval):
        self.edgeID = ID
        self.trafficID = trafficID
        self.othertrafficID = othertrafficID
        self.location = location
        self.otherlocation = otherlocation
        self.interval = interval

    def format(self) -> str:
        return str(self.edgeID) + ', ' + str(self.trafficID) + ', ' + str(self.othertrafficID) + \
               ', Edge Label, ChainIncident, location, ' + str(self.location) + ', otherlocation, ' \
               + str(self.otherlocation) + ', interval, ' + str(self.interval)


class StationIncidentEdge:
    def __init__(self, ID, stationID, trafficID, location, interval):
        self.edgeID = ID
        self.stationID = stationID
        self.trafficID = trafficID
        self.location = location
        self.interval = interval

    def format(self) -> str:
        return str(self.edgeID) + ', ' + str(self.stationID) + ', ' + str(self.trafficID) + \
               ', Edge Label, ClosestStation, location, ' + str(self.location) + ', interval, ' + str(self.interval)


def distance(node1, node2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(node1.lat())
    lon1 = radians(node1.lon())
    lat2 = radians(node2.lat())
    lon2 = radians(node2.lon())

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def time_overlap(node1, node2):
    return node1.interval.overlap(node2.interval)


def outer_interval(node1, node2):
    return node1.interval.outer_interval(node2.interval)


def create_edges(trafficNodesList: list, weatherNodesList: list, stationNodesList: list):
    stationIncidentEdgesList = []
    chainIncidentEdgesList = []
    weatherIncidentEdgesList = []

    chainId = 0
    closestId = 0
    weatherId = 0

    startIndex = 0

    length = trafficNodesList.__len__() - 2

    for i in range(0, length):
        traffic = trafficNodesList[i]

        for j in range(i + 1, length + 1):
            otherTraffic = trafficNodesList[j]

            if traffic.ID != otherTraffic.ID and distance(traffic, otherTraffic) < MAXDISTANCE and time_overlap(traffic,
                                                                                                                otherTraffic):
                chainIncidentEdgesList.append(
                    ChainIncidentEdge(chainId, traffic.ID(), otherTraffic.ID(), traffic.location, otherTraffic.location,
                                      outer_interval(traffic, otherTraffic)))
                chainId += 1

        closest = -1

        for station in stationNodesList:
            if closest == -1 or distance(traffic, station) < distance(traffic, closest):
                closest = station

        stationIncidentEdgesList.append(
            StationIncidentEdge(closestId, closest.ID(), traffic.ID(), traffic.location, traffic.interval))

        closestId += 1

        for i in range(0, stationNodesList.__len__() - 1):
            if stationNodesList[i] == closest.ID():
                startIndex = i * 8760;

        for i in range(startIndex, startIndex + 8759):
            weather = weatherNodesList[i]

            if time_overlap(traffic, weather):
                weatherIncidentEdgesList.append(
                    WeatherIncidentEdge(weatherId, weather.ID(), traffic.ID(), traffic.location, weather.interval))

                weatherId += 1;
                break
    return [stationIncidentEdgesList, chainIncidentEdgesList, weatherIncidentEdgesList]

# for weather in weatherNodesList:
#     if weather.stationID() != closest.ID():
#         continue
#
#     if time_overlap(traffic, weather):
#         weatherIncidentEdgesList.append(
#             WeatherIncidentEdge(weatherId, weather.ID(), traffic.ID(), traffic.location, weather.interval))
#
#         weatherId += 1
#
#         break