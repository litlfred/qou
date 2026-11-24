"""β_Bor-dressed vertex weight (prereg Addendum 19, audit §31).

Exact Q(q) arithmetic (sympy). Weight-zero space of V^{⊗4} (basis as h4_young_channel_vertex.py),
β_Bor = (σ1 σ2^{-1})^3 on the three quark strands, lepton strand 4 a spectator.
D1: W(s) = (β⊗1)_{ss}.  D2: W(s) = (Σ_λ q^{c(λ)} P_λ (β⊗1))_{ss}.
Mirror: σ ↦ σ^{-1}. Reversed order: strings reversed, quarks on strands 2-4.
mpmath only for the final evaluation at the proton q0 (40 dps).
"""
import sympy as sp
q=sp.symbols('q',positive=True); h=q-1/q
B=['uudd','udud','uddu','duud','dudu','dduu']; idx={b:i for i,b in enumerate(B)}
def R(i):
    M=sp.zeros(6)
    for j,b in enumerate(B):
        a,c=b[i],b[i+1]
        if a==c: M[j,j]=q
        elif a=='u': M[idx[b[:i]+'du'+b[i+2:]],j]+=1
        else: M[idx[b[:i]+'ud'+b[i+2:]],j]+=1; M[j,j]+=h
    return M
S=[R(0),R(1),R(2)]; I=sp.eye(6)
Si=[sp.simplify(s-h*I) for s in S]           # σ^{-1} = σ - h
for s,t in zip(S,Si): assert sp.simplify(s*t-I)==sp.zeros(6)
def power(M,k):
    r=I
    for _ in range(k): r=sp.simplify(r*M)
    return r
beta=power(S[0]*Si[1],3)      # quarks on strands 1-3
betaM=power(Si[0]*S[1],3)     # mirror
betaR=power(S[1]*Si[2],3)     # reversed order: quarks on strands 2-4
betaRM=power(Si[1]*S[2],3)
D=S[0]*S[1]*S[2]; F=sp.simplify(D**4)
c={'4':6,'31':2,'22':0}; ev={k:q**(2*v) for k,v in c.items()}
P={}
for k in c:
    num=I; den=1
    for k2 in c:
        if k2!=k: num=num*(F-ev[k2]*I); den*=(ev[k]-ev[k2])
    P[k]=sp.simplify(num/den)
Y=sp.simplify(sum((q**c[k]*P[k] for k in c),sp.zeros(6)))
init=['uddu','dudu','dduu']; fin=['uudd','udud','duud']
initR=['uudd','udud','uddu'][::-1]  # placeholder, recomputed below
# reversed order: lepton at strand 1, quarks 2-4
initR=['u'+x for x in ['udd','dud','ddu']]; finR=['d'+x for x in ['uud','udu','duu']]
def ratio(M,ini,fi):
    a=sum(M[idx[b],idx[b]] for b in ini); b_=sum(M[idx[b],idx[b]] for b in fi)
    return sp.factor(sp.simplify(a)), sp.factor(sp.simplify(b_)), sp.factor(sp.simplify(a/b_))
out={}
for name,M,ini,fi in [('D1',beta,init,fin),('D1_mirror',betaM,init,fin),('D1_rev',betaR,initR,finR),('D1_rev_mirror',betaRM,initR,finR),
                      ('D2',Y*beta,init,fin),('D2_mirror',Y*betaM,init,fin),('D2_rev',Y*betaR,initR,finR),('D2_rev_mirror',Y*betaRM,initR,finR)]:
    Wi,Wf,r=ratio(M,ini,fi); out[name]=r
    print(name,'\n  Wi =',Wi,'\n  Wf =',Wf,'\n  ratio =',r,'\n  at q=1:',sp.simplify(r.subs(q,1)))
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'substrate'))
import mpmath as mp
from q_parameter import Q_MP  # canonical proton q0 (70-digit mpf)
mp.mp.dps=40
q0=Q_MP; me=mp.mpf('0.51099895069'); E0=me/(q0*(q0-1))
for k,r in out.items():
    v=sp.lambdify(q,r,'mpmath')(q0); lg=mp.log(v)
    print(k,'ln ratio =',mp.nstr(lg,12),' dE =',mp.nstr(E0*lg,10),'MeV')
print('cell 2 ln q0 =',mp.nstr(2*mp.log(q0),12),' cell MeV',mp.nstr(2*E0*mp.log(q0),10))
