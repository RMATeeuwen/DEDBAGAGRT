import os.path
import TrafficNodes as tNodes
import WeatherNodes as wNodes
import StationNodes as sNodes

if __name__ == '__main__':
    #trafficNodes = tNodes.loadTrafficNodes(
    #    os.path.dirname(os.path.abspath(__file__)) + '\\Blokkades2017_situatieberichten.csv')

    #weatherNodes = wNodes.loadWeatherNodes(os.path.dirname(os.path.abspath(__file__)) + '\\KNMI_hourly_stripped.txt')

    stationNodes = sNodes.loadStationNodes(os.path.dirname(os.path.abspath(__file__)) + '\\KNMI_stations.txt')

    #tNodes.saveTrafficNodes(trafficNodes)
    #wNodes.saveWeatherNodes(weatherNodes)
    sNodes.saveStationNodes(stationNodes)

    print("Done")
