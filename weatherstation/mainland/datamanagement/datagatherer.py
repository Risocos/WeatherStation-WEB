from .weatherstation_v1_pb2 import Measurement
import random

class DataGatherer:

    def __init__(self):
        pass

    def readdata(self):
        measurement_list = []
        chart_list = []
        # for datefolder in datefolders:
        #     for stationfolder in datefolder:
        #         for hourfile in stationfolder:

        for i in range(21):
            measurement = Measurement()
            measurement.temperature = random.randint(0,40)
            measurement_list.append(measurement.temperature)


        for measurements in measurement_list:
            chart_list.append(measurements)

        return [chart_list]


