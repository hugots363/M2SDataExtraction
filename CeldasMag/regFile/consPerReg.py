import createDics as cd
import pandas as pd
from sys import argv
import matplotlib.pyplot as plt
import numpy as np






if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV> <Ciclo max penalizacion>\n")
    exit()

def intConsumersGraph(res):
    try:
            header = "int_consumers_r"
            regT = argv[3]
            consumers = []
            print(regT)

            for x in range(0,29):
                bench = res.iloc[x]["Benchmark"]
                for y in range (0,int(regT)):
                    pos = header + str(y)
                    aux = res.iloc[x][pos]
                    consumers.append(aux/1000000)
                    pos = ""
                print(bench)
                plt.bar(np.arange(len(consumers)),consumers,color="maroon", width=1)
                #plt.bar()
                plt.margins(x=0)
                #plt.grid()
                plt.tight_layout()
                plt.ylabel('Consumptions (in millions)')
                plt.xlabel('Registers')
                plt.title("Total consumers per each register("+bench+")")
                #plt.ylim((0, 1000))
                #plt.show()
                #print(argv[4]+ "XD")
                plt.savefig(argv[4]+bench+".png", bbox_inches = "tight",width=1)
                plt.close()
                consumers = []
    except:
        print("Faltan  "+ str(29 - len(df)) + " benchmarks")

dic = dict()
benchs = cd.create_dic_agrupado(argv[1])
aux1 = []
aux2 = []
pen_max = int(argv[3])
bench = ""
aux = 0

for benchmark,arc_name in benchs.items():
    for letra in benchmark:
        if(letra != "."):
            bench = bench+letra
        else:
            break

    if aux == 0:
        tops = list(arc_name.columns.values)
        tops.insert(0, "Benchmarks")
        res = arc_name.copy()
        res.insert(0, "Benchmark", bench)
        aux = 1
    else:
        arc_name.insert(0, "Benchmark", bench)
        res = res.append(arc_name)

    aux2.append(bench)
    bench = ""

res.to_csv(argv[2], sep= ",",index=False )
#print(res)

df = pd.DataFrame(res["Benchmark"])
titulo = "int_consumers_r"

print("CSV con los consumidores por registro")
#print(df)
#df.to_csv(argv[2], sep= ",",index=False)

intConsumersGraph(res)

#print(res)
