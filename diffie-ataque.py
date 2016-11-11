from multiprocessing import Process

def ExpM (n,x,p):
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

def ataque (n,p, alice, bob, i,j):
    while i != j :
        i += 1
        deco = ExpM(n,i,p)
        if deco == alice:
            print('x de Alice: %i' % i)
        if deco == bob:
            print('x de Bob: %i' % i)

n = int(7245627542842336859)
p = int(3523269789483225643)

alice = int(2930009534032416290)
bob = int(6290936979721568605)

def espacio(number):
    number *= 10000000
    while True:
        print('---Ataque de %i a %i ---' % (number, number + 10000000))
        ataque(n,p,alice,bob,number,number + 10000000)
        number += 40000000

p_list = []

if __name__ == '__main__':
    for number in range(4):
        p = Process(target=espacio, args=(number,))
        p_list.append(p)

for p in p_list:
    p.start()