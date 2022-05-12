import createDics as cd
import pandas as pd
from sys import argv

if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV>\n")
    exit()



dic = dict()
accesos_L1= 0
LRU_hits=0
accesos_totales=0

porcent_lru= 0
porcent_otros= 0
benchs = cd.create_dic_mod(argv[1])
aux1= []
aux2= []
aux3= []
aux4= []
aux5=[]


for benchmark,arc_name in benchs.items():
    for arc_n,df in arc_name.items():
        #MRU_hits_totales.append(MRU_hits)
        accesos_L1 = sum(df["dl1-0-hits-int"]) + sum(df["dl1-0-misses-int"])
        aciertos_L1 = sum(df["dl1-0-hits-int"])
        lrow = len(df.index) - 1
        aciertos_LRU = df.at[lrow, "dl1-0-c4t1-mru-hits"]
        porcent_otros= (aciertos_L1 - aciertos_LRU) / aciertos_L1
        porcent_lru= aciertos_LRU / aciertos_L1

        aux1.append(benchmark)
        aux2.append(aciertos_L1/accesos_L1)
        aux3.append(aciertos_LRU/accesos_L1)
        aux4.append(porcent_otros)
        aux5.append(porcent_lru)



dic[" Benchmarks"] = aux1
dic["Aciertos L1"] = aux2
dic["Aciertos MRU"] = aux3
dic[" Porcentaje otros aciertos"] = aux4
dic["Porcentaje aciertos MRU"] = aux5

dff = pd.DataFrame(dic)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )