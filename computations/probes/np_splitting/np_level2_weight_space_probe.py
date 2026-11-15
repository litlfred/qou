"""PRE-REGISTERED (2026-11-15 18:55Z, before running).  Bean qou-q1a4, step 3.
Level-2 Schur–Weyl (convention D = gl_2): H_3(q) acts on V^{⊗3}, V = C^2 = span(e1, e2),
by the Jimbo R-matrix  R(e_i⊗e_i) = q e_i⊗e_i,  R(e1⊗e2) = e2⊗e1,  R(e2⊗e1) = e1⊗e2 + h e2⊗e1.
Check (printed): Hecke relation; the weighted trace tr(x) = Tr(K^{⊗n} rho(x))/Tr(K^{⊗n}) is Markov with z = z_D
  for K = diag(q, 1/q) and for K = diag(1/q, q) (both tested; neither selected).
Weight spaces: the H_3 action preserves the number of e1 factors.  Flavour labelling is a CHOICE,
  reported both ways: (L1) u = e1, d = e2;  (L2) u = e2, d = e1.
  proton = weight space with two u, one d; neutron = one u, two d.
Elements (fixed in advance): half twist R1 R2 R1; full twist (R1R2R1)^2; γγ candidate V^3, V = R1 R2^{-1} (PR #7741).
Quantities: T_mu(x) = Tr(K^{⊗3} rho(x) Pi_mu) (raw; the common 1/Tr K^{⊗3} cancels in n/p),
  and the sector-normalised T_mu(x)/Tr(K^{⊗3} Pi_mu).
Report dPhi = log|T_n| - log|T_p| and alpha*|dPhi| (alpha = m_e*8G); CODATA printed for comparison only.
Exact over Q(q) (sympy), numbers at the 50-digit proton q0.  No outcome selects anything."""
import sympy as sp, mpmath as mp, itertools
from qou_substrate.constants import q_at  # proton pin, derived, not a typed copy
q=sp.symbols('q',positive=True); h=q-1/q
R=sp.zeros(4,4)
idx=lambda i,j:2*i+j
R[idx(0,0),idx(0,0)]=q; R[idx(1,1),idx(1,1)]=q
R[idx(1,0),idx(0,1)]=1           # R e1⊗e2 = e2⊗e1   (column = input)
R[idx(0,1),idx(1,0)]=1; R[idx(1,0),idx(1,0)]=h   # R e2⊗e1 = e1⊗e2 + h e2⊗e1
assert sp.simplify((R-q*sp.eye(4))*(R+sp.eye(4)/q))==sp.zeros(4,4)
I2=sp.eye(2)
R1=sp.kronecker_product(R,I2); R2=sp.kronecker_product(I2,R)
R1i=sp.simplify(R1.inv()); R2i=sp.simplify(R2.inv())
assert sp.simplify(R1*R2*R1-R2*R1*R2)==sp.zeros(8,8)
zD=q**3/(q**2+1)
def Kn(K,n):
    M=K
    for _ in range(n-1): M=sp.kronecker_product(M,K)
    return M
Ks={'K=diag(q,1/q)':sp.diag(q,1/q),'K=diag(1/q,q)':sp.diag(1/q,q)}
for kn,K in Ks.items():
    z2=sp.simplify((Kn(K,2)*R).trace()/Kn(K,2).trace())
    # Markov at n=3: tr(x R2) = z tr(x) for x in {1, R1}
    t=lambda X: sp.simplify((Kn(K,3)*X).trace()/Kn(K,3).trace())
    print(kn,': z(n=2) - z_D =',sp.simplify(z2-zD),'; Markov n=3 checks:',sp.simplify(t(R2)-zD*t(sp.eye(8))),sp.simplify(t(R1*R2)-zD*t(R1)))
els={'half twist':R1*R2*R1,'full twist':(R1*R2*R1)**2,'gg V^3':(R1*R2i)**3}
basis=list(itertools.product((0,1),repeat=3))  # 0 = e1, 1 = e2; index = 4a+2b+c
def Pi(n_e1):
    return sp.diag(*[1 if sum(1 for x in b if x==0)==n_e1 else 0 for b in basis])
mp.mp.dps=40; q0=mp.mpf(q_at(60))
al=mp.mpf('0.51099895069')*8*mp.catalan; tgt=mp.mpf('1.29333378')
for kn,K in Ks.items():
  K3=Kn(K,3)
  for lab,(pe1,ne1) in (('L1 u=e1',(2,1)),('L2 u=e2',(1,2))):
    for en,X in els.items():
      for norm in ('raw','sector'):
        Tp=sp.simplify((K3*X*Pi(pe1)).trace()); Tn=sp.simplify((K3*X*Pi(ne1)).trace())
        if norm=='sector': Tp=Tp/(K3*Pi(pe1)).trace(); Tn=Tn/(K3*Pi(ne1)).trace()
        r=sp.factor(sp.simplify(Tn/Tp)) if sp.simplify(Tp)!=0 else None
        if r is None or r==0: print(kn,lab,en,norm,': degenerate',Tp,Tn); continue
        d=mp.log(abs(sp.lambdify(q,r,'mpmath')(q0)))
        print(f'{kn} {lab} {en:10s} {norm:6s}: n/p = {r};  dPhi={mp.nstr(d,7)}  Dm={mp.nstr(al*abs(d),6)}  vs CODATA {mp.nstr((al*abs(d)/tgt-1)*100,4)}%')
