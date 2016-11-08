from multiprocessing import Process

def ExpM (n,x,p):
    #b = bin(x)[2:]
    b ="{0:b}".format(x)


    final = 1
    lenb = len(b) - 1
    n %= p
    if b[lenb] == '1':
        final = n
    while (lenb != 0):
        n = (n*n) % p
        lenb -= 1
        if b[lenb] == '1':
            final *= n
    return (final % p)

def ataque (n,p, alice, bob, i):
    #i = 0
    z = None
    flag = 2
    while flag != 0:
        i += 1
        deco = ExpM(n,i,p)
        if deco == alice:
            print('x de Alice: %i' % i)
            flag -=1
        if deco == bob:
            print('x de Bob: %i' % i)
            flag -=1
    return ExpM(bob,i,p)

# Ejemplo https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

n = int(7245627542842336859)  #65537 #5
p = int(3523269789483225643)  #1372933 #23

'''
xa = 2930009534032416290
xb = 6290936979721568605

alice =  ExpM(n,xa,p) # 8
print('Alice: %i' % alice)

bob = ExpM(n,xb,p)
print('Bob: %i' % bob)

alice_s = ExpM(bob,xa,p)
print('Alice s: %i' % alice_s)

bob_s = ExpM(alice,xb,p)
print('Bob s: %i' % bob_s)
'''

alice = int(2930009534032416290)#6
bob = int(6290936979721568605) #15 # Bob el más grande siempre.




# Lanzar 4 hilos.
def espacio(number,i):
    print('---Ataque---')
    sDescifrada = ataque(n,p,alice,bob,i)
    print('Clave descifrada: %i' % sDescifrada)
    print ("Proceso " + str(number) + " acabado")

p_list = []
espacios = (0,int(bob/4),int(bob/2),int((bob/4)*3))

if __name__ == '__main__':
    for number in range(4):
        p = Process(target=espacio, args=(number,espacios[number],))
        p_list.append(p)

for p in p_list:
    p.start()