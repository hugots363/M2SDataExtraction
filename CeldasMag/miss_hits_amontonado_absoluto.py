import pandas as pd
from sys import argv
import re
import createDics as cd


if len(argv) < 2:
    print("Usage: <Script> <Benchmark_path> <Set size> <Headers>\n")
    exit()
benchmark = argv[1].split("/")
print(argv)
longitud = len(benchmark)
benchmark = benchmark[longitud - 2]
rango =int(argv[3]) -1
cabezales = int(argv[4])
# Var declaration
cond = True
i = 0
via = 0
ciclos_p = 0
sets = 0
num = 0
sets = 0
max = 0
vias = re.findall(r"(\d+)vias", argv[1])
vias = vias[0]
vias = int(vias)
total = 0
names = []
benchs = cd.create_dic(argv[1])
# df = pd.DataFrame(argv[1]+"interval_reports/mod/dl1-0.intrep.csv")
accesos = 0
hits = 0
misses = 0

names = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
miss1 = []
miss2 = []
miss3 = []
miss4 = []
miss5 = []
totalx = []
dic = dict()
#Variables para la media con 4 tramos
#mt0 = 0;
 #mt1 = 0;
#mt2 = 0;
#mt3 = 0;

# npy.zeros((n,n))
# Main

for benchmark,arc_name in benchs.items():
    #print(benchmark)
    #rint("\n")
    for arc_n,df in arc_name.items():
        #print(argv[1]+benchmark+"/interval_reports/mod/dl1-0.intrep.csv")
        df = pd.read_csv(argv[1]+benchmark+"/interval_reports/mod/dl1-0.intrep.csv")
# df = pd.read_csv(path_to_b+"/"+benchmark+"/interval_reports/mod/dl1-0.intrep.csv")
    #Geting the name df
    lrow = len(df.index) -1
    names.append(benchmark)
    total = 0
    tope = int((rango + 1) / cabezales)
    #print(vias)
    #print(benchmark)
    for x in range(0,vias):
            for y in range(0,tope):
                    #print(y)
                    #print("via =  "+str(x)+ " set = " + str(y)) #dl1-0-c4t1-via-0-ciclos-penalizacion-0
                    #print(df.at[lrow, "dl1-0-c4t1-via-"+str(x)+"-ciclos-penalizacion-"+str(y)])
                    #print(y)
                    total = total + df.at[lrow, "dl1-0-c4t1-via-"+str(x)+"-ciclos-penalizacion-"+str(y)]

    totalx.append(total)
    # print("[DEBUG] "+str(benchmark)+ ": " +str(media_t))
    for x in range(0,vias):
            hits = hits+  df.at[lrow, "dl1-0-c4t1-via-"+str(x)+"-ciclos-penalizacion hits-0"]
            misses= misses + df.at[lrow, "dl1-0-c4t1-via-"+str(x)+"-ciclos-penalizacion misses-0"]
    t1.append(hits)
    miss1.append(misses)
    hits = 0
    misses = 0

    for x in range(0,vias):
            for y in range(1,4):
                hits = hits + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion hits-"+str(y)]
                misses = misses + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion misses-"+str(y)]
    t2.append(hits)
    miss2.append(misses)
    hits = 0
    misses = 0

    for x in range(0,vias):
            for y in range(4,9):
                hits = hits + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion hits-"+str(y)]
                misses = misses + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion misses-"+str(y)]
    t3.append(hits)
    miss3.append(misses)
    hits = 0
    misses = 0

    for x in range(0,vias):
            for y in range(9,17):
                hits = hits + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion hits-"+str(y)]
                misses = misses + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion misses-"+str(y)]
    t4.append(hits )
    miss4.append(misses )
    hits = 0
    misses = 0
    for x in range(0,vias):
            for y in range(17,tope):
                hits = hits + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion hits-"+str(y)]
                misses = misses + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion misses-"+str(y)]
    t5.append(hits )
    miss5.append(misses)
    hits = 0
    misses = 0

#names.append("Media global")
#t1.append((mt0/(mt0+mt1+mt2+mt3))*100)
#t2.append((mt1/(mt0+mt1+mt2+mt3))*100)
#t3.append((mt2/(mt0+mt1+mt2+mt3))*100)
#t4.append((mt3/(mt0+mt1+mt2+mt3))*100)



#[DEBUG]
#print(len(t1))
#print(len(t2))
#print(len(t3))
#print(len(t4))




dic["Benchmark"] = names
dic["Tramo 0 hits"] = t1
dic["Tramo 1-3 hits"] = t2
dic["Tramo 4-8 hits"] = t3
dic["Tramo 9-16 hits"] = t4
dic["Tramo +16 hits"] = t5
dic["Tramo 0 misses"] = miss1
dic["Tramo 1-3 misses"] = miss2
dic["Tramo 4-8 misses"] = miss3
dic["Tramo 9-16 misses"] = miss4
dic["Tramo +16 misses"] = miss5
dic["Total"] = totalx


dff = pd.DataFrame(dic)
print(tope)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )
