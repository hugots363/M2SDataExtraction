import numpy
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from sys import argv


def traza_to_plot(path, dump_path,bench):
    file = open(path,'r')
    reg_size = 90

    int_opcodes = [0,1,2,3,4,5,6,7,8,9,10,11,12,52,53,54,55,56,57,58,59,60,61]
                # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    prod_opcodes_num = [1,2,3,4,5,6,7,8,9,10,11,12,52]
    #[             0,     1,     2,   3,     4,    5,      6,      7,    8,   9,    10,   11,     12,    52,     53,      54,      55,   56,    57,    58,       59,       60,       61    ]
    s_opcodes = ["nop","move","add","sub","mult","div","effaddr","and","or","xor","not","shift","sign","load","store","prefetch","call","ret","jump","branch","ibranch","syscall","opcount"]
    prod_opdcodes = ["move","add","sub","mult","div","effaddr","and","or","xor","shift","sign","load"]

    acum_RR = np.array([int_opcodes,[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes)])
    acum_RC = np.array([int_opcodes,[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes)])
    temp_RR = [-1]*len(int_opcodes)
    temp_RC = [-1]*len(int_opcodes)



    def opcode_to_pos(op):
        cont = 0
        for num in int_opcodes:
            if(num == op):
                return cont
            cont = cont + 1
        print("FALLO EN FUNC")

    def is_producer(op):
        for num in prod_opcodes_num:
            if(op == num):
                return 1
        return 0
    #print(is_producer(0))
    #L1W, L2RR, L3RC
    while True:

        next_line = file.readline()
        if not next_line:
            break
        #print(next_line.strip())
        str = next_line.split()
        #print(str)
        if(str[0] != "CC" and str[0] != "0"):
            if(int(str[0]) !=  0):
                bars = 0
                opcode = 0
                lim  = len(str)
                for x in range(0,lim):
                    if str[0] != "|" :
                        if bars == 0:
                          opcode = str[0]
                          op_pos = opcode_to_pos(int(opcode))
                        elif bars == 1:
                            check = list(str[0])
                            if check[1] == "R":
                                reg = str[0].replace("RR","")
                                if temp_RR[op_pos] != -1:
                                    temp_RR[op_pos] = temp_RR[op_pos] +1
                            else:
                                reg = str[0].replace("RC", "")
                                if temp_RC[op_pos] != -1:
                                    temp_RC[op_pos] = temp_RC[op_pos] +1
                        else:
                            if str is not None:
                                if temp_RR[op_pos] >= 3:
                                    acum_RR[4][op_pos] = acum_RR[4][op_pos] +1
                                else:
                                    acum_RR[temp_RR[op_pos]+1][op_pos] = acum_RR[temp_RR[op_pos]+1][op_pos] + 1
                                temp_RR[op_pos] = 0
                                if temp_RC[op_pos] >= 3:
                                    acum_RC[4][op_pos] = acum_RC[4][op_pos] +1
                                else:
                                    if temp_RC[op_pos] != 0:
                                        acum_RC[temp_RC[op_pos]+1][op_pos] = acum_RC[temp_RC[op_pos]+1][op_pos] +1
                                    #if op_pos
                                temp_RC[op_pos] = 0
                    else:
                        bars = bars +1
                    del str[0]


    file.close()
    ##PLOT##
    #print(acum_RC)
    data_to_plot = np.array([int_opcodes,[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),int_opcodes,[0.0]*len(int_opcodes),[0.0] *len(int_opcodes),[0.0]*len(int_opcodes)])
    x = acum_RR[0]
    totales = [0.0]*len(x)
    for index in range(0, len(x)):
        for refs in range(1, 5):
            totales[index] = acum_RR[refs][index] + acum_RC[refs][index] + totales[index]
    data_to_plot = int_opcodes

    for x in range(1, 5):
        for y in range(0, len(int_opcodes) ):
            if(totales[y] != 0 and acum_RC[x][y] != 0):
                acum_RC[x][y] = (acum_RC[x][y]/totales[y])*100.0
            else:
                acum_RC[x][y] = 0
            #print(acum_RC[x][y])
    for x in range(1,5):
        for y in range(0, len(int_opcodes)):
            if(totales[y] != 0 and acum_RR[x][y] != 0):
                acum_RR[x][y] = (acum_RR[x][y]/totales[y])*100.0
            else:
                acum_RR[x][y] = 0
    #print(acum_RC)

    for x in range(1,5):
        #print(acum_RR[x,:])
        data_to_plot = numpy.vstack([data_to_plot, acum_RR[x,:]])
    for x in range(1,5):
        #print(acum_RR[x,:])
        data_to_plot = numpy.vstack([data_to_plot, acum_RC[x,:]])



    print("-------------------------------------------------------------------------------------------")
    #print(data_to_plot)
    #plt.figure(figsize=(7, 7))
    #x = data_to_plot[0]
    x = range(0,23)
    y = range(0,11)
    y = [ element*10 for element in y ]
    width = 0.35
    fig,ax = plt.subplots()
    ax.bar(s_opcodes,data_to_plot[1],width,label="r_0",color = "red")
    ax.bar(s_opcodes,data_to_plot[2],width,label="rr_1",bottom=data_to_plot[1],color = "cyan")
    ax.bar(s_opcodes,data_to_plot[3],width,label="rr_2",bottom=np.array(data_to_plot[1]+ data_to_plot[2]),color="cadetblue")
    ax.bar(s_opcodes,data_to_plot[4],width,label="rr>=3",bottom=np.array(data_to_plot[1]+ data_to_plot[2]+data_to_plot[3]),color="midnightblue")
    ax.bar(s_opcodes,data_to_plot[6],width,label="rc_1",bottom=data_to_plot[1]+ data_to_plot[2]+data_to_plot[3]+data_to_plot[4]+data_to_plot[5],color="chartreuse")
    ax.bar(s_opcodes,data_to_plot[7],width,label="rc_2",bottom=data_to_plot[1]+ data_to_plot[2]+data_to_plot[3]+data_to_plot[4]+data_to_plot[5]+data_to_plot[6],color="limegreen")
    ax.bar(s_opcodes,data_to_plot[8],width,label="rc>=3",bottom=data_to_plot[1]+ data_to_plot[2]+data_to_plot[3]+data_to_plot[4]+data_to_plot[5]+data_to_plot[6]+data_to_plot[7],color="darkgreen")
    ax.legend(ncol=4,bbox_to_anchor =(0.5, 1.25),loc="center")

    plt.title(bench)
    plt.xticks(rotation=90)
    plt.grid()
    plt.tight_layout()
    plt.yticks(y)


    #plt.show()
    print(dump_path+bench)
    ss = dump_path+bench
    plt.savefig(ss)
    plt.close()

def list_benchs(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    res = []
    for elem in files:
        if '.out' in elem:
            res.append( elem.replace('.out',''))
    return res


#####PROGRAM MAIN#####
#traza_to_plot("/home/hutarsan/Documentos/racetrack/racetrack/hangar/aux", "/home/hutarsan/Documentos/racetrack/racetrack/hangar/","prueba")

benchs = list_benchs(argv[1])
for bench in benchs:
    path = argv[1]+bench+".out"
    print(path)
    res = argv[2]
    print(res)
    traza_to_plot(path,res,bench)

#traza_to_plot(argv[1], argv[2], "test")
#print(list_benchs("/home/hutarsan/Documentos/racetrack/hangar/prueba"))
