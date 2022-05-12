import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from sys import argv
import math

def opcodes_distribution(path, dump_path,bench):
    file = open(path,'r')
    reg_size = 90
    int_opcodes = [0,1,2,3,4,5,6,7,8,9,10,11,12,52,53,54,55,56,57,58,59,60,61]
    prod_opcodes_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 52]
    s_opcodes = ["nop","move","add","sub","mult","div","effaddr","and","or","xor","not","shift","sign","load","store","prefetch","call","ret","jump","branch","ibranch","syscall","opcount"]
    prod_opdcodes = ["move", "add", "sub", "mult", "div", "effaddr", "and", "or", "xor", "shift", "sign", "load"]
    distribution = [0]*len(s_opcodes)
    ndistribution = []


    def opcode_to_pos(op):
        cont = 0
        for num in int_opcodes:
            if (num == op):
                return cont
            cont = cont + 1
        print("FALLO EN FUNC")

    def is_producer(op):
        for num in prod_opcodes_num:
            if(op == num):
                return 1
        return 0

    def is_producer_n(opn):
        for name in prod_opdcodes:
            if(name == opn):
                return 1
        return 0

    def truncate(number, decimals=0):
        """
        Returns a value truncated to a specific number of decimal places.
        """
        if not isinstance(decimals, int):
            raise TypeError("decimal places must be an integer.")
        elif decimals < 0:
            raise ValueError("decimal places has to be 0 or more.")
        elif decimals == 0:
            return math.trunc(number)
        factor = 10.0 ** decimals
        return math.trunc(number * factor) / factor

    guarda = 0
    while True:
        next_line = file.readline()
        if not next_line:
            break
    # print(next_line.strip())
        linea = next_line.split()
        if (guarda == 1):
            #print(linea[0])
            pos = opcode_to_pos(int(linea[0]))
            distribution[pos] = distribution[pos] +1
        if (linea and linea[0] == "CC"):
            guarda = 1


    total = 0.0
    for num in distribution:
        total = total + num
    print(total)



    percent = [0.0]*len(s_opcodes)
    legend = [""]*len(s_opcodes)
    cont = 0
    total_dict = {}
    for elem in percent:
        total_dict[s_opcodes[cont]] = distribution[cont]
        percent[cont] = truncate( (distribution[cont]/total)*100,2)
        legend[cont] = str(s_opcodes[cont])+ "-" + str(percent[cont])+"%"
        cont = cont +1
    print(legend)

    cont = 0
    cons_dict = {}
    total_cons = 0.0
    for key in total_dict:
        if is_producer_n(key):
            cons_dict[key] = total_dict[key]
            total_cons = total_cons + total_dict[key]

    for num in prod_opcodes_num:
        if(is_producer(num) == 1):
            ndistribution = np.append(ndistribution, distribution[cont])
            #ndistribution[cont] =  distribution[ndist]
            cont = cont +1
    print(ndistribution)

    legend_cons  = []
    cont = 0
    percent_cons = [0.0]*len(prod_opdcodes)
    for key in cons_dict:
        percent_cons[cont] = truncate((cons_dict[key]/total_cons)*100,2)
        legend_cons = np.append(legend_cons,key+ "-" + str(percent_cons[cont])+"%")
        cont = cont+1
    # for elem in percent_cons:
    #     percent_cons[cont] = truncate( (ndistribution[cont]/total_cons)*100,2)
    #     legend_cons = np.append(legend_cons, str(prod_opdcodes[cont])+ "-" + str(percent_cons[cont])+"%")
    #     cont = cont +1
    #     print(cont)
    print(percent_cons)

    fig1, ax1 = plt.subplots()
    #ax1.pie(distribution,shadow=True, startangle=90)
    ax1.pie(percent_cons, shadow=True, startangle=90)
    ax1.axis('equal')
    plt.legend(labels=legend_cons)
    plt.tight_layout()
    plt.title(bench)
    print(dump_path+bench)
    plt.savefig(dump_path+bench,bbox_inches='tight')

def list_benchs(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    res = []
    for elem in files:
        if '.out' in elem:
            res.append( elem.replace('.out',''))
    return res

####MAIN####
benchs = list_benchs(argv[1])
#print(benchs)
for bench in benchs:
    path = argv[1]+bench+".out"
    print(path)
    res = argv[2]
    opcodes_distribution(path,res,bench)
#opcodes_distribution("/home/hutarsan/Documentos/racetrack/racetrack/hangar/prueba/aux.out","/home/hutarsan/Documentos/racetrack/racetrack/hangar/register_usage/", "zeus")
