import copy


def Sort(freq, nsize, node):
    data = copy.copy(freq)
    for i in range(0, nsize):
        for j in range(i-1, -1, -1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                node[j], node[j + 1] = node[j+1], node[j]
            else:
                break

