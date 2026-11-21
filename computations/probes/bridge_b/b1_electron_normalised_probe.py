"""Bridge B test B1 (pre-registered in b1_preregistration.md). Exact sympy over Q(q);
numbers at q0 via mpmath at 45 dps. No float arithmetic."""
import itertools, sympy as sp
from mpmath import mp, mpf
mp.dps = 45
qs = sp.Rational('1.1099785827513808075916690956107688798744991218736')
q = sp.symbols('q', positive=True); h = q - 1/q
R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
I2 = sp.eye(2); s1 = sp.kronecker_product(R, I2); s2 = sp.kronecker_product(I2, R)
V = s1 * s2.inv()
basis = list(itertools.product(range(2), repeat=3)); K = [q, 1/q]
def T(W, wt=None):
    tot = 0
    for k, b in enumerate(basis):
        if wt is None or tuple(sorted(b)) == wt:
            kk = 1
            for x in b: kk *= K[x]
            tot += kk * W[k, k]
    return sp.factor(sp.simplify(tot / (q + 1/q)**3))
def at(e): return mpf(str(sp.N(e.subs(q, qs), 50)))
from qou_substrate.constants import MASS_RATIO_P_E_STR  # CODATA m_p/m_e, not a typed copy
me = mpf('0.51099895069'); cod = mpf('1.29333205'); mpme = mpf(MASS_RATIO_P_E_STR)
hh = q - 1/q
borr = (4 + hh**2 - 3*hh**4 - hh**6) / (hh**2 + 4)
print('check T(1) =', T(sp.eye(8)), ';  T(sigma1) =', T(s1), '(z_D =', sp.factor(q**3/(q**2+1)), ')')
V3 = V**3; V6 = V**6
print('check T(V^3) - tr_M(Borromean) =', sp.simplify(T(V3) - borr))
nuc = {'V^3': V3, 'V^6': V6}
ele = {'V^0': sp.eye(8), 'V^3': V3, 'V^6': V6}
Te = {k: T(W) for k, W in ele.items()}
for k, v in Te.items(): print(f'T(e={k}) =', v, '=', mp.nstr(at(v), 15))
for nk, W in nuc.items():
    tp = T(W, (0,0,1)); tn = T(W, (0,1,1)); tf = T(W)
    d = at(tn - tp)
    print(f'\nnucleon {nk}: T(p) = {mp.nstr(at(tp),15)}  T(n) = {mp.nstr(at(tn),15)}  T_full = {mp.nstr(at(tf),15)}  T(n)-T(p) = {mp.nstr(d,15)}')
    for ek, te in Te.items():
        tev = at(te)
        dm = me * abs(d) / abs(tev)
        c2r = abs(at(tp)) / abs(tev); c2f = abs(at(tf)) / abs(tev)
        print(f'  e={ek}: B1 dm = {mp.nstr(dm,10)} MeV ({mp.nstr(100*(dm/cod-1),6)} %) | '
              f'C2 m_p/m_e: restricted {mp.nstr(c2r,8)}, full {mp.nstr(c2f,8)}  (CODATA {mp.nstr(mpme,10)})')
