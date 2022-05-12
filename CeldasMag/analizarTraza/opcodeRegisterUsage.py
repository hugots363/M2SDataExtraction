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
         "x86_uinst_xmm_fp_mult","x86_uinst_xmm_fp_div","x86_uinst_xmm_fp_sqrt","x86_uinst_xmm_move","x86_uinst_xmm_shuf","x86_uinst_xmm_conv","x86_uinst_load, x86_uinst_store","x86_uinst_prefetch","x86_uinst_call","x86_uinst_ret",
         "x86_uinst_jump","x86_uinst_branch","x86_uinst_ibranch","x86_uinst_syscall","x86_uinst_opcode_count"]

    #acum_RR = np.array([int_opcodes,[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes)])
    #acum_RC = np.array([int_opcodes,[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes),[0.0]*len(int_opcodes)])
    num_cons_prod = {}
    diff = {}
    opcode_to_op = {}
    cont = 0
    for elem in all_opcodes:
        num_cons_prod[elem] = [-1,-1]
        diff[elem] = False
        opcode_to_op[cont] = elem
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
            consumptions = np.array(div[1].split())
            writes = np.array(div[2].split())
            if num_cons_prod[opcode_to_op[opcode]][0] == -1 or num_cons_prod[opcode_to_op[opcode]][1] == -1:
                inst = opcode_to_op[opcode]
                num_cons_prod[inst][0] = len(consumptions)
                num_cons_prod[inst][1] = len(writes)
            else:
                if num_cons_prod[opcode_to_op[opcode]][0] != len(consumptions)  or num_cons_prod[opcode_to_op[opcode]][1] != len(writes) :
                    diff[opcode_to_op[opcode]]  = True
    print(diff)





traza_to_plot("/home/hutarsan/Documentos/racetrack/racetrack/hangar/aux", "/home/hutarsan/Documentos/racetrack/racetrack/hangar/","prueba")