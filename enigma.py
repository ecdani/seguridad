
# Configuraciones iniciales de enigma
r1 = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
r2 = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')

AB = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
r3 = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
rfb = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')

output = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
key = list('AAA')

# Estado interno
r1k, rk2, rk3 = 0,0,0
input = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # Alfabeto

def clavijas(ch,input,output):
    return output[input.index(ch)]

def rotor3(ch):
    global r3
    global rk3
    rk3 += 1
    r3.append(r3.pop(0)) # Giro
    s = r3[input.index(ch)] # Decode
    # Vuelta
    # Giro

def rotor2(ch):
    global r2
    global rk2
    global rk3
    if rk3 == 26:
        rk3 = 0
        rk2 += 1
        r2.append(r2.pop(0))
    return r2[input.index(ch)]

def rotor1(ch):
    global r1
    global rk1
    global rk2
    if rk2 == 26:
        rk2 = 0
        rk1 += 1
        r1.append(r1.pop(0))
    return r1[input.index(ch)]


def reflector():
    pass


sc = clavijas('A',input,output)
print(sc)
s3 = rotor3(sc)
print(s3)
s2 = rotor2(s3)
print(s2)
s1 = rotor1(s2)
print(s1)
