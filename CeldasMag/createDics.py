from __future__ import print_function
import pandas as pd
import os

#Def dictionarios anidados
def create_dic(path):
    pid_dictionary = dict()

    for bench in sorted(os.listdir(path)):
        int_reps_dir = path + bench + "/interval_reports/x86_ctx/"


        if len(os.listdir(path)) < 1:
            print("Benchmark " + bench + " err: no input files available")
            continue

        pid_dict = dict()
        for pid in os.listdir(int_reps_dir):
            if pid.endswith("~") == False:
                pidid = pid.split('.')[0]
                data_frame = pd.read_csv(int_reps_dir + pid, sep=',',
                header=0, usecols=None)
                pid_dict[pidid] = data_frame

        pid_dictionary[bench] = pid_dict

    return pid_dictionary

def create_dic_nt(path):
    pid_dictionary = dict()

    for bench in sorted(os.listdir(path)):
        int_reps_dir = path + bench + "/interval_reports/x86_ctx/"


        if len(os.listdir(path)) < 1:
            print("Benchmark " + bench + " err: no input files available")
            continue

        pid_dict = dict()
        for pid in os.listdir(int_reps_dir):
            if pid.endswith("~") == False:
                pidid = pid.split('.')[0]
                data_frame = pd.read_csv(int_reps_dir + pid, sep=',',
                header=None, usecols=None)
                pid_dict[pidid] = data_frame

        pid_dictionary[bench] = pid_dict

    return pid_dictionary



def create_dic_mod(path):
    pid_dictionary = dict()

    for bench in sorted(os.listdir(path)):
        int_reps_dir = path + bench + "/interval_reports/mod/"

        if len(os.listdir(path)) < 1:
            print("Benchmark " + bench + " err: no input files available")
            continue

        pid_dict = dict()
        for pid in os.listdir(int_reps_dir):
            if (pid == "dl1-0.intrep.csv"):
                if pid.endswith("~") == False:
                    pidid = pid.split('.')[0]
                    data_frame = pd.read_csv(int_reps_dir + pid, sep=',',
                                             header=0, usecols=None)
                    pid_dict[pidid] = data_frame

        pid_dictionary[bench] = pid_dict

    return pid_dictionary

def create_dic_p(path):
    pid_dictionary = dict()

    for bench in sorted(os.listdir(path)):
        # MOD AQUI
        int_reps_dir = path + bench + "/interval_reports/mod/"

        if len(os.listdir(path)) < 1:
            print("Benchmark " + bench + " err: no input files available")
            continue

        pid_dict = dict()
        for pid in os.listdir(int_reps_dir):
            if (pid == "dl1-0.intrep.csv"):
                if pid.endswith("~") == False:
                    pidid = pid.split('.')[0]
                    data_frame = pd.read_csv(int_reps_dir + pid, sep=',',
                                             header=0, usecols=None)
                    pid_dict[pidid] = data_frame

        pid_dictionary[bench] = pid_dict

    return pid_dictionary

def create_dic_agrupado(path):
    pid_dictionary = dict()

    for bench in sorted(os.listdir(path)):
        # MOD AQUI
        int_reps_dir = path + bench
        data_frame = pd.read_csv(int_reps_dir, sep=',',
                                             header=0, usecols=None)

        pid_dictionary[bench] = data_frame

    return pid_dictionary

