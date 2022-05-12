import createDics as cd
import pandas as pd
from sys import argv

if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV> <Ciclo max penalizacion>\n")
    exit()

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



print(res)
res.to_csv(argv[2], sep= ",",index=False )


