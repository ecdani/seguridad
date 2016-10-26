import datetime


class Bomba:
    abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    r1 = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    r2 = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    r3 = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    rfb = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')

    #dic = ['AMBIGUO', 'OBVIO', 'TRIVIAL', 'ESTUPENDO', 'ESTHER', 'BUGZILLA', 'THEVENIN', 'PACIFICO', 'DIARREA', 'HOLA', 'MUNDO', 'GARABATA', 'PAPILOMA', 'HERPES', 'CELULA', 'PORRO', 'SUAVES', 'DIMITRI', 'FIESTA', 'PATATA', ]
    dic = ['FIESTA']

    codigo = list('GSUTUBBWAXCANFJPPQRLDQQWDJTSVEXHUDHS')
    #codigo = list('RXZRUBOHUAKZOIKCCCE')
    msj = []

    # Estado interno
    rk1, rk2, rk3 = 0, 0, 0

    def atacar(self):
        #clvdic = []
        clv1, clv2, p, o = 0, 0, 0, 0 # indices clavijeros, progreso, ocurrencias

        # Rendimiento: Asignación a variables locales
        scodify = self.codify
        sabc = self.abc


        f = open('.\datos.txt', 'w').close()
        f = open('.\datos.txt', 'a')
        f.write(((datetime.datetime.now()).strftime('Iniciado el dia %d-%m-%Y - Hora %H:%M:%S')))
        for clv1 in range(26):
            for clv2 in range(clv1, 26):
                p += 1
                input =sabc[clv2] + sabc[clv1]
                print ('\n%i de 676 Intercambio %s---------' % (p, input))
                trans_table = str.maketrans(input, sabc[clv1] + sabc[clv2])
                clvdic = [word.translate(trans_table) for word in self.dic]
                self.msj = [word.translate(trans_table) for word in self.codigo]
                for k1 in range(26):
                    for k2 in range(26):    
                        for k3 in range(26):
                            self.rk1 = k1
                            self.rk2 = k2
                            self.rk3 = k3
                            sol = scodify()
                            for word in clvdic:
                                if word in sol:
                                    o += 1
                                    output = '\nRegistro %s: Key:%s Msj:%s' % (o, sabc[k1] + sabc[k2] + sabc[k3], sol.translate(trans_table))
                                    f.write(output)
                                    print(output)
        f.write(datetime.datetime.now().strftime('\nTerminado el dia %d-%m-Y - Hora %H:%M:%S'))
        f.close() 

    def rotor(self, ch, rot, rk):
        s = rot[(self.abc.index(ch) + rk) % 26]
        return self.abc[(self.abc.index(s) - rk) % 26]

    def rotorinv(self, ch, rot, rk):
        s = self.abc[(self.abc.index(ch) + rk) % 26]
        return self.abc[(rot.index(s) - rk) % 26]

    def rotar(self):
        self.rk3 += 1
        if self.rk3 == 22:  # w
            self.rk2 += 1
        elif self.rk3 == 26:
            self.rk3 = 0
        if self.rk2 == 5: #4 f 
            #self.rk2 += 1
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

    def codify(self):
        cod = list()
        sencode = self.encode
        for ch in self.msj:
            cod.append(sencode(ch))
        return ("".join(cod))

Bomba().atacar()
