from collections import defaultdict
from honPlus.Observations import ObservationsPlus
from utils.printFormater import printDataOfOrder

class DistributionPlus:
    def __init__(self ,observations : ObservationsPlus , minSupport : int) -> None:
        self.observations = observations
        self.minSupport = minSupport
        self.distributions = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
        self.extednedSource = defaultdict(lambda : defaultdict(set))
        self.order = 1

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

    def buildDistributionOfSource(self, newSource , order):
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
        # self.buildextendSource(newSource=newSource , order=order)
            # self.chekNewOrder(sources=self.distributions , currentOrder=order)


    def buildextendSource(self , newSource  , order):
        for source in newSource:
            for start in range(1,order):
                curr = source[start:]
                self.extednedSource[curr][order].add(source)
        
    def chekNewOrder(self):
        # filters out all source and destination value with higher order
        newSourcedist = set()
        for source in self.distributions[self.order]:
            for target , distributionVal in self.distributions[self.order][source].items():
                if distributionVal < 1:
                    newSourcedist.add(source + (target,) )
        return newSourcedist

    def getNewsource(self):
        # get all the values with distribution less than 1
        sourcetarget = self.chekNewOrder()
        if sourcetarget:
            # get all new source with previous source
            newSource = self.observations.getNewObservationsource(sourcetarget=sourcetarget, currentOrder=self.order)
            self.order += 1
            # build distribution for next order.
            if newSource:
                self.buildDistributionOfSource(newSource=newSource, order=self.order)
                self.printDistributionOfOrder(self.order)
                self.getNewsource()
            else:
                return
        else:
            return


    def printDistributionOfOrder(self , order , raw = False):
        self.observations.printObservationOfOrder(order=order , raw=raw)
        printDataOfOrder(data=self.distributions , order=order , raw=raw)
    

if __name__ == "__main__":
    trajectory = 'ACDBCEACDBCE'
    

    

