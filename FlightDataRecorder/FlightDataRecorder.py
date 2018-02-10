import math

class FlightDataRecorder:
    def __init__(self):
        pass

    def getDistance(self, heading, distance):
        x, y = 0, 0
        for (h, d) in zip(heading, distance):
            x += math.cos(h / 180 * math.pi) * d
            y -= math.sin(h / 180 * math.pi) * d

        return math.sqrt(x**2 + y**2)

