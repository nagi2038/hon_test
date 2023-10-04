from collections import defaultdict
from observations import BuildObservation
from utils.printFormater import printDataOfOrder

class BuildDistributions:

    def __init__(self , minSupport : int , observations : dict):
        """
        min su
        """
        self.minSupport = minSupport
        self.observation = observations
        self.distribution = defaultdict(lambda : defaultdict( lambda : defaultdict(float)))

    def generateDistribution(self):
        for order in self.observation.keys():
            for source in self.observation[order].keys():
                for target , count in self.observation[order][source].items():
                    if count < self.minSupport:
                        self.observation[order][source][target] = 0
                for target in self.observation[order][source].keys():
                    temp_souce = self.observation[order][source]
                    self.distribution[order][source][target] = temp_souce[target] / sum(temp_souce.values())


    def getDistributionOfOrder(self, order):
        return self.distribution[order]

    def getDistributions(self):
        return self.distribution

    def printDistributionOfOrder(self , order , raw = False):
        printDataOfOrder(data=self.distribution , order=order , raw=raw)

    def printDistributions(self , raw = False):
        for order in self.distribution.keys():
            self.printDistributionOfOrder(order=order , raw=raw)




if __name__ == "__main__":
    maxOrder = 90
    observ = BuildObservation("ACDBCEACDBCE", 90)
    observ.generateSubseqance()
    
    dist = BuildDistributions(1, observ.getObservations())
    dist.generateDistribution()

    for order in range(1,maxOrder+1):
        observ.printObservationOfOrder(order=order , raw=True)
        dist.printDistributionOfOrder(order=order , raw=True)
    # print({i :  dist[i].values() for i in dist.getDistributions()})
    
