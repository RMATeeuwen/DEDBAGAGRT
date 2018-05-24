import TrafficNodes as tNodes

if __name__ == '__main__':
    trafficNodes = tNodes.loadTrafficNodes(
        "C:\\Users\\Daan\\OneDrive\\Master\\Data Engineering\\Data sets\\BlokkadeTest3_904_1079\\dataset.csv")

    # for node in trafficNodes:
    #    print(node.interval)

    tNodes.saveTrafficNodes(trafficNodes)
