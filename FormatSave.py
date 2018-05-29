import os.path


def formatSave(nodeList: list, name: str):
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\output\\' + name + '.csv', 'w')

    for list in nodeList:
        for node in list:
            file.write(node.format() + '\n')

    file.close()
