"""H4 Young-channel vertex energy (prereg Addendum 18, audit §29).

Exact Q(q) computation (sympy): the Jimbo generators on the weight-zero space of V^{⊗4},
central idempotents P_λ as Lagrange polynomials in the full twist, state weights
W(s) = Σ_λ q^{c(λ)} (P_λ)_{ss}, summed over the initial / final sets. The only
mpmath step is the final evaluation at the proton q₀ (40 dps). No float arithmetic.
Lean twin of the algebra on the summed weights: QOU/QBeta/H4VertexEnergy.lean.
"""
import sympy as sp, itertools
q=sp.symbols('q',positive=True); h=q-1/q
B=['uudd','udud','uddu','duud','dudu','dduu']
idx={b:i for i,b in enumerate(B)}
def R(i):
    M=sp.zeros(6)
    for j,b in enumerate(B):
        a,c=b[i],b[i+1]
        if a==c: M[j,j]=q
        elif a=='u':  # ud -> du
            M[idx[b[:i]+'du'+b[i+2:]],j]+=1
        else:         # du -> ud + h du
            M[idx[b[:i]+'ud'+b[i+2:]],j]+=1; M[j,j]+=h
    return M
S=[R(0),R(1),R(2)]
I=sp.eye(6)
for s in S: assert sp.simplify(s*s-h*s-I)==sp.zeros(6)
assert sp.simplify(S[0]*S[1]*S[0]-S[1]*S[0]*S[1])==sp.zeros(6)
assert sp.simplify(S[1]*S[2]*S[1]-S[2]*S[1]*S[2])==sp.zeros(6)
assert sp.simplify(S[0]*S[2]-S[2]*S[0])==sp.zeros(6)
D=S[0]*S[1]*S[2]; F=sp.simplify((D**4))
c={'4':6,'31':2,'22':0}
ev={k:q**(2*v) for k,v in c.items()}
# check minimal poly
P={}
for k in c:
    num=I; den=1
    for k2 in c:
        if k2!=k: num=num*(F-ev[k2]*I); den*=(ev[k]-ev[k2])
    P[k]=sp.simplify(num/den)
for k in c: assert sp.simplify(P[k]*P[k]-P[k])==sp.zeros(6)
assert sp.simplify(sum(P.values(),sp.zeros(6))-I)==sp.zeros(6)
print({k:sp.simplify(P[k].trace()) for k in P})
W=sp.simplify(sum((q**c[k]*P[k] for k in c),sp.zeros(6)))
print('W diag:',[sp.factor(W[i,i]) for i in range(6)])
print('trace',sp.factor(W.trace()))
init=['uddu','dudu','dduu']; fin=['uudd','udud','duud']
Wi=sp.factor(sum(W[idx[b],idx[b]] for b in init)); Wf=sp.factor(sum(W[idx[b],idx[b]] for b in fin))
print('Wi',Wi); print('Wf',Wf); r=sp.factor(Wi/Wf); print('ratio',r)
# reversed order: lepton first -> init = u + quarks(1u): 'uudd'? reversed strings
init_r=[b[::-1] for b in init]; fin_r=[b[::-1] for b in fin]
Wir=sum(W[idx[b],idx[b]] for b in init_r); Wfr=sum(W[idx[b],idx[b]] for b in fin_r)
print('rev ratio',sp.factor(Wir/Wfr), sp.simplify(Wir/Wfr*r))
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'substrate'))
import mpmath as mp
from q_parameter import Q_MP  # canonical proton q0 (70-digit mpf)
mp.mp.dps=40
q0=Q_MP; me=mp.mpf('0.51099895069'); E0=me/(q0*(q0-1))
rv=sp.lambdify(q,r,'mpmath')(q0)
print('dE4',mp.nstr(E0*mp.log(rv),10),'cell',mp.nstr(2*E0*mp.log(q0),10))
