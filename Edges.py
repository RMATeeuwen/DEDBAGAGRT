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
        return str(self.edgeID) + ', ' + str(self.weatherID)+ ', ' + str(self.trafficID) + \
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


def create_edges(TrafficNodesList, WeatherNodesList, stationNodesList):
    stationIncidentEdgesList = []
    chainIncidentEdgesList = []
    weatherIncidentEdgesList = []
    ID = 0
    for traffic in TrafficNodesList:
        for othertraffic in TrafficNodesList:
            if distance(traffic, othertraffic) < MAXDISTANCE and time_overlap(traffic, othertraffic):
                chainIncidentEdgesList.append(
                    ChainIncidentEdge(ID, traffic.ID(), othertraffic.ID(), traffic.location, othertraffic.location,
                                      outer_interval(traffic, othertraffic)))
                ID += 1
        for station in stationNodesList:
            closest = -1
            if closest == -1 or distance(traffic, station) < closest:
                closest = station
                break
        stationIncidentEdgesList.append(
            StationIncidentEdge(ID, closest.ID(), traffic.ID(), traffic.location, traffic.interval))
        ID += 1
        print('begin')
        for weather in WeatherNodesList:
            if weather.stationID() == closest.ID() and time_overlap(traffic, weather):
                print("super'vo")
                weatherIncidentEdgesList.append(WeatherIncidentEdge(ID, weather.ID(), traffic.ID(), traffic.location,
                                                                    weather.interval))
                ID += 1
                break
    print('done with making edges')
    return [stationIncidentEdgesList, chainIncidentEdgesList, weatherIncidentEdgesList]
