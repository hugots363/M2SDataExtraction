import createDics as cd
import pandas as pd
from sys import argv
import matplotlib.pyplot as plt
import numpy as np





if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV> <Ciclo max penalizacion>\n")
    exit()

def intTimes(res):
    headerMax = "int_maxt_cons_r"
    headerMin = "int_mint_cons_r"
    headerAvg = "int_avgt_cons_r"
    regT = argv[3]
    maxTimes = []
    minTimes = []
    avgTimes = []
    print(regT)

    for x in range(0, 29):
        bench = res.iloc[x]["Benchmark"]
        maxTimes = []
        minTimes = []
        avgTimes = []
        for y in range (0,int(regT)):
            posMax = headerMax + str(y)
            posMin =  headerMin + str(y)
            posAvg = headerAvg + str(y)
            auxMax = res.iloc[x][posMax]
            auxMin = res.iloc[x][posMin]
            auxAvg = res.iloc[x][posAvg]

            #maxTimes.append(auxMax)
            if (auxMax == 999999999):
                maxTimes.append(0)
            else:
                maxTimes.append(auxMax)
            if(auxMin == 999999999):
                minTimes.append(0)
            else:
                minTimes.append(auxMin)
            avgTimes.append(auxAvg)
            posMax = headerMax
            posMin = headerMin
            posAvg = headerAvg

        print(bench)
        fig, axs = plt.subplots(2)
        axs[0].plot(x, y)
        axs[1].plot(x, y)
        axs[0].bar(np.arange(len(maxTimes)),maxTimes,color="maroon",label='Max time',width=1)
        axs[1].bar(np.arange(len(avgTimes)), avgTimes, color="blue", label='Average time',width=1)
        axs[1].bar(np.arange(len(minTimes)), minTimes, color="purple", label='Min time',width=1)
        #plt.ylim((0, 1500))
        axs[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.4), ncol=1, fancybox=True, shadow=True)
        axs[1].legend(loc="lower center", bbox_to_anchor=(0.5, -0.4), ncol=2, fancybox=True, shadow=True)
        axs[0].margins(x=0)
        axs[1].margins(x=0)
        axs[0].grid()
        axs[1].grid()
        fig.text(0.5, 0.005, "Registers", ha="center", va="center")
        fig.text(0.01, 0.5, "Time (in cycles)", ha="center", va="center", rotation=90)
        fig.tight_layout()

        #axs.ylabel("Time(in cycles)")
        #axs[0].ylabel('Time (in cycles)')
        #axs[1].ylabel('Time (in cycles)')
        #axs[0].xlabel('Registers')
        #axs[1].xlabel('Registers')
        #fig.set_xlabel('common xlabel')
        #axs.set_ylabel('common ylabel')
        #fig.title("Time between register writing("+bench+")")
        #plt.show()
        fig.savefig(argv[4]+bench+".png", bbox_inches = "tight")
        plt.close()
        consumers = []


dic = dict()
benchs = cd.create_dic_agrupado(argv[1])
print(argv[1])
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

#res.to_csv(argv[2], sep= ",",index=False )

df = pd.DataFrame(res["Benchmark"])
titulo = "int_consumers_r"

print("Grafica ciclos entre escrituras")
print(df)
df.to_csv(argv[2], sep= ",",index=False)
#percentByEpoch(res)
intTimes(res)

#print(res)
