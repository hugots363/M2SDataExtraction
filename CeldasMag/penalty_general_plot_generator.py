import createDics
import sys as sys
import os as os
import createDics as cd
import percent_penalty_cycles as ppc
import matplotlib.pyplot as plt
import sys
import penalty_cycles as pc

if len(sys.argv) < 3:
    print("Usage: <Script> <ReportsDir> <File where save plots>", end="\n")
    exit()

fig = plt.figure()
dic = dict()
benchs = cd.create_dic_mod(sys.argv[1])
plot = 1
contador = 0

#Checking paths
if not (os.path.exists(sys.argv[2]+"percentages")):
    os.mkdir(sys.argv[2]+"percentages")

if not (os.path.exists(sys.argv[2]+"totales")):
    os.mkdir(sys.argv[2]+"totales")

print("Generando plots %")
for benchmark,arc_name in benchs.items():
    path = sys.argv[1]+str(benchmark)+"/"
    dir = sys.argv[2]+"percentages/"+benchmark+".png"
    #print(path)
    busq = path+ "interval_reports/mod/"
    dirContents = os.listdir(busq)
    print(busq)
    if  len(dirContents) != 0 :
        fig = ppc.gen_percent_plot(path)
        fig.savefig(dir)


    else:
        contador = contador + 1
print(str(contador) + " simulaciones no han sido impresas")
contador = 0

print("Generando plots de penalizacion")
for benchmark,arc_name in benchs.items():
    path = sys.argv[1]+str(benchmark)+"/"
    dir = sys.argv[2]+"totales/"+benchmark+".png"
    #print(path)
    busq = path+ "interval_reports/mod/"
    dirContents = os.listdir(busq)
    print(busq)
    if  len(dirContents) != 0 :
        fig = pc.gen_penalty_plots(path)
        plt.tight_layout()
        fig.savefig(dir)
    else:
        contador = contador+1

print(str(contador) + " simulaciones no han sido impresas")




