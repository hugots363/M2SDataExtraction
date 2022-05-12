import createDics as cd
import pandas as pd
from sys import argv
from operator import truediv

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


fp = pd.DataFrame()
integ = pd.DataFrame()
integerBenchs = ["perlbench","bzip2","gcc","mcf","gobmk","hmmer","sjeng","libquantum","h264ref","omnetpp","astar","xalancbmk"]
fpBenchs = ["bwaves","gamess","milc","zeusmp","gromacs","cactusADM","leslie3d","namd","dealII","soplex","povray","calculix","GemsFDTD","tonto","lbm","wrf","sphinx3"]
for bench in integerBenchs:
    integ = integ.append(res[res['Benchmark'] == bench], ignore_index=True)
for bench in fpBenchs:
    fp = fp.append(res[res['Benchmark'] == bench], ignore_index=True)
fp = fp.loc[:, fp.columns.intersection(['Benchmark','Ciclos'])]
print(fp)
integ = integ.loc[:, integ.columns.intersection(['Benchmark','Ciclos'])]
print(integ)
inst = 500000000.0
#fp.options.display.float_format = '{:.2f}'.format
for x in range(0,len(fp.index)):
    fp['Ciclos'].iloc[x] = float( inst ) /(float(fp.at[x, 'Ciclos']))
for x in range(0,len(integ.index)):
    integ['Ciclos'].iloc[x] = float( inst ) /(float(integ.at[x, 'Ciclos']))

print(fp)
print(integ)
#fp_ipc = fp_ipc["Benchmark"]
fp.to_csv(argv[2]+"_fp.csv", sep= ",",index=False)
integ.to_csv(argv[2]+"_int.csv", sep= ",",index=False)
#print(res.iloc[0])
#res.to_csv(argv[2], sep= ",",index=False )