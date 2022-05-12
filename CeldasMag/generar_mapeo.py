i = 0
print("Posicion directa  Posicion entrelazada")
for x in range(0,32):
    print(str(x)+"--------------------"+str(x*4))
i = 0
for x in range(32,64):

    print(str(x)+"--------------------"+str((i*4+1)))
    i = i + 1
i = 0
for x in range(64,96):

    print(str(x) + "--------------------" + str((i * 4 + 2)))
    i = i + 1
i = 0
for x in range(96,128):

    print(str(x) + "--------------------" + str((i * 4 + 3)))
    i = i + 1