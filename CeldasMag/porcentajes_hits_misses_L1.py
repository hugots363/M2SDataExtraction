import createDics as cd
import pandas as pd
from sys import argv

if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV>\n")
    exit()



dic = dict()
accesos_L1= 0
accesos_totales=0


benchs = cd.create_dic_mod(argv[1])
aux1= []
aux2= []
aux3= []
aux4= []
aux5=[]
aux6=[]


for benchmark,arc_name in benchs.items():
    for arc_n,df in arc_name.items():
        #MRU_hits_totales.append(MRU_hits)
        accesos_L1 = sum(df["dl1-0-hits-int"]) + sum(df["dl1-0-misses-int"])
        aciertos_L1 = sum(df["dl1-0-hits-int"])
        fallos_L1 = sum(df["dl1-0-misses-int"])
        lrow = len(df.index) - 1


        aux1.append(benchmark)
        aux2.append(accesos_L1)
        aux3.append(aciertos_L1)
        aux4.append(fallos_L1)
        aux5.append((aciertos_L1/accesos_L1)*100)
        aux6.append((fallos_L1/accesos_L1)*100)



dic[" Benchmarks"] = aux1
dic["Accesos L1-d"] = aux2
dic["Aciertos L1-d"] = aux3
dic[" Fallos L1-d"] = aux4
dic["Porcentaje aciertos L1-d"] = aux5
dic["Porcentaje fallos L1-d"] = aux6

dff = pd.DataFrame(dic)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )