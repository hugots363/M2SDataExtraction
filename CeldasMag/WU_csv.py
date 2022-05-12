import createDics as cd
import pandas as pd
from sys import argv
import csv

if len(argv) < 2:
    print("Usage: <Script> <ReportsDir> \n")
    exit()

dic = dict()
benchs = cd.create_dic(argv[1])

WU_cycles = 7
for benchmark,arc_name in benchs.items():
    #print(benchmark)
    #rint("\n")
    for arc_n,df in arc_name.items():
        for x in range(0,WU_cycles):
            df = df.drop([x])
    #df.to_csv(r'Path where you want to store the exported CSV file\pid100.intrep.csv', sep='\t')
    df.to_csv(argv[1]+benchmark+"/interval_reports/x86_ctx/pid100.intrep.csv", sep= ",",index=False )
print("WU done!")