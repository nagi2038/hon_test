from collections import defaultdict
from utils.printFormater import printDataOfOrder
from consolidate import Consolidate
class ObservationsPlus:
    consolidate = Consolidate()

    def __init__(self, trajectory : str|tuple|list  ) -> None:

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
        """
            Build first order observations

            if length of trajectory = 10 
            order = 1
            range : 10-1 = 9
            total iterations [0,8] which is 9
            
            order = 2
            range 10-2 = 8
            total iterations [0,7] which is 8
            
        """
        order = 1
        paths = defaultdict(lambda : defaultdict(int))
        # paths = self.sourceObservations[order]
        for index in range(self.lenOftraj-order):
            path = tuple(self.trajectory[index:index+order+1])
            source = path[:-1]
            target = path[-1]
            paths[source][target] += 1

            ObservationsPlus.consolidate.OverAllObservations[order][source][target] += 1

            # index of source start point is added 
            # appending index key if present
            if paths.get(source).get("index"):
                paths[source]["index"].append(index)
            else:
                # creating index key if not present for the source
                paths[source]["index"] = [index]
                
        self.sourceObservations[order] = paths

    def buildObservationsOfIndex(self, listIndexs : list[list] , order : int):
        paths  = defaultdict(lambda : defaultdict(int))
        for indexs in listIndexs:
            for index in indexs:
                # checking index are going out of bound
                if index-order + 1 >= 0 and index+1 < self.lenOftraj:
                    # path = tuple(self.trajectory[index-order + 1 : index + 2])
                    # source = path[:-1]
                    # target = path[-1]
                    source=tuple(self.trajectory[index-order + 1 : index + 1])
                    target=self.trajectory[index + 1]
                    paths[source][target] += 1

                    ObservationsPlus.consolidate.OverAllObservations[order][source][target] += 1

                    if paths.get(source).get("index"):
                        paths[source]["index"].append(index)
                    else:
                        # creating index key if not present for the source
                        paths[source]["index"] = [index]
        self.sourceObservations[order] = paths


    # def buildObservationsOfSource(self, newSource , order):
    #     ## below code is for testing
    #     # if len(newSource) != order:
    #     #     raise ValueError("Order and source length does not match")
    #     ###############################
    #     paths  = defaultdict(lambda : defaultdict(int))
    #     for index in range(self.lenOftraj-order):
    #         path = tuple(self.trajectory[index:index+order+1])
    #         source = path[:-1]
    #         if source in newSource:
    #             target = path[-1]
    #             paths[source][target] += 1
    #     self.sourceObservations[order] = paths

    # def getNewObservationsource(self, sourcetarget : set , currentOrder : int) :
    #     newSource = set()
    #     i = 1
    #     while i < self.lenOftraj-currentOrder:
    #         if tuple(self.trajectory[i:i+currentOrder+1]) in sourcetarget:
    #             newSource.add(tuple(self.trajectory[i-1:i+currentOrder]))
    #         i += 1
    #     return newSource

            
    # def printObservationOfOrder(self , order , raw = False):
    #     printDataOfOrder( data=self.sourceObservations, order=order ,raw=raw)

    @staticmethod
    def getConsolidatedObj() -> Consolidate:
        return ObservationsPlus.consolidate


if __name__ == "__main__":
    trajectory = "ACDBCEACDBCE"
    x = ObservationsPlus(trajectory=trajectory)
    x.buildFirstOrderObservations()
    x.buildObservationsOfSource({("A", "C") , ("B", "C") }, 2)
    x.printObservationOfOrder(1)
    x.printObservationOfOrder(2)

    del x
    ObservationsPlus.consolidate.printOverAllObservations()

    y = ObservationsPlus(trajectory=trajectory)
    y.buildFirstOrderObservations()
    y.buildObservationsOfSource({("A", "C") , ("B", "C") }, 2)
    y.printObservationOfOrder(1)
    y.printObservationOfOrder(2)

    del y 
    ObservationsPlus.consolidate.printOverAllObservations()
    