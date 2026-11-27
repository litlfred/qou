import sys
exec(open('deg5.py').read())
t12,t13,t14,t23,t24,t34=[T(g) for g in G]
X_,Y_=0,1
def ev(lie,a,b):  # lie given as nested tuple tree of 'X','Y'
    if lie=='X': return a
    if lie=='Y': return b
    return br(ev(lie[0],a,b),ev(lie[1],a,b))
XXY=('X',('X','Y')); YXY=('Y',('X','Y'))
# deg-3 pentagon (linear) for psi = a XXY + b YXY
U=add(t13,t23)
def psi(c,a,b): return add(sc(c[0],ev(XXY,a,b)),sc(c[1],ev(YXY,a,b)))
def pentdef(c):
    return add(psi(c,t12,add(t23,t24)),psi(c,U,t34),sc(-1,psi(c,t23,t34)),sc(-1,psi(c,add(t12,t13),add(t24,t34))),sc(-1,psi(c,t12,t23)))
# need deg3 ideal check
M3,wi3=ideal_basis(3); B3,piv3=rrefp(M3)
def in3(x):
    v=np.zeros(216,dtype=np.int64)
    for w,c in x.items(): v[wi3[w]]=c%p
    for i,c in enumerate(piv3):
        if v[c]: v=(v-v[c]*B3[i])%p
    return not v.any()
for c in [(1,0),(0,1),(1,1),(1,-1)]: print('pentagon deg3',c,in3(pentdef(c)))
def test(c):
    Ka=psi(c,t12,t23); Kb=psi(c,U,t34); Kc=psi(c,t12,add(t23,t24))
    d23=br(t23,Ka); d34=br(t34,Kb); dw=br(add(t23,t24),add(Kc,Kb))
    d13=sc(-1,d23); d24=add(dw,sc(-1,d23))
    X=add(br(t13,d24),br(d13,t24))
    return in5(X)
for c in [(1,0),(0,1),(1,1),(1,-1)]: print('[s13,s24]_5 zero for',c,test(c))
