import os.path
import TrafficNodes as tNodes
import WeatherNodes as wNodes
import StationNodes as sNodes
import Edges as edge
import FormatSave as fSave

if __name__ == '__main__':
    print('loading traffic nodes..')
    trafficNodes = tNodes.loadTrafficNodes(
        os.path.dirname(os.path.abspath(__file__)) + '\\input\\Blokkades2017_situatieberichten.csv')

    print('loading weather nodes..')
    weatherNodes = wNodes.loadWeatherNodes(
        os.path.dirname(os.path.abspath(__file__)) + '\\input\\KNMI_hourly_stripped.txt')

    print('loading station nodes..')
    stationNodes = sNodes.loadStationNodes(os.path.dirname(os.path.abspath(__file__)) + '\\input\\KNMI_stations.txt')

    print('starting edge creation procedure..')
    edges = edge.create_edges(trafficNodes, weatherNodes, stationNodes)

    print('number of stationIncidentEdges: ' + str(len(edges[0])))
    print('number of chainIncidentEdges: ' + str(len(edges[1])))
    print('number of weatherIncidentEdges: ' + str(len(edges[2])))

    fSave.formatSave([stationNodes, trafficNodes, weatherNodes], 'nodes')
    fSave.formatSave(edges, 'edges')

    # tNodes.saveTrafficNodes(trafficNodes)
    # wNodes.saveWeatherNodes(weatherNodes)
    # sNodes.saveStationNodes(stationNodes)

    print("Done")
