from time import time
from honPlus.Distributions import DistributionPlus
from honPlus.Observations import ObservationsPlus
start = time()
with open(r'trajectory/sample_data50.csv' , 'r') as trajectories:
    data = trajectories.readline().strip("\n").strip()
   
    while data:
        shipid_trajectory = data.split(" ")

        # for space separated values.
        shipId = shipid_trajectory[0:1]
        trajectory = shipid_trajectory[1:]
        observations = ObservationsPlus(trajectory=trajectory)
        dst = DistributionPlus(observations=observations, minSupport=1)
        dst.buildDistribution()
        
        data = trajectories.readline().strip("\n").strip()
            # removing objects to free up space in ram
        del observations
        del dst
        
        
ObservationsPlus.getConsolidatedObj().buildDistribution()
# ObservationsPlus.getConsolidatedObj().printOverAllObservations()
# ObservationsPlus.getConsolidatedObj().printDistributions()
ObservationsPlus.getConsolidatedObj().writeOverAllObservations()
ObservationsPlus.getConsolidatedObj().writeDistributions()
end = time()
print( "total time in minutes " , round((end - start)/60,2))


