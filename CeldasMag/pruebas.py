import createDics
from sys import argv

if len(argv) < 2:
    print("Usage: <Script> <ReportsDir>", end="\n")
    exit()


aux = createDics.create_dic(argv[1])
print(len(aux))
for item in aux:
    print(item)