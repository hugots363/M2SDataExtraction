file = open("/home/hutarsan/Documentos/racetrack/hangar/aux",'r')
int_opcodes = [0,1,2,3,4,5,6,7,8,9,10,11,12,52,53,54,55,56,57,58,59,60,61]
data = [int_opcodes, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def opcode_to_pos(op):
    cont = 0
    for num in int_opcodes:
        if(num == int(op)):
            if(int(op)== 61):
                print("61")
            return int(cont)
        cont = cont + 1
    print("FALLO EN FUNC")

#L1W, L2RR, L3RC
while True:
    next_line = file.readline()
    if not next_line:
        break;
    #print(next_line.strip())
    str = next_line.split()
    if(str[0] != "CC" and str[0] != "0"):
        if(int(str[0]) !=  0):
            bars = 0
            opcode = 0
            lim  = len(str)
            for x in range(0,lim):
                if str[0] != "|" :
                    if bars == 0:
                      opcode = str[0]
                      op_pos = opcode_to_pos(opcode)
                      #print(opcode)
                      #print("opcode->"+ opcode)
                      #print("translated to :")
                    elif bars == 1:
                        check = list(str[0])
                        if check[1] == "R":
                            reg = str[0].replace("RR","")
                            #print("Read in REg->"+ reg)
                            #data[opcode_to_pos(opcode)][reg] = 10
                            data[2][op_pos] = data[2][op_pos] +1
                            #print("RR->"+reg)
                        else:
                            reg = str[0].replace("RC", "")
                            data[3][op_pos] = data[3][op_pos] + 1
                            #print("RC  -> " + op_pos)

                    else:
                        if str is not None:
                            #print("W->"+str[0])
                            #print(str)
                            data[1][op_pos] = data[1][op_pos] + 1
                else:
                    bars = bars+1
                del str[0]


file.close()
print(data)