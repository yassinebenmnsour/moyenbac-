
# yassine benmansour ---------------
ar = input("entre note arabe :")
fr = input("entre note francais :")
phi = input("entre note philosophie :")
ang = input("entre note anglais :")
si = input("entre note sience d'ingenieur :")
pc = input("entre note physique :")
math = input("entre note mathematique :")
isl = input("entre note islamiyat :")

noteregional = (int(ar)*2+int(fr)*4+int(isl)*2)/8
notenational = (int(phi)*2+int(math)*7+int(pc)*5+int(si)*8+int(ang)*2)/24

moyen = (int(notenational)+int(noteregional))/2

if int(moyen) < 10:
    print("votre moyen est :")
    print(moyen)
    print("non admis")
else:
    print("votre moyen est :")
    print(moyen)
    print("admis")
