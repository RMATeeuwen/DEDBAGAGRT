import TrafficNodes as tNodes

if __name__ == '__main__':
    trafficNodes = tNodes.loadTrafficNodes(
        "C:\\Users\\Daan\\OneDrive\\Master\\Data Engineering\\Data sets\\Final\\Blokkades2017_situatieberichten.csv")

    # for node in trafficNodes:
    #    print(node.interval)

    tNodes.saveTrafficNodes(trafficNodes)
