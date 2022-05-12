import createDics as cd
import pandas as pd
from sys import argv

if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV>\n")
    exit()

dic = dict()
benchs = cd.create_dic_nt(argv[1])
print(argv[1])
aux1 = []
aux2 = []

for benchmark,arc_name in benchs.items():
    #print(benchmark)
    #rint("\n")
    total = 0
    for arc_n,df in arc_name.items():

        #total += sum(df["pid100-disp-stall-uopq"])
        total += sum(df["pid100-disp-stall-rob-smt"])
        total += sum(df["pid100-disp-stall-rob-mem"])
        total += sum(df["pid100-disp-stall-rob"])
        #total += sum(df["pid100-disp-stall-iq"])
        #total += sum(df["pid100-disp-stall-lq"])
        #total += sum(df["pid100-disp-stall-sq"])
        #total += sum(df["pid100-disp-stall-pq"])
        #total += sum(df["pid100-disp-stall-rename"])
        #total += sum(df["pid100-disp-stall-ctx"])
        #print(benchmark + "inst-> " + str(inst))
        aux1.append(benchmark)
        aux2.append((sum(df["pid100-disp-stall-rob"])/total)*100)

dic["Benchmark"] = aux1
dic["%_stall_rob"] = aux2



dff = pd.DataFrame(dic)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )