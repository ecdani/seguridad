import datetime


class Bomba:
    abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    r1 = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    r2 = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    r3 = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    rfb = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')

    # dic = ['AMBIGUO', 'OBVIO', 'TRIVIAL', 'ESTUPENDO', 'ESTHER', 'BUGZILLA', 'THEVENIN', 'PACIFICO', 'DIARREA', 'HOLA', 'MUNDO', 'GARABATA', 'PAPILOMA', 'HERPES', 'CELULA', 'PORRO', 'SUAVES', 'DIMITRI', 'FIESTA', 'PATATA', ]
    dic = ['NAZI']

    key = list('AAA')
    # msj = list('GSUTUBBWAXCANFJPPQRLDQQWDJTSVEXHUDHS')
    msj = list('CWOINBYPQJZJX')

    # Estado interno
    rk1, rk2, rk3 = 0, 0, 0

    # Bomba

    def atacar(self):
        clv = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        clvdic = []
        clv1, clv2 = 0, 0
        contador = 1
        inicio = datetime.datetime.now()
        inicio = inicio.strftime('Iniciado el dia %d-%m-%Y - Hora %H:%M:%S\n')
        try:
            archivo = self.abrirtxt()
        except Exception:
            archivo = self.creartxt()
            archivo = self.abrirtxt(archivo)
        self.escribirarchivo(archivo, inicio)
        self.cerrararchivo(archivo)
        for clv1 in range(26):
            for clv2 in range(clv1, 26):
                # clvdic = self.dic[:]
                trans_table = str.maketrans(clv[clv1] + clv[clv2], clv[clv2] + clv[clv1])
                clvdic = [word.translate(trans_table) for word in self.dic]

                # print(clvdic[0])
                # k1, k2, k3 = 0,0,0
                for k1 in range(26):
                    for k2 in range(26):
                        for k3 in range(26):
                            self.putkey(k1, k2, k3)
                            sol = self.translate()
                            sol.translate(trans_table)
                            for word in clvdic:
                                # print(word)
                                if word in sol:
                                    parm1 = self.abc[k1] + self.abc[k2] + self.abc[k3]
                                    parm2 = sol.translate(trans_table)
                                    parm3 = trans_table
                                    # print (parm1)
                                    # print(parm2)
                                    # print(parm3)
                                    contador = self.guardar_txt(parm1, parm2, parm3, contador)
        fin = datetime.datetime.now()
        fin = fin.strftime('Iniciado el dia %d-%m-Y - Hora %H:%M:%S\n')
        direrencia = '%s' % (fin - inicio)
        archivo = self.abrirtxt()
        archivo = self.escribirarchivo(archivo, fin)
        archivo = self.escribirarchivo(archivo, direrencia)
        self.cerrararchivo(archivo)

    def putkey(self, k1, k2, k3):
        self.rk1 = k1
        self.rk2 = k2
        self.rk3 = k3

    def rotor(self, ch, rot, rk):
        s = rot[(self.abc.index(ch) + rk) % 26]
        return self.abc[(self.abc.index(s) - rk) % 26]

    def rotorinv(self, ch, rot, rk):
        s = self.abc[(self.abc.index(ch) + rk) % 26]
        return self.abc[(rot.index(s) - rk) % 26]

    def clav(self, ch, abc, clv):
        return clv[abc.index(ch)]

    def rotar(self):
        self.rk3 += 1
        if self.rk3 == 22:  # w
            self.rk2 += 1
        elif self.rk3 == 26:
            self.rk3 = 0
        if self.rk2 == 4:
            self.rk2 += 1
            self.rk1 += 1
        elif self.rk2 == 26:
            self.rk2 = 0
        if self.rk1 == 26:
            self.rk1 = 0

    def encode(self, ch):
        self.rotar()
        return self.rotorinv(self.rotorinv(self.rotorinv(self.reflector(
            self.rotor(self.rotor(self.rotor(ch, self.r3, self.rk3), self.r2, self.rk2), self.r1, self.rk1)), self.r1,
            self.rk1), self.r2, self.rk2), self.r3, self.rk3)

    def reflector(self, ch):
        return self.rfb[self.abc.index(ch)]

    def translate(self):

        cod = list()
        for ch in self.msj:
            cod.append(self.encode(ch))
        return ("".join(cod))

    def guardar_txt(self, parm1, parm2, parm3, contador):
        cadena = '----**Registro %s**----\n%s\n%s\n%s\n\n' % (contador, parm1, parm2, parm3)
        try:
            archivo = self.abrirtxt()
        except Exception:
            print("Error!")
            archivo = self.creartxt()
            archivo = self.abrirtxt()
        self.escribirarchivo(archivo, cadena)
        self.cerrararchivo(archivo)
        contador += 1
        return contador

    def creartxt(self, date=None):
        archi = open('.\datos.txt', 'w')
        if date:
            archi = self.escribirarchivo(archi, date)
        self.cerrararchivo(archi)

    def abrirtxt(self):
        archivo = open('.\datos.txt', 'a')
        return archivo

    def escribirarchivo(self, archivo, cadena):
        print("write!")
        archivo.write(cadena)
        return archivo

    def cerrararchivo(self, archivo):
        archivo.close()


Bomba().atacar()
