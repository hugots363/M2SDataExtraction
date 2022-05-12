import createDics as cd
import pandas as pd
from sys import argv
import matplotlib.pyplot as plt
import numpy as np






if len(argv) < 3:
    print("Usage: <Script> <ReportsDir> <nameCSV> <Tam Reg Bank>\n")
    exit()


dic = dict()
benchs = cd.create_dic_agrupado(argv[1])
print(argv[1])
aux1 = []
aux2 = []
pen_max = int(argv[3])
bench = ""
aux = 0
check = 0
col = "int_cons_per_write_r"

for benchmark,arc_name in benchs.items():
    for letra in benchmark:
        if(letra != "."):
            bench = bench+letra
        else:
            break

    if aux == 0:
        tops = list(arc_name.columns.values)
        tops.insert(0, "Benchmarks")
        res = arc_name.copy()
        res.insert(0, "Benchmark", bench)
        aux = 1
    else:
        arc_name.insert(0, "Benchmark", bench)
        res = res.append(arc_name)

    aux2.append(bench)
    bench = ""

#res.to_csv(argv[2], sep= ",",index=False )
df = pd.DataFrame(res["Benchmark"])
nBenchs = len(res)
benchs = res.loc[:,"Benchmark"]
total_consumers = []
bot = [0]* nBenchs
for nb in range(0,nBenchs):
    benchmark = res["Benchmark"].iloc[nb]
    total_consumers.append(0)
    perc_cons = []
    for x in range (1,int(argv[3])):
        column = col+str(x)
        total_consumers[nb] = total_consumers[nb] + res[column].iloc[nb]

print(total_consumers)
aux = 0
writes = []
for x in range(1, 6):
    for nb in range(0, nBenchs):
        column = col + str(x)
        num = (res[column].iloc[nb]/total_consumers[nb])*100
        #print(num)
        writes.append(num)
        aux = aux + (res[column].iloc[nb]/total_consumers[nb])*100

    #for x in range(0, int(argv[3])):
     #   column = "int_cons_per_write_r" + str(x)
      #  perc_cons.append((res[column].iloc[nb]/total_consumers)*100)
    #print(writes)
    for nb in range(0, nBenchs):
        if(writes[nb] > 3):
            check = 1


    lab = str(x) +"r"
    plt.bar(benchs,writes, bottom= bot,label=lab)
    for nb in range(1, nBenchs):
            bot[nb] = bot[nb] + (res[column].iloc[nb] / total_consumers[nb]) * 100
    #if (writes[nb] > 2):

    writes = []

writes = [0]*nBenchs
for nb in range(0, nBenchs):
    for x in range(6, int(argv[3])):
        column = col + str(x)
        writes[nb] = writes[nb]+ res[column].iloc[nb]

for nb in range(0, nBenchs):
    writes[nb] = (writes[nb]/total_consumers[nb]) * 100
plt.bar(benchs, writes, bottom=bot, label=">5r")

plt.xticks(rotation = 90)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.title("Distribution of reads between writes for not consumers, integer register file")
plt.title("Distribution of reads between writes for consumers, integer register file")
plt.ylabel("Percentage")
plt.grid()
plt.tight_layout()
#plt.legend(loc="upper right")
plt.savefig(argv[2]+"apilado")
 #print(perc_cons)
# for nb in range(0,nBenchs):
#     benchmark = res["Benchmark"].iloc[nb]
#     int_cons = []
#     fp_cons = []
#     axis = []
#     #for x in range (0,int(argv[3])):
#     for x in range(0, 30):
#         #print(res["int_cons_per_write_r"+ str(x)].iloc[0])
#         int_cons.append(res["int_cons_per_write_r"+ str(x)].iloc[nb])
#         try:
#             fp_cons.append(res["fp_cons_per_write_r" + str(x)].iloc[nb])
#         except:
#             print("Posicion inexistente")
#         #axis.append(int(x))
#         axis.append(int(x*10))
#         #bins = np.linspace(0,2,40)
#     dataframe = pd.DataFrame(int_cons,axis)
#     ax = dataframe.plot(kind='bar',legend=None, color='limegreen')
#     #plt.xticks(range(0,30,1))
#     plt.xticks(range(0,180,10))
#     ##Enable if you want to zoom in first group
#     ####################--------
#     #plt.ylim([0,3000])
#     plt.xlim([0,40])
#     plt.title(benchmark)
#     #plt.show()
#     name = benchmark.replace(".csv","")
#     print(name)
#     plt.savefig(argv[2]+name)
#     plt.clf()
#     plt.close()
#percentByEpoch(res)


#print(res)
