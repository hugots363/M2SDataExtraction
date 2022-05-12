import createDics as cd
import pandas as pd
from sys import argv
import re
import createDics as cd


if len(argv) < 2:
    print("Usage: <Script> <Benchmark_path>\n")
    exit()
benchmark = argv[1].split("/")
longitud = len(benchmark)
benchmark = benchmark[longitud - 2]
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

names = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
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



# get number of sets
    if(sets  == 0 ):
        for col in df.columns:
            aux = list(col)
            length = len(aux)

            pens = []
            # print(aux)
            if aux[length - 2] == '-':
                num = aux[length - 1]

            elif (aux[length - 3] == '-'):
                num = (aux[length - 2]) + (aux[length - 1])
            else:
                num = (aux[length - 3]) + (aux[length - 2]) + (aux[length - 1])

            if (num.isdigit()):
                if (int(num) > max):
                    max = int(num)

        sets = max
        n_vias = dict()
    #Geting the name df
    lrow = len(df.index) - 17
    names.append(benchmark)
    total = 0
    rango = sets
    if vias == 128:
        rango = 4
    if vias == 64:
        rango = 8
    if vias == 32:
        rango = 5
    for x in range(0,vias):
        try:
            #Utiliar sets para todos o hasta donde se quiera llegar +1
            for y in range(0,rango):
                    total = total + df.at[lrow, "dl1-0-c4t1-via-"+str(x)+"-ciclos-penalizacion-"+str(y)]
        except:
            print("Fuera de rango 1")
    media_t = total/vias
    #print(media_t)

    # print("[DEBUG] "+str(benchmark)+ ": " +str(media_t))

    total = 0
    for x in range(0,vias):
        try:
            total = total + df.at[lrow, "dl1-0-c4t1-via-"+str(x)+"-ciclos-penalizacion-0"]
        except:
            total = total
    accesos = accesos + total
    total = total/vias
    try:
        t1.append((total/media_t)*100)
    except:
        t1.append(0)

    total = 0
    for x in range(0,vias):
        try:
            for y in range(1,4):
                total = total + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion-"+str(y)]
        except:
            print("Fuera de rango 2")
    accesos = accesos + total
    total = total/vias
    try:
        t2.append((total/media_t)*100)
    except:
        t2.append(0)

    total = 0

    var= 9
    if rango <= 8:
        t3.append(0)

    else:
        try:
            for x in range(0, vias):
                for y in range(4,var ):
                    total = total + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion-" + str(y)]
        except:
            print("Fuera de rango 3")
        accesos = accesos + total
        total = total / vias
        try:
            t3.append((total / media_t) * 100)
        except:
            t3.append(0)
        for x in range(var,9):
            t3.append(0)

    total = 0
    if rango > 8:
        try:
            for x in range(0, vias):
                for y in range(9, 17):
                    total = total + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion-" + str(y)]
        except:
            print("Fuera de rango 4")
        accesos = accesos + total
        #print ("Numero de  accesos: " + str(accesos))
        total = total / vias
        try:
            t4.append((total / media_t) * 100)
        except:
            t4.append(0)
    else:

            t4.append(0)
    total = 0
    if rango > 8:
        try:
            for x in range(0, vias):
                for y in range(17, sets+1):
                    total = total + df.at[lrow, "dl1-0-c4t1-via-" + str(x) + "-ciclos-penalizacion-" + str(y)]
        except:
            print("Fuera de rango 5")
        accesos = accesos + total
        total = total / vias
        try:
            t5.append((total / media_t) * 100)
        except:
            t5.append(0)
    else:
        t5.append(0)

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
dic["Tramo 0"] = t1
dic["Tramo 1-3"] = t2
dic["Tramo 4-8"] = t3
dic["Tramo 9-16"] = t4
dic["Tramo +16"] = t5


dff = pd.DataFrame(dic)
print(dff)
dff.to_csv(argv[2], sep= ",",index=False )



