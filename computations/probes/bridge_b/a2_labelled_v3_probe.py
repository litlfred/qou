"""Arm 2 'labelled V^3' probe (pre-registered in a2_preregistration.md). Exact over Q(q)."""
import sympy as sp
from sympy import kronecker_product as kp
from mpmath import mp, mpf, catalan
mp.dps = 40
q = sp.symbols('q', positive=True)
h = q - 1/q
R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
Ri = R.inv().applyfunc(sp.simplify)
I2 = sp.eye(2)
K = sp.diag(q, 1/q)
K3 = kp(kp(K,K),K)
def gen(M, i):  # i = 1 or 2
    return kp(M, I2) if i == 1 else kp(I2, M)
two = q + 1/q
Wloc = (2/(q**2+1)) * sp.Rational(1,2) * (R + Ri)
word = [(1, +1), (2, -1)] * 3   # V^3 = (s1 s2^-1)^3
def T(Wm):
    return sp.simplify((K3*Wm).trace() / two**3)
def labelled(labels):
    lab = list(labels); M = sp.eye(8); nud = 0
    for (i, s) in word:
        a, b = lab[i-1], lab[i]
        if a == b:
            loc = R if s > 0 else Ri
        else:
            loc = Wloc; nud += 1
        M = M * gen(loc, i)
        lab[i-1], lab[i] = b, a
    assert lab == list(labels), "labels must close up"
    return T(M), nud
q0 = mpf('1.1099785827513808')
me = mpf('0.51099895069')
alpha = me * 8 * catalan
E0 = me / (q0*(q0-1))
codata = mpf('1.29333378')
# sanity: unlabelled V^3
Mv = sp.eye(8)
for (i, s) in word: Mv = Mv * gen(R if s > 0 else Ri, i)
print("sanity T(V^3) at q0:", sp.N(T(Mv).subs(q, sp.Rational(str(q0))), 15))
for k in range(3):
    p = ['u','u','u']; p[k] = 'd'
    n = ['d','d','d']; n[k] = 'u'
    tp, np_ = labelled(p); tn, nn = labelled(n)
    tpv = mpf(str(sp.N(tp.subs(q, sp.Rational(str(q0))), 45)))
    tnv = mpf(str(sp.N(tn.subs(q, sp.Rational(str(q0))), 45)))
    r = tnv/tpv
    dm_log = alpha*abs(mp.log(r)); dm_lin = E0*abs(tnv-tpv)
    print(f"odd quark on strand {k+1}: ud crossings p={np_} n={nn}")
    print("  t_p =", sp.factor(tp)); print("  t_n =", sp.factor(tn))
    print(f"  t_p={mp.nstr(tpv,12)} t_n={mp.nstr(tnv,12)} r=t_n/t_p={mp.nstr(r,12)} (q^-2={mp.nstr(q0**-2,12)})")
    print(f"  dm log-form (H_alpha) = {mp.nstr(dm_log,8)} MeV ({mp.nstr(100*(dm_log/codata-1),5)} %)")
    print(f"  dm linear E0 form     = {mp.nstr(dm_lin,8)} MeV ({mp.nstr(100*(dm_lin/codata-1),5)} %)")
