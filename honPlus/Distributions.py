from collections import defaultdict
from honPlus.Observations import ObservationsPlus
from utils.printFormater import printDataOfOrder

class DistributionPlus:
    def __init__(self ,observations : ObservationsPlus , minSupport : int) -> None:
        self.observations = observations
        self.minSupport = minSupport
        self.distributions = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
        self.extednedSource = defaultdict(lambda : defaultdict(set))

        """
        distributions  : {order : source : target : normalizedvalue}

        distributions are stored in dict(dict(dict)) in below format
        { order : {source : {destination : count }}}

        ##### sample storage for distributions #####

        ```
        {1 : {"A" : {"B" : 0.5 , "C" : 0.5}, ...},
         2 : {"AB" : {"C" : 0.667 , "D", 0.333}, ...}
        }
        
        """

    def buildFirstOrderDistribution(self ):
        order  = 1
        """
        if observation of specific order is not present 
        it will generate the observations
        
        """
        self.observations.buildFirstOrderObservations()
        for source in self.observations.sourceObservations[order].keys():
            for target , count in self.observations.sourceObservations[order][source].items():
                if count < self.minSupport:
                    self.observations[order][source][target] = 0
            for target in self.observations.sourceObservations[order][source].keys():
                temp_souce = self.observations.sourceObservations[order][source]
                self.distributions[order][source][target] = temp_souce[target] / sum(temp_souce.values())

    def buildObservationsOfSource(self, newSource , order):
        """
        this function will build observatoins and distributions of specific newSource 
        """
        self.observations.buildObservationsOfSource(newSource=newSource, order=order)
        for source in self.observations.sourceObservations[order].keys():
            for target , count in self.observations.sourceObservations[order][source].items():
                if count < self.minSupport:
                    self.observations.sourceObservations[order][source][target] = 0
            for target in self.observations.sourceObservations[order][source].keys():
                temp_souce = self.observations.sourceObservations[order][source]
                self.distributions[order][source][target] = temp_souce[target] / sum(temp_souce.values())
        self.buildextendSource(newSource=newSource , order=order)


    def buildextendSource(self , newSource  , order):
        for source in newSource:
            for start in range(1,order):
                curr = source[start:]
                self.extednedSource[curr][order].add(source)

    

    def printDistributionOfOrder(self , order , raw = False):
        self.observations.printObservationOfOrder(order=order , raw=raw)
        printDataOfOrder(data=self.distributions , order=order , raw=raw)
    

if __name__ == "__main__":
    trajectory = 'ACDBCEACDBCE'
    observations = ObservationsPlus(trajectory=trajectory)
    dst = DistributionPlus(observations=observations, minSupport=1)
    dst.buildFirstOrderDistribution()
    dst.buildObservationsOfSource(newSource={("A", "C") , ("B", "C") }, order= 2)
    dst.printDistributionOfOrder(order=1)
    dst.printDistributionOfOrder(order=2)

    

