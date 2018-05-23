import TrafficNodes as csv

if __name__ == '__main__':
    trafficNodes = csv.loadTrafficNodes(
        "C:\\Users\\Daan\\OneDrive\\Master\\Data Engineering\\Data sets\\BlokkadeTest3_904_1079\\dataset.csv")

    # for node in trafficNodes:
    #    print(node.interval)

    csv.saveTrafficNodes(trafficNodes)
