from honPlus.Distributions import DistributionPlus
from honPlus.Observations import ObservationsPlus
with open(r'trajectory\trajectoryPath.txt' , 'r') as trajectories:
    data = trajectories.readline().strip("\n")
    while data:
        shipid , trajectory = data.split(" ")
        observations = ObservationsPlus(trajectory=trajectory)
        dst = DistributionPlus(observations=observations, minSupport=1)
        dst.buildFirstOrderDistribution()
        dst.printDistributionOfOrder(order=1)
        dst.getNewsource()
        data = trajectories.readline()
        print("-"*50)

