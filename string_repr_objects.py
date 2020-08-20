

class Car:
# Takes in 2 arguments speed units and returns:
# "Car with the maximum speed of {speed} {units}"
    def __init__(self, speed, unit):
        # take in speed and units
        self.speed = speed
        self.unit = unit
    def __str__(self):
        answer = "Car with the maximum speed of {} {}"
        return answer.format(self.speed, self.unit)

class Boat:
# Takes in 2 arguments speed units and returns:
# "Boat with the maximum speed of {speed} units"
    def __init__(self,speed):
        # take in speed
        self.speed = speed

    def __str__(self):
        answer = "Boat with the maximum speed of {} knots"
        return answer.format(self.speed)