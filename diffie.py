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

# Ejemplo https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
alice =  ExpM(5,6,23) # 8
print('Alice: %i' % alice)

bob = ExpM(5,15,23)
print('Bob: %i' % bob)

alice_s = ExpM(bob,6,23)
print('Alice s: %i' % alice_s)

bob_s = ExpM(alice,15,23)
print('Bob s: %i' % bob_s)
