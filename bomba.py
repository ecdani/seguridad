import datetime


class Bomba:
    abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # abcn = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
    r1 = (4,10,12,5,11,6,3,16,21,25,13,19,14,22,24,7,23,20,18,15,0,8,1,17,2,9)
    ri1 = (20,22,24,6,0,3,5,15,21,25,1,4,2,10,12,19,7,23,18,11,17,8,13,16,14,9)
    r2 = (0,9,3,10,18,8,17,20,23,1,11,7,22,19,12,2,16,6,25,13,15,24,5,21,14,4)
    ri2 = (0,9,15,2,25,22,17,11,5,1,3,10,14,19,24,20,16,6,4,13,7,23,12,8,21,18)
    r3 = (1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14)
    ri3 = (19,0,6,1,15,2,18,3,16,4,20,5,21,13,25,7,24,8,23,9,22,11,17,10,14,12)
    rfb = (24,17,20,7,16,18,11,3,15,23,13,6,14,10,12,8,4,1,5,25,2,22,21,9,0,19)

    dic = ['AMBIGUO', 'OBVIO', 'TRIVIAL', 'ESTUPENDO', 'ESTHER', 'BUGZILLA', 'THEVENIN', 'PACIFICO', 'DIARREA', 'HOLA', 'MUNDO', 'GARABATA', 'PAPILOMA', 'HERPES', 'CELULA', 'PORRO', 'SUAVES', 'DIMITRI', 'FIESTA', 'PATATA', ]

    codigo = list('YLJKKVAWHAQTJITNQUPTJSHDBWGDSBEOWKLEDBYBJSSGCI')

    # Estado interno
    rk1, rk2, rk3 = 0, 0, 0

    def atacar(self):
        clv1, clv2, p, o = 0, 0, 0, 0 # indices clavijeros, progreso, ocurrencias

        # Rendimiento: Asignación a variables locales
        scodify = self.codify
        sabc = self.abc


        f = open('.\datos.txt', 'w').close()
        f = open('.\datos.txt', 'a')
        f.write(((datetime.datetime.now()).strftime('Iniciado el dia %d-%m-%Y - Hora %H:%M:%S')))
        for clv1 in range(26):
            for clv2 in range(clv1+1, 26):
                p += 1
                inter = sabc[clv1] + sabc[clv2]
                print ('\n%i de 325 Intercambio %s---------' % (p, inter))
                trans_table = str.maketrans(sabc[clv2] + sabc[clv1], inter)
                clvdic = [word.translate(trans_table) for word in self.dic]
                msj = [word.translate(trans_table) for word in self.codigo]

                nmsj = [self.abc.index(word) for word in msj]
                '''nmsj = list()
                for ch in msj:
                    nmsj.append(self.abc.index(ch))'''

                for k1 in range(26):
                    for k2 in range(26):
                        for k3 in range(26):
                            self.rk1 = k1
                            self.rk2 = k2
                            self.rk3 = k3
                            sol = scodify(nmsj)
                            for word in clvdic:
                                if word in sol:
                                    o += 1
                                    salida = '\nRegistro %s: Key:%s Intercambio:%s Msj:%s' % (o, sabc[k1] + sabc[k2] + sabc[k3], inter, sol.translate(trans_table))
                                    f.write(salida)
                                    print(salida)
        f.write(datetime.datetime.now().strftime('\nTerminado el dia %d-%m-Y - Hora %H:%M:%S'))
        f.close() 

    def rotar(self):
        if self.rk1 == 26:
            self.rk1 = 0

        # En la posición previa autogira
        if self.rk2 == 4: #f
            self.rk2 += 1
            self.rk1 += 1
        elif self.rk2 == 26:
            self.rk2 = 0

        self.rk3 += 1
        if self.rk3 == 22:#w
            self.rk2 += 1
        elif self.rk3 == 26:
            self.rk3 = 0

    def encode(self, ch):
        self.rotar()
        ch = ((self.r3[(ch + self.rk3) % 26] - self.rk3) % 26)
        ch = ((self.r2[(ch + self.rk2) % 26] - self.rk2) % 26)
        ch = ((self.r1[(ch + self.rk1) % 26] - self.rk1) % 26)
        ch = self.rfb[ch]
        ch = ((self.ri1[(ch + self.rk1) % 26] - self.rk1) % 26)
        ch = ((self.ri2[(ch + self.rk2) % 26] - self.rk2) % 26)
        ch = ((self.ri3[(ch + self.rk3) % 26] - self.rk3) % 26)
        return ch

    def codify(self,msj):
        cod = list()
        sencode = self.encode
        for ch in msj:
            cod.append(self.abc[sencode(ch)])
        return ("".join(cod))

Bomba().atacar()
