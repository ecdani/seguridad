def ExpM (n,x,p):
    b = bin(x)[2:]

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

def ataque (n,p, alice, bob):
    i = 1
    z = None
    while True:
        deco = ExpM(n,i,p)
        if deco == alice:
            return ExpM(bob,i,p)
        elif deco == bob:
            return ExpM(alice,i,p)
        i += 1

# Ejemplo https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

n = 65537#5
p = 1372933 #23
xa = 5858999999#6
xb = 7888899999 #15

alice =  ExpM(n,xa,p) # 8
print('Alice: %i' % alice)

bob = ExpM(n,xb,p)
print('Bob: %i' % bob)

alice_s = ExpM(bob,xa,p)
print('Alice s: %i' % alice_s)

bob_s = ExpM(alice,xb,p)
print('Bob s: %i' % bob_s)

sDescifrada = ataque(n,p,alice,bob)
print('Clave descifrada: %i' % sDescifrada)
