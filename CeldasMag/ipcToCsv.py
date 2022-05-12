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

num = 0
for benchmark,arc_name in benchs.items():
    #print(benchmark)
    #rint("\n")
    for arc_n,df in arc_name.items():
        # print(benchmark)
        # print(df["pid100-l1-misses-int"])
        #L1 MISSES
        #print(benchmark + " misses-> " + str(misses))
        lrow = len(df.index) -1
        cycles = df.iat[lrow, 0]
        #print(benchmark + "inst-> " + str(inst))
        aux1.append(benchmark)
        aux2.append(500000000/cycles)

dic["Benchmark"] = aux1
dic["IPC"] = aux2



dff = pd.DataFrame(dic)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )