"""PRE-REGISTERED (written before running), np-splitting audit §18.
Question: which corpus scale converts the level-2 weight-space u/d difference into MeV?
Corpus finding (searched before writing this): the derived hadronic scale is
  E0 = m_e/(q(q-1))  (CAL-1 + CAL-2 only; notation-collisions, mass-formula-validation),
  tower-summed E0_full = E0/(1 - hbar_q^2), canonical per the full-tower ruling,
described as "the MeV-per-dimensionless-trace-unit conversion for hadronic predictions",
used LINEARLY on trace differences (Q_beta = |Delta net| * E0; Q_beta = |eps(Delta)| * E0).
alpha = m_e*8G has no such derivation for this use (§15, §17).
Fixed choices:
  element  = the ruled gamma-gamma nucleon V^3, V = s1 s2^{-1} (V^6 also passes; reported).
  trace    = D quantum trace on (C^2)^{x3}, K = diag(q,1/q) (forced, Lean), normalised tr(1)=1.
  restrict = to p weight (u,u,d) and n weight (u,d,d), u = e1 (forced via PR #7971).
Candidates:
  D1 (primary, linear, corpus form):  dm = E0_full * |t_n - t_p|
  D1'                                  dm = E0^(0) * |t_n - t_p|  (order-zero, reported only)
  D2 (log form kept, scale swapped):  dm = E0_full * 2 ln q
CODATA 1.29333205 MeV is comparison only; nothing is selected by residual.
"""
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import itertools, sympy as sp
from mpmath import mp, mpf, log
mp.dps=40
qs=sp.Rational('1.1099785827513808075916690956107688798744991218736')
q=sp.symbols('q',positive=True); h=q-1/q
R=sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
I2=sp.eye(2); s1=sp.kronecker_product(R,I2); s2=sp.kronecker_product(I2,R)
V=s1*s2.inv()
basis=list(itertools.product(range(2),repeat=3))
K=[q,1/q]
def t(W,wt):
    tot=0
    for k,b in enumerate(basis):
        if tuple(sorted(b))==wt:
            kk=1
            for x in b: kk*=K[x]
            tot+=kk*W[k,k]
    return sp.simplify(tot/(q+1/q)**3)
me=mpf('0.51099895069'); cod=mpf('1.29333205')
qm=mpf(str(sp.N(qs,45))); hb=1-1/qm
E00=_qbeta_e0.order_zero_scaled(me, qm); E0f=E00/(1-hb**2)
print('E0^(0) =',mp.nstr(E00,12),' E0_full =',mp.nstr(E0f,12))
for name,W in [('V^3',V**3),('V^6',V**6)]:
    tp=t(W,(0,0,1)); tn=t(W,(0,1,1))
    print(name,' t_p =',sp.factor(tp),'  t_n/t_p =',sp.simplify(tn/tp))
    d=abs(mpf(str(sp.N((tn-tp).subs(q,qs),45))))
    for lab,E in (('D1 E0_full',E0f),("D1' E0^(0)",E00)):
        v=E*d; print(f'  {lab}: |t_n-t_p| = {mp.nstr(d,10)}  dm = {mp.nstr(v,10)} MeV  {mp.nstr(100*(v/cod-1),6)} %')
v=E0f*2*log(qm); print('D2 E0_full*2lnq =',mp.nstr(v,10),'MeV',mp.nstr(100*(v/cod-1),6),'%')
