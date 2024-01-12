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
        {1 : {"A" : {"B" : 2 , "C" : 2}, ...},
         2 : {"AB" : {"C" : 2 , "D", 1}, ...}
        }
        
        """
        self.trajectory = trajectory
        self.sourceObservations = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
        self.lenOftraj = len(trajectory)


    def buildFirstOrderObservations(self):
        order = 1
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

    def buildObservationsOfSource(self, newSource , order):
        ## below code is for testing
        if len(newSource) != order:
            raise ValueError("Order and source length does not match")
        ###############################
        paths = paths = defaultdict(lambda : defaultdict(int))
        for index in range(self.lenOftraj-order):
            path = tuple(self.trajectory[index:index+order+1])
            source = path[:-1]
            if source in newSource:
                target = path[-1]
                paths[source][target] += 1
        self.sourceObservations[order] = paths


            
    def printObservationOfOrder(self , order , raw = False):
        printDataOfOrder( data=self.sourceObservations, order=order ,raw=raw)


if __name__ == "__main__":
    trajectory = "ACDBCEACDBCE"
    x = ObservationsPlus(trajectory=trajectory)
    x.buildFirstOrderObservations()
    x.buildObservationsOfSource({("A", "C") , ("B", "C") }, 2)
    x.printObservationOfOrder(1)
    x.printObservationOfOrder(2)
    