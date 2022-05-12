import createDics as cd
import pandas as pd
from sys import argv
import numpy as npy
import re
import matplotlib.pyplot as plt

# if len(argv) < 2:
#     print("Usage: <Script> <Benchmark_path>\n")
#     exit()

def gen_percent_plot(path_to_b):

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


    vias = re.findall(r"(\d+)vias" ,argv[1])
    vias = vias[0]
    vias = int(vias)
    total = 0
    names = []



    #df = pd.DataFrame(argv[1]+"interval_reports/mod/dl1-0.intrep.csv")

    #npy.zeros((n,n))
    #Main
    df = pd.read_csv(path_to_b+"interval_reports/mod/dl1-0.intrep.csv")

    max = 0
    #get number of sets
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
    #figura = plt.figure(figsize=(20,16))
    figura, axes = plt.subplots(aux,2)
    figura.set_size_inches(14,12)
    widthx = 0.7       # the width of the bars: can also be len(x) sequence
    indexes = npy.arange(resultado.index.__len__())
    ejex = npy.arange(0,sets+10,10)
    ejey = npy.arange(0,105,5)
    posx_4 = [0,0,1,1]
    posy_4 = [1,0,0,1]
    posx_8 = [0,1,2,3,0,1,2,3]
    posy_8 = [1, 1, 1, 1, 0, 0, 0, 0]
    figura.suptitle(benchmark)



    for num in range(vias):
        # print(indexes)
        if(vias == 4):
            posx = posx_4[num]
            posy = posy_4[num]
        else:
            posx = posx_8[num]
            posy = posy_8[num]

        ax = axes[posx][posy]
        sumatorio = resultado["Via " + str(num)].sum()
        #print(sumatorio)

        plotear = ((resultado.iloc[:, num])/sumatorio) * 100
        bars = ax.bar(indexes, plotear, width=widthx, axes=ax)
        ax.set_title("Via "+str(num))
        ax.set_ylabel("Probabilidad de acceso")
        #ax.set_xlabel(via_p)

        ax.set_xticks(ejex)

        # --Usual scale--
        ax.set_ylim(0, 100)
        ax.set_yticks(ejey)

        # for i in ax.patches:
        #     height = i.get_height()
        #
        #     if (height > 14500000):
        #         ax.text(i.get_x() + 0.5, i.get_y()+10000000, str(height), fontsize=9, color='dimgrey', rotation=45)
            # if (height > 10000000):
            #     ax.text(i.get_x() + .04, i.get_height() + 12000, \
            #              str(round((i.get_height()), 2)), fontsize=9, color='dimgrey',
            #             rotation=45)
    plt.close("all")
    return figura;

#USE -> Put path to the bench you want to print!
#gen_percent_plot("/home/hutarsan/Documentos/racetrack/reports/baseline_DDR4/4vias/calculix/")








