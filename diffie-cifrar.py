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

n = int(7245627542842337021864103589)
p = int(9412350003523269789483225961)

#xa = 2930009534032416290
xb = int(8888888897888888899)
alice = int(7256978686144453597453239000) # Jose

#alice =  ExpM(n,xa,p) # 8
#print('Alice: %i' % alice)

bob = ExpM(n,xb,p)
print('Bob: %i' % bob)

#alice_s = ExpM(bob,xa,p)
#print('Alice s: %i' % alice_s)

bob_s = ExpM(alice,xb,p)
print('Bob s: %i' % bob_s)
