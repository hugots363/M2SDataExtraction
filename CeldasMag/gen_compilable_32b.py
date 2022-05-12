from sys import argv
import os
import re


if len(argv) < 1:
    print("Usage: <Script> <dry_run_archive> \n")
    exit()
#name= argv[0].path
#print(name)
#get path and archive name
path= os.path.dirname(argv[1])
name= os.path.basename(argv[1])
curr_path= os.getcwd()

try:
    #goes to archive path
    os.chdir(path)
    listOfLines = list()

    #creates output file
    res = open("compilacion", "w")
    #opens archive line by line
    with open(name,"r+") as filehandler:
        line = filehandler.readline()
        while line:
            contenedor = re.sub('-m32','-m32 -static',line)
            #contenedor = re.sub('-static','',contenedor)
            #contenedor = re.sub(r'/gcc', r'/gcc -static -m32', line)
            contenedor = re.sub('-D_FILE_OFFSET_BITS=64', '-D_FILE_OFFSET_BITS=32', contenedor)
            print(contenedor)
            res.write(contenedor)
            line = filehandler.readline()

    filehandler.close()
    res.close()


except:
    print("Somthing failed, check the path")
finally:
    os.chdir(curr_path)