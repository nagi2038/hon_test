from collections import defaultdict
from utils.printFormater import printDataOfOrder

class Consolidate:

    minSupport = 1

    OverAllObservations = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
    OverAllDistributinos = defaultdict(lambda : defaultdict(lambda : defaultdict(float)))
    
    @staticmethod
    def printOverAllObservations(raw = True):
        for order in Consolidate.OverAllObservations:
            printDataOfOrder(data= Consolidate.OverAllObservations , order=order , raw=raw)

    @staticmethod
    def printDistributions( raw = True):
        for order in Consolidate.OverAllDistributinos:
            printDataOfOrder(data= Consolidate.OverAllDistributinos , order=order , raw=raw)

        
    @staticmethod
    def buildDistribution():
        for order , sources in  Consolidate.OverAllObservations.items():
                for source in sources:
                    tot_visits = Consolidate.filterOutMinSupport(order=order , source=source)
                    for target , count in Consolidate.OverAllObservations[order][source].items():
                        Consolidate.OverAllDistributinos[order][source][target] =  count/tot_visits if tot_visits else 1


    @staticmethod
    def filterOutMinSupport(order , source) -> int:

        # calculate the "sum of visit for the source" and validate "min support"
        tot_visits = 0
        for target, count in Consolidate.OverAllObservations[order][source].items():
            # make sure that index cache does not affect the minsupport
            if target == "index":
                continue
            tot_visits += count

            # if visits are less than min support it will be set to zero
            if count < Consolidate.minSupport:
                 Consolidate.OverAllObservations[order][source][target] = 0

        # returns sum of total vist for given source       
        return tot_visits 