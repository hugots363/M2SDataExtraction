import createDics as cd
import pandas as pd
from sys import argv

if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV>\n")
    exit()

dic = dict()
benchs = cd.create_dic(argv[1])
aux1 = [] #Benchmarks
aux2 = [] #Hit_ratios_L1
aux3 = []  #hits via LRU sobre accesos
aux4 =[] #Porcentaje aciertos L1
aux5 = [] #Porcentaje de aciertos LRU
accesosL1 = 0
aciertosL1 = 0
hitsLRU = 0
for benchmark,arc_name in benchs.items():
    #print(benchmark)
    #rint("\n")
    for arc_n,df in arc_name.items():
        # print(benchmark)
        # print(df["pid100-l1-misses-int"])
        accesosL1= sum(df["pid100-l1-accesses-int"])
        aciertosL1= sum(df["pid100-l1-hits-int"])
        hitsLRU= sum(df["pid100-l1-lru-hits"])
        aux1.append(benchmark)
        num = (aciertosL1/accesosL1)
        aux2.append(aciertosL1) #Hit ratio sin hit ratio LRU
        #aux3.append(100 - (hitsLRU*100))
        #------------------#
        aux3.append(hitsLRU) #Sobre accesos
        #-------------------
        aux4.append(accesosL1)
        aux5.append(aciertosL1 - hitsLRU)


        #-------------------
        #aux3.append((1 - hitsLRU/aciertosL1)*100)
        #print(misses)
        #print(inst) #bien

dic["Benchmark"] = aux1
dic["Aciertos totales L1"] = aux2
dic["Aciertos totales MRU"] = aux3
#dic["Hit_ratio_LRU_sobre_aciertos"] = aux4
dic["Accesos"] = aux4
dic["L1 - MRU"] = aux5

dff = pd.DataFrame(dic)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )