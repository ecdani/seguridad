def ExpM (n,x,p):
    b = bin(x)[2:]

    k = 1
    final = 1
    lenb = len(b)
    ar = n % p
    if b[lenb - k] == '1':
        final = ar
    while (lenb != k):
        ar = (ar*ar) % p
        k += 1
        if b[lenb - k] == '1':
            final = final * ar
    return (final % p)

# Ejemplo https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
alice =  ExpM(5,6,23) # 8
print('Alice: '+str(alice))

bob = ExpM(5,15,23)
print('Bob: '+str(bob))

alice_s = ExpM(bob,6,23)
print('Alice s: '+str(alice_s))

bob_s = ExpM(alice,15,23)
print('Bob s: '+str(bob_s))
