class Enigma:
    abc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    r1 =  list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    r2 =  list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    r3 =  list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    rfb = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    clv = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    key = list('AAA')
    msj = list('MENSAJEDEPRUEBA')
    
    # Estado interno
    rk1, rk2, rk3 = 0,0,0
    inv = False

    def clavijas(self,ch):
        if self.inv:
            self.inv = False
            return self.abc[self.clv.index(ch)]
        else:
            return self.clv[self.abc.index(ch)]

    def rotor3(self,ch):
        """
            Giro, decode, vuelta y giro
        """
        if self.inv:
            s = self.abc[(self.abc.index(ch)+self.rk3) % 26] # Decode
            print("InvR3DECO:"+s)
            s = self.abc[(self.r3.index(s)-self.rk3) % 26]
            print("InvR3:"+s)
            return s
        else:
            self.rk3 += 1
            s = self.r3[(self.abc.index(ch)+self.rk3) % 26] # Decode
            s = self.abc[(self.abc.index(s)-self.rk3) % 26]
            print("R3:"+s)
            return s

    def rotor2(self,ch):
        if self.inv:
            s = self.abc[(self.abc.index(ch)+self.rk2) % 26] # Decode
            s = self.abc[(self.r2.index(s)-self.rk2) % 26]
            print("InvR2:"+s)
            return s
        else:
            if self.rk3 == 26:
                self.rk3 = 0
                self.rk2 += 1
            s = self.r2[(self.abc.index(ch)+self.rk2) % 26] # Decode
            s = self.abc[(self.abc.index(s)-self.rk2) % 26]
            print("R2:"+s)
            return s

    def rotor1(self,ch):
        if self.inv:
            s = self.abc[(self.abc.index(ch)+self.rk1) % 26] # Decode
            s = self.abc[(self.r1.index(s)-self.rk1) % 26]
            print("InvR1:"+s)
            return s
        else:
            if self.rk2 == 26:
                self.rk2 = 0
                self.rk1 += 1
            s = self.r1[(self.abc.index(ch)+self.rk1) % 26] # Decode
            s = self.abc[(self.abc.index(s)-self.rk1) % 26]
            print("R1:"+s)
            return s

    def reflector(self,ch):
        self.inv = True
        s = self.rfb[self.abc.index(ch)] # Decode
        print("Refl:"+s)
        return s
    def decode(self,ch):
        s = self.reflector(self.rotor1(self.rotor2(self.rotor3(self.clavijas(ch)))))
        #print(s)
        s = self.rotor3(self.rotor2(self.rotor1(s)))
        #print(s)
        return s
    def translate(self):
        cod = list()
        for ch in self.msj:
            s = self.decode(ch)
            print("SALIDA:"+s)
            cod.append(s)
        print(cod)



e = Enigma()
#sc = clavijas('A',input,output)
e.translate()
#s3 = rotor3(sc)
#print(s3)
#s2 = rotor2(s3)
#print(s2)
#s1 = rotor1(s2)
#print(s1)
