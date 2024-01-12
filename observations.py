from collections import defaultdict
from utils.printFormater import printDataOfOrder

class BuildObservation:

    def __init__(self, trajectory : int , maxOrder = 1):
        """
        To build all observation for given sequncial string

        Input format:
        trajectory : string
        maxOrder : int

        Observations are stored in dict(dict(dict)) in below format
        { order : {source : {destination : count }}}

        ##### sample storage for Observations #####

        ```
        {1 : {"A" : {"B" : 2 , "C" : 2}},
         2 : {"AB" : {"C" : 2 , "D", 1}}
        }
        ```

        A -> B : 2
        A -> C : 2
        
        """
        self.trajectory = trajectory
        self.sizeOftrajectory = len(trajectory)
        # to avoid un necessary iterations
        self.maxOrder = maxOrder
        self.observations = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
    
    def generateSubseqance(self):
        """
        Example : 
        Given trajectory => ACDBCEACDBCE
        maxOrder => len(trajectory) - 1
            i.e :  (12) - 1 = 11
        
        if order = 2 
            AC, CD, DB, BC, CE, EA, AC, CD, DB, BC, CE

            #########################
            [SOURCE] -> [DESTINATION]
            #########################

            A -> C
            C -> D
            D -> B
            B -> C
            C -> E
            E -> A


        if order = 3
            ACD, CDB, DBC, BCE, CEA, EAC, ACD, CDB, DBC, BCE

            AC -> D
            CD -> B
            DB -> C
            BC -> E
            CE -> A
            EA -> C
        
        similary for other order too.
        """
        for order in range(1,self.maxOrder+1):
            count = 0
            for start in range(self.sizeOftrajectory - order):
                count += 1
                # print(self.trajectory[start:start+order+1])
                source = self.trajectory[start:start+order]
                target = self.trajectory[start+order]
                self.observations[order][source][target] += 1
            # print(count)

    def printObservationOfOrder(self , order , raw = False):
        if order > self.maxOrder:
            return
        printDataOfOrder( data=self.getObservations(), order=order ,raw=raw)
        
    def printObservations(self, raw = False):
        """
        To print all order observations for given trajectory
        """
        for order in range(1,self.maxOrder+1):
            printDataOfOrder(data=self.observations , order=order , raw=raw)

    def getObservationsOfOrder(self , order : int):
        return self.observations[order]
    
    def getObservations(self):
        return self.observations

if __name__ == "__main__":
    x = BuildObservation("ACDBCEACDBCE", 3)
    x.generateSubseqance()
    # x.printObservationsOfOrder(3)
    x.printObservations(raw=True)
    # x.printObservationOfOrder(3)
    # help(BuildObservation)