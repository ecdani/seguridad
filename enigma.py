class Enigma:
    abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    r1 =  list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    r2 =  list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    r3 =  list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    rfb = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    clv = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    key = list('BDT')
    msj = list('JDLSIEURJNZMAKFLDPOEUERUNVMNXJDHEYHHHHWJXBSKQUERHBSKJNA')

    # Estado interno
    rk1, rk2, rk3 = 0,0,0
    def putkey(self):
        self.rk1 = self.abc.index(self.key[0])
        self.rk2 = self.abc.index(self.key[1])
        self.rk3 = self.abc.index(self.key[2])

    def rotor(self,ch,rot,rk):
        s = rot[(self.abc.index(ch)+rk) % 26]
        return self.abc[(self.abc.index(s)-rk) % 26]

    def rotorinv(self,ch,rot,rk):
        s = self.abc[(self.abc.index(ch)+rk) % 26]
        return self.abc[(rot.index(s)-rk) % 26]

    def clav(self,ch,abc,clv):
        return clv[abc.index(ch)]

    def rotar(self):
        self.rk3 += 1
        if self.rk3 == 22:#w
            self.rk3 = 0
            self.rk2 += 1
        if self.rk2 == 5:#f
            self.rk2 = 0
            self.rk1 += 1

    def encode(self,ch):
        ch = self.clav(ch,self.abc,self.clv)
        self.rotar()
        ch = self.rotor(ch,self.r3,self.rk3)
        ch = self.rotor(ch,self.r2,self.rk2)
        ch = self.rotor(ch,self.r1,self.rk1)
        ch = self.reflector(ch)
        ch = self.rotorinv(ch,self.r1,self.rk1)
        ch = self.rotorinv(ch,self.r2,self.rk2)
        ch = self.rotorinv(ch,self.r3,self.rk3)
        ch = self.clav(ch,self.clv,self.abc)
        return ch

    def reflector(self,ch):
        return self.rfb[self.abc.index(ch)]

    def translate(self):
        self.putkey()
        cod = list()
        for ch in self.msj:
            cod.append(self.encode(ch))
        print("".join(cod))

Enigma().translate()
