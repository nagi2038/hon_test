from honPlus.Distributions import DistributionPlus
from honPlus.Observations import ObservationsPlus
with open(r'trajectory\sample_data50.csv' , 'r') as trajectories:
    data = trajectories.readline().strip("\n")
    count = 0
    while data:
        shipid_trajectory = data.split(" ")

        # for space separated values.
        shipId = shipid_trajectory[0:1]
        trajectory = shipid_trajectory[1:]
        observations = ObservationsPlus(trajectory=trajectory)
        dst = DistributionPlus(observations=observations, minSupport=1)
        dst.buildFirstOrderDistribution()
        dst.printDistributionOfOrder(order=1)
        dst.getNewsource()
        data = trajectories.readline()
        print("-"*50)
        # removing objects to free up space in ram
        del observations
        del dst
        count += 1
        if count%20 == 0:
            break

# BUG
# ***** Observations ORDER 3 *****
# 10|19.29 -> 20 : 0
# 10|19.29 -> 19 : 0
# 41|31.30 -> 31 : 2
# 41|31.30 -> 42 : 0
# 30|31.21 -> 31 : 0
# 30|31.21 -> 39 : 0
# 19|29.39 -> 29 : 0


# ***** Distributions ORDER 3 *****
# 10|19.29 -> 19 : 1.0
# 41|31.30 -> 42 : 0.0
# 30|31.21 -> 39 : 1.0
# 19|29.39 -> 29 : 1.0
