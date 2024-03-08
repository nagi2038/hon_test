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
        self.order = 1


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

    def buildObservationsOfIndex(self, listIndexs : list[list]  ):
        paths  = defaultdict(lambda : defaultdict(int))
        for indexs in listIndexs:
            for index in indexs:
                # checking index are going out of bound
                if index-self.order + 1 >= 0 and index+1 < self.lenOftraj:
                    source=tuple(self.trajectory[index-self.order + 1 : index + 1])
                    target=self.trajectory[index + 1]
                    paths[source][target] += 1

                    ObservationsPlus.consolidate.OverAllObservations[self.order][source][target] += 1

                    if paths.get(source).get("index"):
                        paths[source]["index"].append(index)
                    else:
                        # creating index key if not present for the source
                        paths[source]["index"] = [index]
        self.sourceObservations[self.order] = paths


    def extendObservations(self, newIndex = None ):
        """
        calculate the distribution of all orders
        """
        if self.order == 1:
            # build first order observations
            self.buildFirstOrderObservations()
        elif newIndex :
            # build observations from order 2
            self.buildObservationsOfIndex(listIndexs=newIndex)
        extendedIndexing = []
        # access given order observations and generate it distributions
        for source in self.sourceObservations[self.order].keys():
            
            # since, all index are unique if we compare first and last if they are different their exits to targets
            if self.sourceObservations[self.order][source]["index"][0] != self.sourceObservations[self.order][source]["index"][-1]:
                extendedIndexing.append(self.sourceObservations[self.order][source]["index"])
        
        # they are extendedIndexing present we call same function again with passing new Index
                
        # self.printDistributionOfOrder(self.order, raw=False)
        if extendedIndexing:
            self.order += 1
            self.extendObservations(newIndex=extendedIndexing)

    @staticmethod
    def getConsolidatedObj() -> Consolidate:
        return ObservationsPlus.consolidate


if __name__ == "__main__":
    trajectory = "ACDBCEACDBCE"
    x = ObservationsPlus(trajectory=trajectory)
    x.extendObservations()
    