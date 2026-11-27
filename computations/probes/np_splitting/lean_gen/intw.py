import sympy as sp, itertools
exec(open('gen.py').read().split("if sys.argv[1]=='check'")[0].replace('import sympy as sp, itertools, sys','import sympy as sp, itertools'))
N={1:4,2:6,3:4}
def intertwiners(a,b):
    na,nb=N[a],N[b]; xs=sp.symbols(f'x0:{na*nb}'); P=sp.Matrix(nb,na,xs)
    eqs=[]
    for i in range(3):
        eqs+=list(P*gen(a,i,0)-gen(b,i,0)*P)
    sol=sp.solve(eqs,xs,dict=True)[0]
    Pg=P.subs(sol); free=sorted(Pg.free_symbols-{q},key=str)
    return [sp.simplify(Pg.subs({f:(1 if f==g else 0) for f in free})) for g in free]
basis={}
for a,b in [(3,2),(2,1),(1,2),(2,3),(1,3),(3,1)]:
    basis[(a,b)]=intertwiners(a,b); print(a,'->',b,len(basis[(a,b)]))
# M blocks for phi = tn - q^-2 tp, nucleon on 0..2
def Mblock(z):
    S=states(z); d=[]
    for s in S:
        nz=sum(1 for t in (0,1,2) if s[t]==0); w=K(s)
        d.append(w if nz==1 else (-w/q**2 if nz==2 else 0))
    return sp.diag(*d)
M={z:Mblock(z) for z in (1,2,3)}
# unknown functionals: for each intertwiner P (a->b) and free N (na x nb): contributes M_b += P N? careful: Tr(N word_b P)=Tr(N P word_a)
# Tr(N word_b P) = Tr(P N word_b). So functional: W -> Tr((P N) W_b) - Tr((N P) W_a) vanishes.
unk=[]; contrib={z:sp.zeros(N[z]) for z in (1,2,3)}
for (a,b),Ps in basis.items():
    for k,P in enumerate(Ps):
        ns=sp.symbols(f'n_{a}{b}{k}_0:{N[a]*N[b]}'); unk+=ns
        Nm=sp.Matrix(N[a],N[b],ns)
        contrib[b]+=P*Nm; contrib[a]-=Nm*P
# functional Tr(C W) equals Tr(M W) for all W iff C = M + (anything orthogonal to span of words). Strong: require C diag == M diag only matters on algebra; require C == M exactly.
eqs=[]
for z in (1,2,3): eqs+=list(contrib[z]-M[z])
sol=sp.solve(eqs,unk,dict=True)
print('solvable exactly:',bool(sol))
