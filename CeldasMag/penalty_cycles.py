import createDics as cd
import pandas as pd
from sys import argv
import numpy as npy
import re
import matplotlib.pyplot as plt

# if len(argv) < 2:
#     print("Usage: <Script> <Benchmark_path>\n")
#     exit()


def gen_penalty_plots(path_to_b):
    benchmark = path_to_b.split("/")
    longitud = len(benchmark)
    benchmark = benchmark[longitud - 2]
    #Var declaration
    cond = True
    i = 0
    via = 0
    ciclos_p = 0
    sets = 0
    num = 0


    vias = re.findall(r"(\d+)vias" ,path_to_b)
    vias = vias[0]
    vias = int(vias)
    total = 0
    names = []

    # for x in range(vias -1):
    #     dx = "Via" + str(x)
    #     names.append(dx)
    #
    # df = pd.DataFrame(names)
    #npy.zeros((n,n))
    #Main
    df = pd.read_csv(path_to_b + "interval_reports/mod/dl1-0.intrep.csv")


    #get number of sets
    max = 0
    for col in  df.columns:
        aux = list(col)
        length = len(aux)

        pens = []
        #print(aux)
        if aux[length - 2 ] == '-' :
            num = aux[length -1 ]

        elif(aux[length - 3 ] == '-')  :
            num = (aux[length-2]) + (aux[length-1])
        else:
            num = (aux[length-3]) + (aux[length-2]) + (aux[length-1])

        if(num.isdigit() ):
            if(int(num) > max):
                 max =  int(num)




    sets = max
    n_vias = dict()

    for i in range (vias):
        #total = 0
        via_e = "Via " + str(i)
        aux = []
        n_vias[via_e] = aux
        for j in range (sets+1):

            dir = "dl1-0-c4t1-via-"+str(i)+ "-ciclos-penalizacion-"+str(j)
            lrow = len(df) -1
            n_vias[via_e].insert(j,df.loc[lrow, dir])
            #total = total + df.loc[lrow, dir]
            #n_vias[via_e].append(df.loc[lrow, dir])


    resultado = pd.DataFrame(n_vias)

    #Ploting
    #data
    aux= int(vias/2)
    fig, axes = plt.subplots(aux,2)
    fig.set_size_inches(14, 12)
    width = 0.7       # the width of the bars: can also be len(x) sequence
    via_p = "via 0"
    indexes = npy.arange(resultado.index.__len__())
    ejex = npy.arange(0,sets+10,10)
    ejey = npy.arange(0,15000000,750000)
    posx_4 = [0,0,1,1]
    posy_4 = [1,0,0,1]
    posx_8 = [0,1,2,3,0,1,2,3]
    posy_8 = [1, 1, 1, 1, 0, 0, 0, 0]
    fig.suptitle(benchmark)













