import TrafficNodes as tNodes
import WeatherNodes as wNodes

if __name__ == '__main__':
     #trafficNodes = tNodes.loadTrafficNodes(
     #   "C:\\Users\\Daan\\OneDrive\\Master\\Data Engineering\\Data sets\\Final\\Blokkades2017_situatieberichten.csv")

    # tNodes.saveTrafficNodes(trafficNodes)

    weatherNodes = wNodes.loadWeatherNodes(
        "C:\\Users\\Daan\\OneDrive\\Master\\Data Engineering\\Data sets\\Final\\KNMI_hourly_stripped.txt")

    for node in weatherNodes:
        print(node)