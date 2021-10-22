from random import randint


def roll(data):

    data = data.split("d")

    if len(data) == 1:
        return [data[0]]

    if data[0] == "":
        times = 1
    else:
        times = int(data[0])

    value = int(data[1])

    results = []

    for _ in range(times):

        result = randint(1, value)
        results.append(result)

    return results
