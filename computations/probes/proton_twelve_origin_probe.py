"""Probe: where does the -12 m_e in m_p/m_e = 2(Vol/hbar_q^2)F_Bor - 12 come from?

Pre-registration: docs/audits/2026-11-21-proton-minus-twelve-origin.md (section 1).
Lean twin: QOU/MassTheory/ProtonTwelveOrigin.lean.
Exact H_3(q) (T_i^2 = h T_i + 1, h = q - 1/q) with sympy; numbers at the muon pin
(CODATA 2022) at 70 dps mpmath. No float64 anywhere. Emits no witness; no number moves.
"""
import sympy as sp
from itertools import permutations
q, z = sp.symbols('q z', positive=True)
h = q - 1/q
# elements: dict perm(tuple)->coeff ; reduced words via S3
S = [tuple(p) for p in permutations(range(3))]
def s(i):  # simple transposition i,i+1 as perm
    p=list(range(3)); p[i],p[i+1]=p[i+1],p[i]; return tuple(p)
def comp(a,b): return tuple(a[b[k]] for k in range(3))  # a∘b
def length(p): return sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j])
def mulT(x, i):  # x * T_i
    out={}
    si=s(i)
    for w,c in x.items():
        ws=comp(w,si)
        if length(ws)>length(w):
            out[ws]=out.get(ws,0)+c
        else:
            out[ws]=out.get(ws,0)+c
            out[w]=out.get(w,0)+c*h
    return {k:sp.simplify(v) for k,v in out.items() if sp.simplify(v)!=0}
def word(letters):  # letters: list of (i, e) e=+1/-1
    x={tuple(range(3)):sp.Integer(1)}
    for i,e in letters:
        if e==1: x=mulT(x,i)
        else:
            y=mulT(x,i); 
            # T^-1 = T - h
            for k,v in x.items(): y[k]=y.get(k,0)-h*v
            x={k:sp.simplify(v) for k,v in y.items() if sp.simplify(v)!=0}
    return x
# Ocneanu trace on basis T_w: tr(T_w)= z^{#?}; use reduced words: tr(x T_{n-1} y)=z tr(xy) for x,y in H_{n-1}
# For S3: tr(1)=1, tr(T1)=tr(T2)=z, tr(T1T2)=tr(T2T1)=z^2, tr(T1T2T1)=tr(T1^2 T2)?? compute directly:
# T1T2T1 : tr = tr(T1 T2 T1) = z tr(T1^2) = z(h z + 1)
def trw(p):
    L=length(p)
    if L==0: return sp.Integer(1)
    if L==1: return z
    if L==2: return z**2
    return z*(h*z+1)
def tr(x): return sp.simplify(sum(c*trw(w) for w,c in x.items()))

import mpmath as mpm
mpm.mp.dps = 70
zD = q**3/(q**2+1)
qf3 = (q**2+1+q**-2)*(q+1/q)
def F_of(letters):
    return sp.simplify(tr(word(letters)).subs(z,zD)*qf3/q**3)
Fbor = F_of([(0,1),(1,-1)]*3)
Fe   = F_of([(0,1),(1,1),(0,1)])
FX   = F_of([(0,1),(1,-1)])
print("F_Bor(1) =", sp.limit(Fbor,q,1), " F_e(1) =", sp.limit(Fe,q,1), " F_X(1) =", sp.limit(FX,q,1))
print("tr_M(e) =", sp.factor(tr(word([(0,1),(1,1),(0,1)])).subs(z,zD)))
# C1: Laurent expansion of 2 F_Bor / hbar^2 in hbar  (q = 1/(1-u), u = hbar)
u=sp.symbols('u')
ser = sp.series((2*Fbor/((1-1/q)**2)).subs(q,1/(1-u)), u, 0, 2)
print("C1: 2F/hbar^2 =", ser, "  (times Vol for T/m_e)")
# C1b: h^2-expansion coefficients of F_Bor, F_e
hh=sp.symbols('hh')
def h2coef(F):
    # F at q=1+e, series in e then convert: report d/d(h^2) at q=1
    e=sp.symbols('e'); s=sp.series(F.subs(q,1+e),e,0,3).removeO()
    return sp.nsimplify(s.coeff(e,0)), sp.nsimplify(s.coeff(e,1)), sp.nsimplify(s.coeff(e,2))
print("F_Bor series in (q-1):", h2coef(Fbor)); print("F_e series in (q-1):", h2coef(Fe))
# C3: q*tr(V3_A) closed form on proton weight space from the Lean theorem
trV3A = (q**12-3*q**10+3*q**8-5*q**6+3*q**4-3*q**2+1)/q**6
print("C3: q*tr(V3_A) at q=1:", sp.limit(q*trV3A,q,1), " series:", h2coef(q*trV3A))
# numbers at q0 (muon pin, CODATA 2022)
me = mpm.mpf('0.51099895069'); r_mu = mpm.mpf('206.7682827'); r_p = mpm.mpf('1836.152673426')
Vol = 2*mpm.clsin(2, mpm.pi/3)
q0 = mpm.findroot(lambda x: Vol/(1-1/x)**2 - r_mu, mpm.mpf('1.11'))
Fb0 = sp.lambdify(q, Fbor, 'mpmath')(q0); Fe0 = sp.lambdify(q, Fe, 'mpmath')(q0)
R30 = sp.lambdify(q, q*trV3A, 'mpmath')(q0)
T = 2*r_mu*Fb0   # tower / m_e
print("q0(muon) =", mpm.nstr(q0,25), " h^2 =", mpm.nstr((q0-1/q0)**2,8))
print("T/m_e =", mpm.nstr(T,20), " c_req = T - mp/me =", mpm.nstr(T-r_p,15))
for name,c in [("12",mpm.mpf(12)),("2F_Bor(q0)",2*Fb0),("4F_e(q0)",4*Fe0),("-4 q tr V3A(q0)",-4*R30)]:
    mpp = T - c
    print(f"{name:18s} c={mpm.nstr(c,12):>16s}  m_p resid ppb = {mpm.nstr((mpp-r_p)/r_p*10**9,8):>14s}  dm_n (MeV) vs c=12: {mpm.nstr(-(c-12)*me,8)}")
