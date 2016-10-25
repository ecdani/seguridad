import datetime


class Bomba:
    abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    r1 = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    r2 = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    r3 = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    rfb = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')

    #dic = ['AMBIGUO', 'OBVIO', 'TRIVIAL', 'ESTUPENDO', 'ESTHER', 'BUGZILLA', 'THEVENIN', 'PACIFICO', 'DIARREA', 'HOLA', 'MUNDO', 'GARABATA', 'PAPILOMA', 'HERPES', 'CELULA', 'PORRO', 'SUAVES', 'DIMITRI', 'FIESTA', 'PATATA', ]
    dic = ['DEMIAN'] #

    #codigo = list('GSUTUBBWAXCANFJPPQRLDQQWDJTSVEXHUDHS')
    codigo = list('AJXGSTMFRCTXBS')
    msj = ''

    # Estado interno
    rk1, rk2, rk3 = 0, 0, 0

    def atacar(self):
        clvdic = []
        clv1, clv2, p, o = 0, 0, 0, 0 # indices clavijeros, progreso, ocurrencias

        # Rendimiento: Asignación a variables locales
        srk1 = self.rk1
        srk2 = self.rk2
        srk3 = self.rk3
        scodify = self.codify
        sabc = self.abc


        f = open('.\datos.txt', 'w').close()
        f = open('.\datos.txt', 'a')
        f.write(((datetime.datetime.now()).strftime('Iniciado el dia %d-%m-%Y - Hora %H:%M:%S\n')))
        for clv1 in range(26):
            for clv2 in range(clv1, 26):
                print("clv1 y 2:"+str(clv1)+str(clv2))
                p += 1
                print('%i de 676' % p)
                output =sabc[clv1] + sabc[clv2]
                input =sabc[clv2] + sabc[clv1]
                print ('in %s out %s' % (input, output))
                trans_table = str.maketrans(input, output)
                clvdic = [word.translate(trans_table) for word in self.dic]
                #clvdic = self.dic
                #self.msj = [word.translate(trans_table) for word in self.codigo]
                #self.msj = self.codigo
                #print(self.dic)
                #print(self.codigo)
                for k1 in range(26):
                    srk1 = k1
                    for k2 in range(26):
                        srk2 = k2
                        for k3 in range(26):
                            srk3 = k3
                            self.msj = [word.translate(trans_table) for word in self.codigo]
                            sol = scodify()
                           # if (k1 == 0 and k2 == 0 and k3 == 0):
                               # print('PRE::'+sol)
                                #sol = sol.translate(trans_table)
                               # print('POST::'+sol)                    
                            #sol = sol.translate(trans_table)
       
                            for word in clvdic:
                                if word in sol:
                                    print(word)
                                    o += 1
                                    
                                    output = '----**Registro %s**----\n%s\n%s\n%s\n\n' % (o, sabc[k1] + sabc[k2] + sabc[k3], sol, trans_table)
                                    f.write(output)
                                    print(output)
        f.write(datetime.datetime.now().strftime('Iniciado el dia %d-%m-Y - Hora %H:%M:%S\n'))
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

    def codify(self):
        cod = list()
        sencode = self.encode
        for ch in self.msj:
            cod.append(sencode(ch))
        return ("".join(cod))

Bomba().atacar()
