from collections import defaultdict
from honPlus.Distributions import DistributionPlus
from honPlus.Observations import ObservationsPlus
from utils.printFormater import printDataOfOrder

class RuleBuilderPlus:
    def __init__(self , distributions : DistributionPlus):
        """
        NOT REQUIRED
        """
        self.rules = defaultdict(lambda : defaultdict(lambda : defaultdict(tuple)))
        self.distributions = distributions
    

    def buildRules(self, order = 1):
        for source in self.distributions.distributions[order]:
            self.extendrule(source, source, order)



    def generateRules(self):
        self.distributions.buildFirstOrderDistribution()
        self.AddToRules()


    def extendrule(self , orginalSource , updatedSource , order):
        # to get original distribution
        distribution = self.distributions.distributions[order][orginalSource]
        updatedOrder = order + 1
        extednedSource = self.distributions.extednedSource[updatedOrder][updatedOrder]

        

    def kld(self):
        pass

    def kldThreshold(self):
        pass

if __name__ == "__main__":
    trajectory = "ACDBCEACDBCE"
    obser = ObservationsPlus(trajectory=trajectory)
    dist = DistributionPlus(observations=obser, minSupport=1)
    rules = RuleBuilderPlus(distributions=dist)
    rules.buildRules()