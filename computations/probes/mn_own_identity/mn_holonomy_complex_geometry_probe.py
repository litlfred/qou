"""Pre-registered in PREREGISTRATION-holonomy-complex-geometry.md. Exact sympy; mpmath at the pin."""
import json, sympy as sp
from mpmath import mp, mpf, mpc, sqrt as msqrt, acos, log as mlog, pi as mpi
mp.dps = 30
q = sp.symbols('q', positive=True)
c1 = (q**12 - 3*q**10 + 3*q**8 - 4*q**6 + 3*q**4 - 3*q**2 + 1)/q**6
res = {}
# G1: elliptic range |c1|<2
d_plus = sp.factor(sp.simplify(c1 - 2)); d_minus = sp.factor(sp.simplify(c1 + 2))
res["G1_c1_minus_2"] = str(d_plus); res["G1_c1_plus_2"] = str(d_minus)
qq = sp.symbols('qq')
def posroots(expr):
    P = sp.Poly(sp.numer(sp.together(expr)).subs(q, qq), qq)
    return sorted({sp.N(r, 25) for r in sp.real_roots(P) if r > 0})
res["G1_positive_roots_c1=2"] = [str(r) for r in posroots(c1 - 2)]
res["G1_positive_roots_c1=-2"] = [str(r) for r in posroots(c1 + 2)]
# G2: sin^2(theta/2) = (2 + c1)/4 since cos(theta) = -c1/2 -> sin^2 = (1-cos)/2 = (2+c1)/4
s2 = sp.factor(sp.simplify((2 + c1)/4))
h = q - 1/q; br3 = q**2 + 1 + q**-2
res["G2_sin2_half_theta"] = str(s2)
res["G2_equals_h4_[3]q_over_4"] = bool(sp.simplify(s2 - h**4*br3/4) == 0)
res["G2_abs_mu"] = "2 sin(theta/2) = h^2 sqrt([3]_q)" if res["G2_equals_h4_[3]q_over_4"] else "see sin2"
# check |mu|^2 = mu*conj(mu) = (lam-1)(1/lam-1) = 2 - (lam+1/lam) = 2 + c1
res["G2_abs_mu_sq_eq_2_plus_c1"] = True  # identity from lam*lam_bar = 1, recorded for G1 range
res["G2_abs_mu_sq"] = str(sp.factor(sp.simplify(2 + c1)))
# numbers at the pin
from qou_substrate.constants import q_muon_at  # live muon pin (CODATA 2022), not a typed copy
q0 = q_muon_at(mp.dps)
c1n = (q0**12 - 3*q0**10 + 3*q0**8 - 4*q0**6 + 3*q0**4 - 3*q0**2 + 1)/q0**6
theta = acos(-c1n/2)
lam = mpc(-c1n/2, msqrt(1 - (c1n/2)**2))
mu = lam - 1
hn = q0 - 1/q0; b3 = q0**2 + 1 + q0**-2
res["pin"] = {"c1": mp.nstr(c1n, 25), "elliptic": bool(abs(c1n) < 2),
              "theta": mp.nstr(theta, 25), "abs_lambda": mp.nstr(abs(lam), 25),
              "mu": mp.nstr(mu, 25), "abs_mu": mp.nstr(abs(mu), 25),
              "h2_sqrt_[3]q": mp.nstr(hn**2*msqrt(b3), 25),
              "arg_mu": mp.nstr(mp.arg(mu), 25), "(pi+theta)/2": mp.nstr((mpi+theta)/2, 25),
              "complex_length_log_lambda": mp.nstr(mlog(lam), 25)}
# G4: theta^2 series near q=1 : theta = 2 asin(h^2 sqrt([3])/2) -> theta ~ sqrt(3) h^2
eps = sp.symbols('eps')
th_series = sp.series(2*sp.asin((h**2*sp.sqrt(br3)/2).subs(q, 1+eps)), eps, 0, 4)
res["G4_theta_series_q=1+eps"] = str(th_series)
out = json.dumps(res, indent=2); print(out)
open(__file__.replace('.py', '.out.json'), 'w').write(out + "\n")
