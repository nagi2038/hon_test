from collections import defaultdict
from honPlus.Observations import ObservationsPlus
from utils.printFormater import printDataOfOrder

class DistributionPlus:
    def __init__(self ,observations : ObservationsPlus , minSupport : int) -> None:
        self.observations = observations
        self.minSupport = minSupport
        self.distributions = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
        # self.extednedSource = defaultdict(lambda : defaultdict(set))
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

    def buildDistribution(self, newIndex = None ):
        """
        calculate the distribution of all orders
        """
        
        if self.order == 1:
            # build first order observations
            self.observations.buildFirstOrderObservations()
        elif newIndex :
            # build observations from order 2
            self.observations.buildObservationsOfIndex(listIndexs=newIndex, order=self.order)


        extendedIndexing = []
        # access given order observations and generate it distributions
        for source in self.observations.sourceObservations[self.order].keys():


            ###################################################################################
            
            # tot_visits = self.filterOutMinSupport(  source = source )

            # # to calcuate distribution of each target
            # for target , count in self.observations.sourceObservations[self.order][source].items():

            #     # make sure that index cache does not affect the minsupport
            #     if target == "index":
            #         continue
                
            #     self.distributions[self.order][source][target] = count / tot_visits if tot_visits else 1

            #################################################################################################

            
            # since, all index are unique if we compare first and last if they are different their exits to targets
            if self.observations.sourceObservations[self.order][source]["index"][0] != self.observations.sourceObservations[self.order][source]["index"][-1]:
                extendedIndexing.append(self.observations.sourceObservations[self.order][source]["index"])
        
        # they are extendedIndexing present we call same function again with passing new Index
                
        # self.printDistributionOfOrder(self.order, raw=False)
        if extendedIndexing:
            self.order += 1
            self.buildDistribution(newIndex=extendedIndexing)

                



    def filterOutMinSupport(self, source) -> int:

        # calculate the "sum of visit for the source" and validate "min support"
        tot_visits = 0
        for target, count in self.observations.sourceObservations[self.order][source].items():
            # make sure that index cache does not affect the minsupport
            if target == "index":
                continue
            tot_visits += count

            # if visits are less than min support it will be set to zero
            if count < self.minSupport:
                self.observations.sourceObservations[self.order][source][target] = 0

        # returns sum of total vist for given source       
        return tot_visits 



    # def buildFirstOrderDistribution(self ):
    #     order  = 1
    #     """
    #     if observation of specific order is not present 
    #     it will generate the observations
        
    #     """
    #     # build first order observations
    #     self.observations.buildFirstOrderObservations()

    #     # access {order val} order observations and generate it distributions
    #     for source in self.observations.sourceObservations[order].keys():
    #         for target , count in self.observations.sourceObservations[order][source].items():

    #             # make sure that index cache does not affect the minsupport
    #             if target == "index":
    #                 continue
    #             if count < self.minSupport:
    #                 self.observations.sourceObservations[order][source][target] = 0
    #         for target , count in self.observations.sourceObservations[order][source].items():
    #             if target == "index":
    #                 continue
    #             temp_souce = self.observations.sourceObservations[order][source]
    #             sum_temp_source = 0
    #             for targetx, count in temp_souce.items():
    #                 if targetx == "index":
    #                     continue
    #                 sum_temp_source += count
    #             self.distributions[order][source][target] = temp_souce[target] / sum_temp_source if sum_temp_source else 1.0
    
    





    # def buildDistributionOfSource(self, newSource , order):
    #     """
    #     this function will build observatoins and distributions of specific newSource 
    #     """
    #     self.observations.buildObservationsOfSource(newSource=newSource, order=order)
    #     for source in self.observations.sourceObservations[order].keys():
    #         for target , count in self.observations.sourceObservations[order][source].items():
    #             if target == "index":
    #                 continue
    #             if count < self.minSupport :
    #                 self.observations.sourceObservations[order][source][target] = 0
    #         for target, count in self.observations.sourceObservations[order][source].items():
    #             if target == "index":
    #                 continue
    #             temp_souce = self.observations.sourceObservations[order][source]
    #             sum_temp_source = 0
    #             for target, count in temp_souce.items():
    #                 if target == "index":
    #                     continue
    #                 sum_temp_source += count
    #             self.distributions[order][source][target] = temp_souce[target] / sum_temp_source if sum_temp_source else 1.0
    #     # self.buildextendSource(newSource=newSource , order=order)
    #         # self.chekNewOrder(sources=self.distributions , currentOrder=order)


          
    # def chekNewOrder(self):
    #     # filters out all source and destination value with higher order
    #     newSourcedist = set()
    #     for source in self.distributions[self.order]:
    #         for target , distributionVal in self.distributions[self.order][source].items():
    #             if distributionVal < 1:
    #                 newSourcedist.add(source + (target,) )
    #     return newSourcedist

    # def getNewsource(self):
    #     # get all the values with distribution less than 1
    #     sourcetarget = self.chekNewOrder()
    #     if sourcetarget:
    #         # get all new source with previous source
    #         newSource = self.observations.getNewObservationsource(sourcetarget=sourcetarget, currentOrder=self.order)
    #         self.order += 1
    #         # build distribution for next order.
    #         if newSource:
    #             self.buildDistributionOfSource(newSource=newSource, order=self.order)
    #             self.printDistributionOfOrder(self.order)
    #             self.getNewsource()
    #         else:
    #             return
    #     else:
    #         return


    # def printDistributionOfOrder(self , order , raw = False):
    #     self.observations.printObservationOfOrder(order=order , raw=raw)
    #     # printDataOfOrder(data=self.distributions , order=order , raw=raw)
    

if __name__ == "__main__":
    trajectory = 'ACDBCEACDBCE'
    observations = ObservationsPlus(trajectory=trajectory)
    dst = DistributionPlus(observations=observations, minSupport=1)
    dst.buildFirstOrderDistribution()
    dst.printDistributionOfOrder(order=1)
    dst.getNewsource()

    

