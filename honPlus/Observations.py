from collections import defaultdict
from utils.printFormater import printDataOfOrder

class ObservationsPlus:
    def __init__(self, trajectory : str|tuple|list) -> None:

        """
        trajectory may be list , str , tuple
        sourceObservation  : {order : source : target : count}

        Observations are stored in dict(dict(dict)) in below format
        { order : {source : {destination : count }}}

        ##### sample storage for Observations #####

        ```
        {1 : {"A" : {"B" : 2 , "C" : 2}},
         2 : {"AB" : {"C" : 2 , "D", 1}}
        }
        
        """
        self.trajectory = trajectory
        self.sourceObservations = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
        self.lenOftraj = len(trajectory)


    def buildObservations(self, order = 1):
        if order < 1:
            raise ValueError("Order can not be less than 1")
        
        paths = defaultdict(lambda : defaultdict(int))
        # paths = self.sourceObservations[order]
        for index in range(self.lenOftraj-order):
            """
            if length = 10 
            order = 1
            range : 10-1 = 9
            total iterations [0,8] which is 9
            
            order = 2
            range 10-2 = 8
            total iterations [0,7] which is 8
            
            """
            path = tuple(self.trajectory[index:index+order+1])
            source = path[:-1]
            target = path[-1]
            paths[source][target] += 1
        self.sourceObservations[order] = paths
            
    def printObservationOfOrder(self , order , raw = False):
        printDataOfOrder( data=self.sourceObservations, order=order ,raw=raw)


if __name__ == "__main__":
    order = 2
    trajectory = "helllollo"
    x = ObservationsPlus(trajectory=trajectory)
    x.buildObservations(order=order)
    x.printObservationOfOrder(order=order)

    x.buildObservations(1)
    x.printObservationOfOrder(order=1)
    