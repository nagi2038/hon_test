
def writeToFile(filePath, data , raw = True) :

    with open(filePath, 'w') as file:
        printbuildformat = "{}{} -> {} : {}"
        if raw:
            for order in data.keys():
                # print(order)
                orderHeader = "*"*5 + f" {filePath[:-3]} ORDER {order} " + "*"*5
                file.write(orderHeader+"\n")
                for source in data[order].keys():
                    for target , count in data[order][source].items():
                        vals = ",".join(source) +  " -> " + "".join(target) + " : " + str(count) + "\n"
                        file.write(vals)
        else:
            for order in data.keys():
                # print(order)
                orderHeader =  "*"*5 + f" {filePath[:-3]} ORDER {order} " + "*"*5
                file.write(orderHeader+"\n")
                for source in data[order].keys():
                    for target , count in data[order][source].items():
                        if source[:-1]:
                            prevsouce =  "|" + ".".join(source[:-1][::-1])
                        else:
                            prevsouce = ""
                        val2 = printbuildformat.format(source[-1], prevsouce, target , count)
                        file.write(val2 + '\n')



































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