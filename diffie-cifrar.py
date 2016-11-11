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

n = int(7245627542842337021864103589)
p = int(9412350003523269789483225961)

xa = int(2115478207654128809) # Jose
xb = int(8888888897888888899) # Dani

alice =  ExpM(n,xa,p)
print('JoseMaria: %i' % alice)

bob = ExpM(n,xb,p)
print('Dani: %i' % bob)

alice_s = ExpM(bob,xa,p)
print('JoseMaria s: %i' % alice_s)

bob_s = ExpM(alice,xb,p)
print('Dani s: %i' % bob_s)
