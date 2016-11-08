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
    i = 0
    z = None
    flag = 2
    while flag != 0:
        i += 1
        deco = ExpM(n,i,p)
        if deco == alice:
            print('x de Alice: %i' % deco)
            flag -=1
        if deco == bob:
            print('x de Bob: %i' % deco)
            flag -=1
    return ExpM(bob,i,p)

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

print('---Ataque---')
sDescifrada = ataque(n,p,alice,bob)
print('Clave descifrada: %i' % sDescifrada)
