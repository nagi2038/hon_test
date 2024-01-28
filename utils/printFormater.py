import inspect
from os.path import basename

file = open(r"trajectory/output.txt", "w")

def printDataOfOrder(data : dict, order : int, raw = False):
        file = open(r"trajectory/output.txt", "a")
        # to print the file name which is calling this function
        filepath = inspect.stack()[1][0].f_code.co_filename
        filename = basename(filepath)
        
        header = "\n" +"*"*5 + f" {filename[:-3]} ORDER {order} " + "*"*5
        print(header)
        file.write(header)
        file.write("\n")
        # print("\n" +"*"*5 + f" ORDER {order} " + "*"*5)
        if raw:
            for source in data[order].keys():
                for target , count in data[order][source].items():
                    valST = ",".join(source) +  " -> " + "".join(target) , " : ", count
                    file.write(valST)
                    file.write("\n")
                    print(valST)
            print()
            file.write("\n")
            return
        """
        if order = 2
        or
        if variable raw == True
            AC, CD, DB, BC, CE, EA, AC, CD, DB, BC, CE

            A -> C : 2
            C -> D : 2
            D -> B : 2
            B -> C : 2
            C -> E : 2
            E -> A : 1


        if order = 3
            ACD, CDB, DBC, BCE, CEA, EAC, ACD, CDB, DBC, BCE

            #########################FORMAT##########################
            [Preset] | [Previous].[Previous -1] -> [Future] : [value]
            #########################################################

            C|A -> D : 2
            D|C -> B : 2
            B|D -> C : 2
            C|B -> E : 2
            E|C -> A : 1
            A|E -> C : 1
        
        similary for other order too.
        """
        printbuildformat = "{}{} -> {} : {}"
        for source in data[order].keys():
            for target , count in data[order][source].items():
                if source[:-1]:
                    prevsouce =  "|" + ".".join(source[:-1][::-1])
                else:
                    prevsouce = ""
                val = printbuildformat.format(source[-1], prevsouce, target , count)
                print(val)
                file.write(val)
                file.write("\n")
        print()
        file.write("\n")
