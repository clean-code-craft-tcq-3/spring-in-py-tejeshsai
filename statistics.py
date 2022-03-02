import math


def calculateStats(numbers):

    if(len(numbers) == 0):
        average = math.nan
        maximum = math.nan
        minimum = math.nan
    else:
        average = sum(numbers)/len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)

    return {
        "avg": average,
        "max": maximum,
        "min": minimum
    }


class EmailAlert():
    def __init__(self):
        self.emailSent = False


class LEDAlert():
    def __init__(self):
        self.ledGlows = False


class StatsAlerter():
    def __init__(self, maxthreshold, alerts):
        self.maxthreshold = maxthreshold
        self.emailAlert = alerts[0]
        self.ledAlert = alerts[1]

    def checkAndAlert(self, numbers):
        computedStats = calculateStats(numbers)
        if(computedStats["max"] > self.maxthreshold):
            self.emailAlert.emailSent = True
            self.ledAlert.ledGlows = True
