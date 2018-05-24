import os.path
import TrafficNodes as tNodes
import WeatherNodes as wNodes

if __name__ == '__main__':
    trafficNodes = tNodes.loadTrafficNodes(
        os.path.dirname(os.path.abspath(__file__)) + '\\Blokkades2017_situatieberichten.csv')

    weatherNodes = wNodes.loadWeatherNodes(os.path.dirname(os.path.abspath(__file__)) + '\\KNMI_hourly_stripped.txt')

    tNodes.saveTrafficNodes(trafficNodes)
    wNodes.saveWeatherNodes(weatherNodes)

    print("Done")
