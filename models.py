class NearEarthObject:
    def __init__(self, pdes, name='unknown', diameter=float('nan'), hazardous=True):
        self.pdes = pdes
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous
        self.approaches = []
    def add_approach(self,approach):
        self.approaches.append(approach)


    def __str__(self):
        return '{name} has a pdes of {pdes} and a diameter of {diameter} and hazardous = {hazardous}'.format(name=self.name
                                                                                                    ,pdes=self.pdes
                                                                                                    ,diameter = self.diameter
                                                                                                    ,hazardous = self.hazardous)

class CloseApproach:
    def __init__(self,neo_pdes, time, distance, velocity):
        self.neo = neo_pdes
        self.time = time
        self.distance = distance
        self.velocity = velocity
        self.data = {
            'neo_pdes':neo_pdes
            ,'time':time
            ,'distance':distance
            ,'velocity':velocity
        }

    def __str__(self):
        return '{neo} passed by Eart at {time}, traveling at {velocity} and at {distance} away'.format(neo=self.neo
                                                                                                       ,time=self.time
                                                                                                       ,distance=self.distance
                                                                                                       ,velocity=self.velocity)
