import createDics as cd
import pandas as pd
from sys import argv
import matplotlib.pyplot as plt
import numpy as np






if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV> <Ciclo max penalizacion>\n")
    exit()

def percentByEpoch(res):
    # res.to_csv(argv[2], sep= ",",index=False )
    r1 = res["1ref"].to_numpy()
    r2 = res["2ref"].to_numpy()
    r3 = res["3ref"].to_numpy()
    r4 = res["4ref"].to_numpy()
    r5 = res["5ref"].to_numpy()
    labels = []
    for num in range(0, 1000):
        labels.append(num)
    # Getting ploted data
    iteraciones = len(res)/1000
    iteraciones = int(iteraciones)
    for x in range (0,iteraciones):
    # labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        print("Dibujando grafica " + str(x))
        ref1 = r1[x*1000:x*1000+1000]
        ref2 = r2[x*1000:x*1000+1000]
        ref3 = r3[x*1000:x*1000+1000]
        ref4 = r4[x*1000:x*1000+1000]
        ref5 = r5[x*1000:x*1000+1000]
        benchmark = res.iat[x*1000,0]
        width = 1  # the width of the bars: can also be len(x) sequence
        #print(r1)
        fig, ax = plt.subplots()
        ax.bar(labels, ref1, width, label='1 reference')
        ax.bar(labels, ref2, width, label='2 references')
        ax.bar(labels, ref3, width, label='3 references')
        ax.bar(labels, ref4, width, label='4 references')
        ax.bar(labels, ref5, width, label='5or+ references')

        ax.set_ylabel('Registers')
        ax.set_xlabel('Time (in epochs)')
        ax.set_title('Reference by register divided in epochs(' + benchmark + ")")
        ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), ncol=3, fancybox=True, shadow=True)
        ax.margins(x=0)
        plt.grid()
        plt.tight_layout()
        figura = plt.gcf()
        figura.savefig(argv[2] + benchmark)
        plt.close('all')
        #plt.show()


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
#print(res)
percentByEpoch(res)


#print(res)
