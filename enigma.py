class Enigma:
    abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    r1 =  list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    r2 =  list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    r3 =  list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    rfb = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    clv = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    key = list('KWC')
    msj = list('PULJEQTVXYVTDOM')
    
    # Estado interno
    rk1, rk2, rk3 = 0,0,0
    def putkey(self):
        self.rk1 = self.abc.index(self.key[0])
        self.rk2 = self.abc.index(self.key[1])
        self.rk3 = self.abc.index(self.key[2])

    def rotor(self,ch,abc,rot,rk):
        s = rot[(abc.index(ch)+rk) % 26] # Decode
        s = abc[(abc.index(s)-rk) % 26]
        return s

    def rotorinv(self,ch,abc,rot,rk):
        s = abc[(abc.index(ch)+rk) % 26]
        s = abc[(rot.index(s)-rk) % 26] # Decode
        return s

    def clav(self,ch,abc,clv):
        return self.clv[self.abc.index(ch)]

    def rotar(self):
        self.rk3 += 1
        if self.rk3 == 26:
            self.rk3 = 0
            self.rk2 += 1
        if self.rk2 == 26:
            self.rk2 = 0
            self.rk1 += 1

    def code(self,ch):
        ch = self.clav(ch,self.abc,self.clv)
        self.rotar()
        ch = self.rotor(ch,self.abc,self.r3,self.rk3)
        ch = self.rotor(ch,self.abc,self.r2,self.rk2)
        ch = self.rotor(ch,self.abc,self.r1,self.rk1)
        ch = self.reflector(ch)
        ch = self.rotorinv(ch,self.abc,self.r1,self.rk1)
        ch = self.rotorinv(ch,self.abc,self.r2,self.rk2)
        ch = self.rotorinv(ch,self.abc,self.r3,self.rk3)
        ch = self.clav(ch,self.clv,self.abc)
        return ch

    def reflector(self,ch):
        self.inv = True
        s = self.rfb[self.abc.index(ch)] # Decode
        return s

    def translate(self):
        self.putkey()
        cod = list()
        for ch in self.msj:
            s = self.code(ch)
            cod.append(s)
        print(cod)

e = Enigma()
e.translate()
