import createDics as cd
import pandas as pd
from sys import argv

if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV>\n")
    exit()

dic = dict()
benchs = cd.create_dic(argv[1])
aux1 = []
aux2 = []
aux3=[]
aux4= []


num = 0
for benchmark,arc_name in benchs.items():
    #print(benchmark)
    #rint("\n")
    for arc_n,df in arc_name.items():
        # print(benchmark)
        # print(df["pid100-l1-misses-int"])
        #L1 MISSES
        misses= sum(df["pid100-l1-misses-int"])
        #print(benchmark + " misses-> " + str(misses))
        lrow = len(df.index) -1
        inst = df.at[lrow, "pid100-uinsts"]
        #print(benchmark + "inst-> " + str(inst))
        aux1.append(benchmark)
        aux2.append(misses/(inst/1000))
        #print(benchmark + " MPKI_L1-> " + str(inst))
        #print(misses)
        #print(inst) #bien
        #L2 MISSES
        misses = sum(df["pid100-l2-misses-int"])
        inst = df.at[lrow, "pid100-uinsts"]
        aux3.append(1000 * misses / inst)
        #L3 MISSES
        misses = sum(df["pid100-l3-misses-int"])
        inst = df.at[lrow, "pid100-uinsts"]
        aux4.append(1000 * misses / inst)

dic["Benchmark"] = aux1
dic["mpki_L1"] = aux2
dic["mpki_L2"] = aux3
dic["mpki_L3"] = aux4



dff = pd.DataFrame(dic)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )