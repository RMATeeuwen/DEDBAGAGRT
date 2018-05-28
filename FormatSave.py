import os.path


def formatSave(nodeList: list):
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\output\\nodes.csv', 'w')

    for list in nodeList:
        for node in list:
            file.write(node.format() + '\n')

    file.close()
