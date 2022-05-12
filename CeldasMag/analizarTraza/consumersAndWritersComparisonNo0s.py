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
    all_opcodes = ["x86_uinst_nop", "x86_uinst_move","x86_uinst_add","x86_uinst_sub","x86_uinst_mult","x86_uinst_div","x86_uinst_effaddr","x86_uinst_and","x86_uinst_or","x86_uinst_xor","x86_uinst_not","x86_uinst_shift","x86_uinst_sign",
         "x86_uinst_fp_move","x86_uinst_fp_sign", "x86_uinst_fp_round","x86_uinst_fp_add","x86_uinst_fp_sub","x86_uinst_fp_comp","x86_uinst_fp_mult","x86_uinst_fp_div","x86_uinst_fp_exp","x86_uinst_fp_log","x86_uinst_fp_sin",
         "x86_uinst_fp_cos","x86_uinst_fp_sincos","x86_uinst_fp_tan","x86_uinst_fp_atan","x86_uinst_fp_sqrt","x86_uinst_fp_push","x86_uinst_fp_pop","x86_uinst_xmm_and","x86_uinst_xmm_or","x86_uinst_xmm_xor","x86_uinst_xmm_not","x86_uinst_xmm_nand",
         "x86_uinst_xmm_shift","x86_uinst_xmm_sign","x86_uinst_xmm_add","x86_uinst_xmm_sub","x86_uinst_xmm_comp","x86_uinst_xmm_mult","x86_uinst_xmm_div","x86_uinst_xmm_fp_add","x86_uinst_xmm_fp_sub","x86_uinst_xmm_fp_comp",
         "x86_uinst_xmm_fp_mult","x86_uinst_xmm_fp_div","x86_uinst_xmm_fp_sqrt","x86_uinst_xmm_move","x86_uinst_xmm_shuf","x86_uinst_xmm_conv","x86_uinst_load", "x86_uinst_store","x86_uinst_prefetch","x86_uinst_call","x86_uinst_ret",
         "x86_uinst_jump","x86_uinst_branch","x86_uinst_ibranch","x86_uinst_syscall","x86_uinst_opcode_count"]


    #acum_RR = np.array([int_opcodes,[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes)])
    #acum_RC = np.array([int_opcodes,[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes)])
    num_cons_prod = {}
    diff = {}
    opcode_to_op = {}
    cont = 0
    cons_bet_wr = {}
    cons_bet_wc = {}
    temp_r = {}
    temp_c = {}
    totals = {}
    for elem in all_opcodes:
        num_cons_prod[elem] = [-1,-1]
        diff[elem] = False
        opcode_to_op[cont] = elem
        cons_bet_wr[elem] = [0.0,0.0,0.0,0.0]
        cons_bet_wc[elem] = [0.0,0.0 ,0.0,0.0]
        temp_r[elem] = -1
        temp_c[elem] = -1
        cont  = cont +1
    #temp_RC = [-1]*len(int_opcodes)
    print(num_cons_prod)


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
        div= np.array(next_line.split("|"))
        if div[0] != "\n":
            opcode = int(div[0])
            elem = all_opcodes[opcode]
            consumptions = np.array(div[1].split())
            writes = np.array(div[2].split())
            #Check if consumes anything
            #Tratando la parte de la lectura
            if(len(consumptions) != 0 and  temp_r[elem] != -1 ):
                for reg in consumptions:
                    if (reg[0] == "R"):
                        temp_r[elem] = temp_r[elem] +1
                    else:
                         temp_c[elem] = temp_c[elem] + 1
            #Tratando la parte de la escritura
            if(len(writes) != 0 ):
                if(temp_r[elem] > 2):
                    cons_bet_wr[elem][3] = cons_bet_wr[elem][3] +1
                else:
                    cons_bet_wr[elem][temp_r[elem]] = cons_bet_wr[elem][temp_r[elem]] + 1
                if (temp_c[elem] > 2):
                    cons_bet_wc[elem][3] = cons_bet_wc[elem][3] + 1
                else:
                    cons_bet_wc[elem][temp_c[elem]] = cons_bet_wc[elem][temp_c[elem]] + 1
                temp_r[elem] = 0
                temp_c[elem] = 0




    for elem in all_opcodes:

        totals_r = 0
        totals_c = 0
        if cons_bet_wr[elem][0] == 0 and cons_bet_wr[elem][1] == 0 and cons_bet_wr[elem][2] == 0:
            #del cons_bet_wr[elem]
            cons_bet_wr.pop(elem)
        else:
            totals_r =  cons_bet_wr[elem][1] + cons_bet_wr[elem][2] + cons_bet_wr[elem][3]

        if cons_bet_wc[elem][0] == 0 and cons_bet_wc[elem][1] == 0 and cons_bet_wc[elem][2] == 0:
            #del cons_bet_wr[elem]
            cons_bet_wc.pop(elem)
        else:
            totals_c =  cons_bet_wc[elem][1] + cons_bet_wc[elem][2] + cons_bet_wc[elem][3]
        if totals_r != 0 or totals_c != 0:
            totals[elem] = totals_c + totals_r


    # c = []
    # v = []
    percentil = {}
    if len(cons_bet_wc) >= len(cons_bet_wr):
        dict_to_it = cons_bet_wc
        sec_to_it = cons_bet_wr
    else:
        dict_to_it = cons_bet_wr
        sec_to_it = cons_bet_wc

    for key in dict_to_it:
        if key != "x86_uinst_effaddr":
            if key in sec_to_it:
                #aux = np.add(dict_to_it[key], sec_to_it[key])
                #aux = dict_to_it[elem].append( sec_to_it[elem])
                percentil[key] = np.append(dict_to_it[key][1:], sec_to_it[key][1:])
                #print("IF")
            else:
                percentil[key] = np.append(dict_to_it[key][1:], [0,0,0])

    for key in percentil:
        #print(key)
        #total = 0.0
        for x in range(0,6):
            if percentil[key][x] != 0.0:
                percentil[key][x] = percentil[key][x]/totals[key]
        #        total = total + percentil[key][x]
        #print(total)

    #####PLOTING PARTR#####
    opc = []
    vals = []
    for key, val in percentil.items():
        opc.append(key)
        vals.append(val)
    vals = np.array(vals)
    fig, ax = plt.subplots()
    plt.bar( range(len(opc)), vals[:,0],label="1 read(c)")
    plt.bar(range(len(opc)), vals[:, 1], bottom=vals[:, 0],label="2 reads(c)")
    plt.bar(range(len(opc)), vals[:, 2], bottom=vals[:, 0]+vals[:, 1],label="3 or + reads(c)")
    plt.bar(range(len(opc)), vals[:, 3], bottom=vals[:, 0] + vals[:, 1]+vals[:, 2],label="1 read(r)")
    plt.bar(range(len(opc)), vals[:, 4], bottom=vals[:, 0] + vals[:, 1] + vals[:, 2]+ vals[:, 3],label="2 reads(r)")
    plt.bar(range(len(opc)), vals[:, 5], bottom=vals[:, 0] + vals[:, 1] + vals[:, 2] + vals[:, 3] + vals[:, 4],label="3 or + reads(r)")
    #plt.bar(range(len(opc)), vals[:, 6], bottom=vals[:, 0] + vals[:, 1] + vals[:, 2] + vals[:, 3] + vals[:, 4]+vals[:, 5],label="3 or + reads(r)")

    plt.grid()
    plt.title(bench)
    ax.legend(ncol=4, bbox_to_anchor=(0.5, 1.25), loc="center")
    plt.xticks(range(len(opc)), opc)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(dump_path+bench)
    plt.close()

def list_benchs(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    res = []
    for elem in files:
        if '.out' in elem:
            res.append( elem.replace('.out',''))
    return res

benchs = list_benchs(argv[1])
for bench in benchs:
    path = argv[1]+bench+".out"
    print(path)
    res = argv[2]
    print(res)
    traza_to_plot(path,res,bench)

#traza_to_plot("/home/hutarsan/Documentos/racetrack/racetrack/hangar/outputs/rf90perf/aux", "/home/hutarsan/Documentos/racetrack/racetrack/hangar/","prueba")